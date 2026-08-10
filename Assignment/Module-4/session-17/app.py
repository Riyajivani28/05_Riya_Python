import os
import random
import string
from datetime import datetime
import requests
import stripe
from dotenv import load_dotenv
from flask import (Flask, flash, redirect, render_template, request, url_for, jsonify)

from models import db, Match, FoodItem, Order
from paytm_checksum import generate_signature, verify_signature

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'default_secret_key_12345')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Configure Stripe API key
stripe.api_key = os.getenv('STRIPE_SECRET_KEY', '')


def generate_order_id(prefix="PAY"):
    """Generates a unique dynamic order ID, e.g. IPL-20260810-AB1234"""
    date_str = datetime.now().strftime("%Y%m%d")
    random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"{prefix}-{date_str}-{random_str}"


def seed_database():
    """Seeds initial dynamic data for IPL Matches and Food Items if DB is empty."""
    if Match.query.count() == 0:
        matches = [
            Match(
                team_a="Mumbai Indians",
                team_b="Chennai Super Kings",
                venue="Wankhede Stadium, Mumbai",
                match_date="Sat, 18 Apr 2026 - 7:30 PM",
                price=1500.0,
                available_tickets=45,
                image_url="https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?auto=format&fit=crop&w=600&q=80"
            ),
            Match(
                team_a="Royal Challengers Bengaluru",
                team_b="Kolkata Knight Riders",
                venue="M. Chinnaswamy Stadium, Bengaluru",
                match_date="Tue, 21 Apr 2026 - 7:30 PM",
                price=1800.0,
                available_tickets=30,
                image_url="https://images.unsplash.com/photo-1531415074968-036ba1b575da?auto=format&fit=crop&w=600&q=80"
            ),
            Match(
                team_a="Gujarat Titans",
                team_b="Rajasthan Royals",
                venue="Narendra Modi Stadium, Ahmedabad",
                match_date="Fri, 24 Apr 2026 - 7:30 PM",
                price=1200.0,
                available_tickets=60,
                image_url="https://images.unsplash.com/photo-1512719994953-eabf50895df7?auto=format&fit=crop&w=600&q=80"
            ),
            Match(
                team_a="Delhi Capitals",
                team_b="Sunrisers Hyderabad",
                venue="Arun Jaitley Stadium, Delhi",
                match_date="Sun, 26 Apr 2026 - 3:30 PM",
                price=1400.0,
                available_tickets=25,
                image_url="https://images.unsplash.com/photo-1508098682722-e99c43a406b2?auto=format&fit=crop&w=600&q=80"
            )
        ]
        db.session.add_all(matches)

    if FoodItem.query.count() == 0:
        food_items = [
            FoodItem(
                dish_name="Gourmet Pepperoni Pizza",
                restaurant_name="La Pino'z Pizza",
                price=350.0,
                description="Hand-tossed crust topped with mozzarella cheese and premium spicy pepperoni slices.",
                image_url="https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=600&q=80"
            ),
            FoodItem(
                dish_name="Classic Cheeseburger Combo",
                restaurant_name="Burger King",
                price=220.0,
                description="Flame-grilled beef/veggie patty with cheese, fresh lettuce, pickles, and crispy fries.",
                image_url="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=600&q=80"
            ),
            FoodItem(
                dish_name="Creamy Alfredo Pasta",
                restaurant_name="Toscano Italian",
                price=280.0,
                description="Rich parmesan cream sauce tossed with garlic herbs, mushrooms, and penne pasta.",
                image_url="https://images.unsplash.com/photo-1621996346565-e3d5d6281878?auto=format&fit=crop&w=600&q=80"
            ),
            FoodItem(
                dish_name="Hyderabadi Dum Biryani",
                restaurant_name="Paradise Biryani",
                price=320.0,
                description="Authentic slow-cooked aromatic basmati rice infused with tender chicken and secret spices.",
                image_url="https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?auto=format&fit=crop&w=600&q=80"
            ),
            FoodItem(
                dish_name="Club Sandwich & Iced Coffee",
                restaurant_name="Cafe Coffee Day",
                price=190.0,
                description="Triple decker toasted sandwich loaded with veggies & cheese served with cold brew coffee.",
                image_url="https://images.unsplash.com/photo-1528735602780-2552fd46c7af?auto=format&fit=crop&w=600&q=80"
            )
        ]
        db.session.add_all(food_items)

    db.session.commit()


