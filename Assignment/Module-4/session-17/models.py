from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Match(db.Model):
    __tablename__ = 'matches'
    
    id = db.Column(db.Integer, primary_key=True)
    team_a = db.Column(db.String(100), nullable=False)
    team_b = db.Column(db.String(100), nullable=False)
    venue = db.Column(db.String(200), nullable=False)
    match_date = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    available_tickets = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(500), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'team_a': self.team_a,
            'team_b': self.team_b,
            'venue': self.venue,
            'match_date': self.match_date,
            'price': self.price,
            'available_tickets': self.available_tickets,
            'image_url': self.image_url
        }

class FoodItem(db.Model):
    __tablename__ = 'food_items'
    
    id = db.Column(db.Integer, primary_key=True)
    dish_name = db.Column(db.String(100), nullable=False)
    restaurant_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(500), nullable=True)
    description = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'dish_name': self.dish_name,
            'restaurant_name': self.restaurant_name,
            'price': self.price,
            'image_url': self.image_url,
            'description': self.description
        }

class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.String(50), unique=True, nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    order_type = db.Column(db.String(50), nullable=False)  # 'IPL Ticket' / 'Food Order'
    item_name = db.Column(db.String(150), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    amount = db.Column(db.Float, nullable=False)
    payment_gateway = db.Column(db.String(50), nullable=False)  # 'Paytm' / 'Stripe' / 'PayPal'
    transaction_id = db.Column(db.String(100), nullable=True)
    payment_status = db.Column(db.String(20), nullable=False, default='Pending')  # 'Pending', 'Success', 'Failed', 'Cancelled'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'customer_name': self.customer_name,
            'email': self.email,
            'order_type': self.order_type,
            'item_name': self.item_name,
            'quantity': self.quantity,
            'amount': self.amount,
            'payment_gateway': self.payment_gateway,
            'transaction_id': self.transaction_id,
            'payment_status': self.payment_status,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S') if self.created_at else ''
        }