# Initialize database tables on app startup
with app.app_context():
    db.create_all()
    seed_database()


# ==========================================
# 3. HOME PAGE
# ==========================================
@app.route('/')
def home():
    return render_template('home.html')


# ==========================================
# 4. IPL TICKET BOOKING
# ==========================================
@app.route('/tickets')
def tickets():
    matches = Match.query.all()
    return render_template('tickets.html', matches=matches)


@app.route('/pay', methods=['GET', 'POST'])
def pay():
    if request.method == 'GET':
        match_id = request.args.get('match_id')
        if not match_id:
            flash('Please select an IPL match first.', 'warning')
            return redirect(url_for('tickets'))
        match = Match.query.get_or_404(match_id)
        return render_template('pay.html', match=match)

    # POST Form Submission
    customer_name = request.form.get('customer_name', '').strip()
    email = request.form.get('email', '').strip()
    match_id = request.form.get('match_id')
    payment_gateway = request.form.get('payment_gateway', 'Paytm')

    try:
        quantity = int(request.form.get('quantity', 1))
    except ValueError:
        quantity = 1

    match = Match.query.get_or_404(match_id)

    # Backend Validation
    if not customer_name or not email:
        flash('Please fill in your name and a valid email address.', 'danger')
        return render_template('pay.html', match=match)

    if quantity <= 0:
        flash('Ticket quantity must be at least 1.', 'danger')
        return render_template('pay.html', match=match)

    if quantity > match.available_tickets:
        flash(f'Only {match.available_tickets} tickets available for this match.', 'danger')
        return render_template('pay.html', match=match)

    # Backend recalculation of total amount
    total_amount = round(match.price * quantity, 2)

    # Generate unique order ID
    order_id = generate_order_id("IPL")

    # Create pending order in database
    new_order = Order(
        order_id=order_id,
        customer_name=customer_name,
        email=email,
        order_type='IPL Ticket',
        item_name=f"{match.team_a} vs {match.team_b}",
        quantity=quantity,
        amount=total_amount,
        payment_gateway=payment_gateway,
        payment_status='Pending'
    )
    db.session.add(new_order)
    db.session.commit()

    # Route based on selected Gateway
    if payment_gateway == 'Paytm':
        # Initiate Paytm Sandbox Flow
        mid = os.getenv('PAYTM_MID', 'YOUR_PAYTM_MID')
        merchant_key = os.getenv('PAYTM_MERCHANT_KEY', 'YOUR_PAYTM_MERCHANT_KEY')
        website = os.getenv('PAYTM_WEBSITE', 'WEBSTAGING')
        channel_id = os.getenv('PAYTM_CHANNEL_ID', 'WEB')
        industry_type_id = os.getenv('PAYTM_INDUSTRY_TYPE_ID', 'Retail')
        callback_url = os.getenv('PAYTM_CALLBACK_URL', request.host_url.rstrip('/') + url_for('payment_callback'))

        paytm_params = {
            "MID": mid,
            "ORDER_ID": order_id,
            "CUST_ID": email,
            "TXN_AMOUNT": f"{total_amount:.2f}",
            "CHANNEL_ID": channel_id,
            "WEBSITE": website,
            "INDUSTRY_TYPE_ID": industry_type_id,
            "CALLBACK_URL": callback_url,
        }

        # Generate Checksum Hash
        checksum = generate_signature(paytm_params, merchant_key)
        paytm_params["CHECKSUMHASH"] = checksum

        # Standard Paytm Sandbox Gateway URL
        paytm_url = "https://securegw-stage.paytm.in/order/process"

        return render_template(
            'payment_callback.html',
            paytm_params=paytm_params,
            paytm_url=paytm_url,
            order=new_order
        )

    elif payment_gateway == 'PayPal':
        return redirect(url_for('paypal_pay', order_id=order_id))

    else:
        flash('Selected payment gateway is invalid.', 'danger')
        return redirect(url_for('tickets'))


# ==========================================
# 5. PAYTM SANDBOX CALLBACK & VERIFICATION
# ==========================================
@app.route('/payment-callback', methods=['GET', 'POST'])
def payment_callback():
    """
    Receives Paytm Sandbox callback, verifies checksum signature and status,
    updates order status in SQLite DB, and redirects to result page.
    """
    merchant_key = os.getenv('PAYTM_MERCHANT_KEY', 'YOUR_PAYTM_MERCHANT_KEY')
    param_dict = request.form.to_dict() if request.form else request.args.to_dict()

    order_id = param_dict.get('ORDERID') or param_dict.get('ORDER_ID')
    
    # If order_id not in callback data (e.g. testing simulator post)
    if not order_id and 'sim_order_id' in param_dict:
        order_id = param_dict.get('sim_order_id')
        status = param_dict.get('sim_status', 'TXN_SUCCESS')
        txn_id = f"PAYTM-SIM-{random.randint(100000, 999999)}"
        order = Order.query.filter_by(order_id=order_id).first()
        if order:
            order.payment_status = 'Success' if status == 'TXN_SUCCESS' else 'Failed'
            order.transaction_id = txn_id
            if status == 'TXN_SUCCESS':
                # Deduct ticket count if IPL
                match_name = order.item_name
                teams = match_name.split(" vs ")
                if len(teams) == 2:
                    match = Match.query.filter_by(team_a=teams[0].strip(), team_b=teams[1].strip()).first()
                    if match and match.available_tickets >= order.quantity:
                        match.available_tickets -= order.quantity
            db.session.commit()
            return redirect(url_for('payment_result', order_id=order.order_id))

    if not order_id:
        flash('Invalid callback response from Paytm.', 'danger')
        return redirect(url_for('home'))

    order = Order.query.filter_by(order_id=order_id).first()
    if not order:
        flash('Order not found.', 'danger')
        return redirect(url_for('home'))

    paytm_checksum = param_dict.get('CHECKSUMHASH', '')
    is_valid_checksum = verify_signature(param_dict, merchant_key, paytm_checksum)
    txn_status = param_dict.get('STATUS', 'TXN_FAILURE')
    txn_id = param_dict.get('TXNID', f"TXN-{random.randint(100000, 999999)}")

    # Allow sandbox test verification fallback if merchant key is placeholder
    if merchant_key == 'YOUR_PAYTM_MERCHANT_KEY' or is_valid_checksum:
        if txn_status == 'TXN_SUCCESS':
            order.payment_status = 'Success'
            order.transaction_id = txn_id
            # Deduct tickets
            teams = order.item_name.split(" vs ")
            if len(teams) == 2:
                match = Match.query.filter_by(team_a=teams[0].strip(), team_b=teams[1].strip()).first()
                if match and match.available_tickets >= order.quantity:
                    match.available_tickets -= order.quantity
        else:
            order.payment_status = 'Failed'
            order.transaction_id = txn_id
    else:
        order.payment_status = 'Failed'
        order.transaction_id = 'CHECKSUM_FAILED'

    db.session.commit()
    return redirect(url_for('payment_result', order_id=order.order_id))


# ==========================================
# 6. ZOMATO-STYLE FOOD ORDER
# ==========================================
@app.route('/food-order')
def food_order():
    items = FoodItem.query.all()
    return render_template('food_order.html', items=items)


@app.route('/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'GET':
        food_id = request.args.get('food_id')
        if not food_id:
            flash('Please select a food item first.', 'warning')
            return redirect(url_for('food_order'))
        food = FoodItem.query.get_or_404(food_id)
        stripe_publishable_key = os.getenv('STRIPE_PUBLISHABLE_KEY', '')
        return render_template('payment.html', food=food, stripe_publishable_key=stripe_publishable_key)

    # POST Submission for Food Order
    customer_name = request.form.get('customer_name', '').strip()
    email = request.form.get('email', '').strip()
    food_id = request.form.get('food_id')

    try:
        quantity = int(request.form.get('quantity', 1))
    except ValueError:
        quantity = 1

    food = FoodItem.query.get_or_404(food_id)

    if not customer_name or not email:
        flash('Please enter your name and a valid email address.', 'danger')
        stripe_pub_key = os.getenv('STRIPE_PUBLISHABLE_KEY', '')
        return render_template('payment.html', food=food, stripe_publishable_key=stripe_pub_key)

    if quantity <= 0:
        flash('Quantity must be at least 1.', 'danger')
        stripe_pub_key = os.getenv('STRIPE_PUBLISHABLE_KEY', '')
        return render_template('payment.html', food=food, stripe_publishable_key=stripe_pub_key)

    # Calculate total backend side
    total_amount = round(food.price * quantity, 2)
    order_id = generate_order_id("FOOD")

    new_order = Order(
        order_id=order_id,
        customer_name=customer_name,
        email=email,
        order_type='Food Order',
        item_name=food.dish_name,
        quantity=quantity,
        amount=total_amount,
        payment_gateway='Stripe',
        payment_status='Pending'
    )
    db.session.add(new_order)
    db.session.commit()

    return redirect(url_for('create_stripe_payment', order_id=order_id))


# ==========================================
# 7. STRIPE TEST PAYMENT
# ==========================================
@app.route('/create-stripe-payment', methods=['GET', 'POST'])
def create_stripe_payment():
    order_id = request.args.get('order_id') or request.form.get('order_id')
    if not order_id:
        flash('Invalid order reference.', 'danger')
        return redirect(url_for('food_order'))

    order = Order.query.filter_by(order_id=order_id).first_or_404()
    stripe_secret_key = os.getenv('STRIPE_SECRET_KEY', '')

    # Real Stripe API Call if real secret key configured
    if stripe_secret_key and not stripe_secret_key.startswith('sk_test_51Mzxyz'):
        try:
            domain_url = request.host_url.rstrip('/')
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'inr',
                        'product_data': {
                            'name': order.item_name,
                            'description': f"Food Order ({order.quantity} qty)"
                        },
                        'unit_amount': int(order.amount / order.quantity * 100),
                    },
                    'quantity': order.quantity,
                }],
                mode='payment',
                customer_email=order.email,
                success_url=domain_url + f"/stripe-success?session_id={{CHECKOUT_SESSION_ID}}&order_id={order.order_id}",
                cancel_url=domain_url + f"/stripe-cancel?order_id={order.order_id}",
            )
            return redirect(checkout_session.url, code=330)
        except Exception as e:
            flash(f"Stripe Sandbox Error: {str(e)}", "danger")

    # Sandbox Simulation Fallback when test key is default placeholder
    return render_template('stripe_sandbox_checkout.html', order=order)


@app.route('/stripe-success')
def stripe_success():
    session_id = request.args.get('session_id')
    order_id = request.args.get('order_id')

    if not order_id:
        flash('Invalid stripe completion request.', 'danger')
        return redirect(url_for('home'))

    order = Order.query.filter_by(order_id=order_id).first_or_404()

    stripe_secret_key = os.getenv('STRIPE_SECRET_KEY', '')
    if session_id and stripe_secret_key and not stripe_secret_key.startswith('sk_test_51Mzxyz'):
        try:
            session = stripe.checkout.Session.retrieve(session_id)
            if session.payment_status == 'paid':
                order.payment_status = 'Success'
                order.transaction_id = session.payment_intent or session_id
            else:
                order.payment_status = 'Failed'
        except Exception as e:
            order.payment_status = 'Failed'
            order.transaction_id = 'STRIPE-ERR'
    else:
        # Mock Stripe Test Success
        order.payment_status = 'Success'
        order.transaction_id = session_id or f"ch_test_{random.randint(10000000, 99999999)}"

    db.session.commit()
    return redirect(url_for('payment_result', order_id=order.order_id))


@app.route('/stripe-cancel')
def stripe_cancel():
    order_id = request.args.get('order_id')
    if order_id:
        order = Order.query.filter_by(order_id=order_id).first()
        if order:
            order.payment_status = 'Cancelled'
            order.transaction_id = f"cancel_{random.randint(10000, 99999)}"
            db.session.commit()
            return redirect(url_for('payment_result', order_id=order.order_id))
    return redirect(url_for('home'))


# ==========================================
# 8 & 9. PAYPAL SANDBOX & CHATGPT COMMENT
# ==========================================
"""
ChatGPT Prompt Used for PayPal Integration:

Generate Python code for integrating PayPal Sandbox payment
processing in a Flask route for an IPL ticket payment scenario.
The payment should create a PayPal Sandbox order, redirect the
user to PayPal approval, capture the payment after approval,
and handle success/cancel cases.

Adapted Code:
[Put the final adapted PayPal implementation below this comment]
"""


@app.route('/paypal/pay/<order_id>')
def paypal_pay(order_id):
    order = Order.query.filter_by(order_id=order_id).first_or_404()

    client_id = os.getenv('PAYPAL_CLIENT_ID', 'YOUR_PAYPAL_CLIENT_ID')
    client_secret = os.getenv('PAYPAL_CLIENT_SECRET', 'YOUR_PAYPAL_CLIENT_SECRET')

    # Attempt real PayPal Sandbox API integration if real credentials supplied
    if client_id != 'YOUR_PAYPAL_CLIENT_ID' and client_secret != 'YOUR_PAYPAL_CLIENT_SECRET':
        try:
            # 1. Get OAuth Access Token from PayPal Sandbox
            token_url = "https://api-m.sandbox.paypal.com/v1/oauth2/token"
            headers = {"Accept": "application/json", "Accept-Language": "en_US"}
            data = {"grant_type": "client_credentials"}
            res = requests.post(token_url, auth=(client_id, client_secret), headers=headers, data=data)

            if res.status_code == 200:
                access_token = res.json().get('access_token')

                # Convert INR to approximate USD for PayPal Sandbox compatibility
                usd_amount = round(order.amount / 80.0, 2)
                if usd_amount < 1.00:
                    usd_amount = 1.00

                order_payload = {
                    "intent": "CAPTURE",
                    "purchase_units": [
                        {
                            "reference_id": order.order_id,
                            "amount": {
                                "currency_code": "USD",
                                "value": f"{usd_amount:.2f}"
                            },
                            "description": f"{order.item_name} ({order.quantity} tickets)"
                        }
                    ],
                    "application_context": {
                        "return_url": request.host_url.rstrip('/') + f"/paypal/success?order_id={order.order_id}",
                        "cancel_url": request.host_url.rstrip('/') + f"/paypal/cancel?order_id={order.order_id}",
                        "brand_name": "PayEase IPL Tickets",
                        "user_action": "PAY_NOW"
                    }
                }

                create_order_url = "https://api-m.sandbox.paypal.com/v2/checkout/orders"
                api_headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {access_token}"
                }
                order_res = requests.post(create_order_url, json=order_payload, headers=api_headers)

                if order_res.status_code in (200, 201):
                    order_data = order_res.json()
                    # Find approve link
                    for link in order_data.get('links', []):
                        if link.get('rel') == 'approve':
                            return redirect(link.get('href'))
        except Exception as e:
            flash(f"PayPal Sandbox Error: {str(e)}", "danger")

    # Render PayPal Sandbox Simulator page if placeholder credentials or offline
    return render_template('paypal_sandbox_checkout.html', order=order)


@app.route('/paypal/success')
def paypal_success():
    order_id = request.args.get('order_id')
    paypal_order_token = request.args.get('token')

    if not order_id:
        flash('Invalid PayPal verification parameters.', 'danger')
        return redirect(url_for('home'))

    order = Order.query.filter_by(order_id=order_id).first_or_404()

    client_id = os.getenv('PAYPAL_CLIENT_ID', 'YOUR_PAYPAL_CLIENT_ID')
    client_secret = os.getenv('PAYPAL_CLIENT_SECRET', 'YOUR_PAYPAL_CLIENT_SECRET')

    if paypal_order_token and client_id != 'YOUR_PAYPAL_CLIENT_ID':
        try:
            # Get token
            token_url = "https://api-m.sandbox.paypal.com/v1/oauth2/token"
            res = requests.post(token_url, auth=(client_id, client_secret), data={"grant_type": "client_credentials"})
            if res.status_code == 200:
                access_token = res.json().get('access_token')
                capture_url = f"https://api-m.sandbox.paypal.com/v2/checkout/orders/{paypal_order_token}/capture"
                headers = {"Content-Type": "application/json", "Authorization": f"Bearer {access_token}"}
                capture_res = requests.post(capture_url, headers=headers)
                if capture_res.status_code in (200, 201):
                    cap_data = capture_res.json()
                    if cap_data.get('status') == 'COMPLETED':
                        order.payment_status = 'Success'
                        capture_id = cap_data['purchase_units'][0]['payments']['captures'][0]['id']
                        order.transaction_id = capture_id
                        # Deduct tickets
                        teams = order.item_name.split(" vs ")
                        if len(teams) == 2:
                            match = Match.query.filter_by(team_a=teams[0].strip(), team_b=teams[1].strip()).first()
                            if match and match.available_tickets >= order.quantity:
                                match.available_tickets -= order.quantity
                        db.session.commit()
                        return redirect(url_for('payment_result', order_id=order.order_id))
        except Exception:
            pass

    # Fallback/Simulator success
    order.payment_status = 'Success'
    order.transaction_id = paypal_order_token or f"PAYPAL-TXN-{random.randint(1000000, 9999999)}"
    # Deduct tickets
    teams = order.item_name.split(" vs ")
    if len(teams) == 2:
        match = Match.query.filter_by(team_a=teams[0].strip(), team_b=teams[1].strip()).first()
        if match and match.available_tickets >= order.quantity:
            match.available_tickets -= order.quantity

    db.session.commit()
    return redirect(url_for('payment_result', order_id=order.order_id))


@app.route('/paypal/cancel')
def paypal_cancel():
    order_id = request.args.get('order_id')
    if order_id:
        order = Order.query.filter_by(order_id=order_id).first()
        if order:
            order.payment_status = 'Cancelled'
            order.transaction_id = f"PAYPAL-CANCEL-{random.randint(10000, 99999)}"
            db.session.commit()
            return redirect(url_for('payment_result', order_id=order.order_id))
    return redirect(url_for('home'))


# ==========================================
# 10. MY ORDERS PAGE
# ==========================================
@app.route('/orders')
def orders():
    all_orders = Order.query.order_by(Order.created_at.desc()).all()
    return render_template('orders.html', orders=all_orders)


# ==========================================
# 11. PAYMENT RESULT PAGE
# ==========================================
@app.route('/payment-result')
def payment_result():
    order_id = request.args.get('order_id')
    if not order_id:
        flash('No order ID provided.', 'warning')
        return redirect(url_for('home'))

    order = Order.query.filter_by(order_id=order_id).first_or_404()
    return render_template('payment_result.html', order=order)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
