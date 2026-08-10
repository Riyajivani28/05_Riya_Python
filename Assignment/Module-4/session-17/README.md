# PayEase - Dynamic Flask Payment Gateway Application

PayEase is a dynamic, real-world web application built with **Flask**, **SQLite**, **SQLAlchemy**, and **Bootstrap 5** that demonstrates sandbox payment gateway integrations for:
1. **IPL Ticket Booking System** (Paytm Sandbox & PayPal Sandbox)
2. **Zomato-Style Food Ordering System** (Stripe Test Mode)

> **IMPORTANT:** This application operates strictly in **TEST / SANDBOX MODE**. No real monetary transactions take place.

---

## 🚀 Features

- 🎟️ **Dynamic IPL Ticket Booking**: Select matches, choose ticket quantities, see total prices dynamically updated via JS, and pay with Paytm Sandbox or PayPal Sandbox.
- 🍔 **Zomato-Style Food Delivery Checkout**: Pick food items, customize dish quantities, recalculate totals, and checkout with Stripe Test Mode.
- 📊 **Dynamic Order Management**: Store all orders in a local SQLite database (`database.db`). View real-world order history, payment gateways, status badges (`Success`, `Pending`, `Failed`, `Cancelled`), and transaction IDs.
- 🔐 **Backend Security & Amount Verification**: Order totals are dynamically computed on the backend server to prevent tampered frontend requests. Secret keys are kept in `.env`.
- ⚡ **Automated Checksum & Signature Verification**: Paytm HMAC/AES checksum generation and verification, PayPal OAuth token + Capture verification, and Stripe Session validation.

---

## 🛠️ Tech Stack & Requirements

- **Backend**: Python 3.11+, Flask, Flask-SQLAlchemy, PyCryptodome (Paytm Checksum), Requests
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript (Vanilla JS for dynamic calculations)
- **Database**: SQLite3 (`database.db`)
- **Payment Gateways (Sandbox/Test Only)**:
  - Paytm Staging API
  - Stripe Test Mode API
  - PayPal v2 REST Sandbox API

---

## 📋 Installation & Setup Guide

Follow these exact steps in your terminal (VS Code / Command Prompt):

### 1. Navigate to Project Directory
```bash
cd e:\Python\Assignment\Module-4\session-17
```

### 2. Create & Activate Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows PowerShell / Command Prompt)
venv\Scripts\activate

# (If on Linux/macOS, run: source venv/bin/activate)
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables Configuration (`.env`)

Create or edit the `.env` file in the project root directory with your sandbox credentials:

```env
FLASK_SECRET_KEY=payease_secret_key_super_secret_2026

# Paytm Sandbox Credentials
PAYTM_MID=YOUR_PAYTM_MID
PAYTM_MERCHANT_KEY=YOUR_PAYTM_MERCHANT_KEY
PAYTM_WEBSITE=WEBSTAGING
PAYTM_CHANNEL_ID=WEB
PAYTM_INDUSTRY_TYPE_ID=Retail
PAYTM_CALLBACK_URL=http://localhost:5000/payment-callback

# Stripe Test Credentials
STRIPE_SECRET_KEY=sk_test_51...
STRIPE_PUBLISHABLE_KEY=pk_test_51...

# PayPal Sandbox Credentials
PAYPAL_CLIENT_ID=YOUR_PAYPAL_CLIENT_ID
PAYPAL_CLIENT_SECRET=YOUR_PAYPAL_CLIENT_SECRET
PAYPAL_MODE=sandbox
```

---

## 🏦 Payment Gateway Setup Instructions

### A. Paytm Sandbox Setup
1. Log in to [Paytm Developer Dashboard](https://dashboard.paytm.com/next/apikeys).
2. Switch to **Test Account / Staging Credentials**.
3. Copy `MID` and `Merchant Key` into `.env`.
4. The callback URL will receive signature parameters, verify checksum using `paytm_checksum.py`, and update the SQLite database order status.

### B. Stripe Test Setup
1. Log in to [Stripe Dashboard](https://dashboard.stripe.com/test/dashboard).
2. Ensure **Test Mode** toggle is ON.
3. Copy **Secret Key** (`sk_test_...`) and **Publishable Key** (`pk_test_...`) into `.env`.
4. Test cards: Use `4242 4242 4242 4242` with any future expiry date and 3-digit CVC.

### C. PayPal Sandbox Setup
1. Log in to [PayPal Developer Portal](https://developer.paypal.com/dashboard/applications/sandbox).
2. Create a **Sandbox App**.
3. Copy the **Client ID** and **Secret** into `.env`.
4. The app uses PayPal's `/v2/checkout/orders` REST API to get approval links and capture payments.

---

## 🗄️ Database Setup & Running the App

Database tables (`matches`, `food_items`, `orders`) and initial sample match/food data are generated automatically on startup!

Run the Flask application:
```bash
python app.py
```

Open your browser and navigate to:
`http://localhost:5000` or `http://127.0.0.1:5000`

---

## 🔄 Complete Application Flow

1. **IPL Tickets Flow**:
   - Go to **IPL Tickets** (`/tickets`).
   - Select match -> Click **Book Tickets Now** (`/pay`).
   - Enter Customer Name, Email, and Quantity.
   - Choose **Paytm Sandbox** or **PayPal Sandbox**.
   - Complete test transaction -> Redirected to `/payment-result`.
   - Ticket availability count dynamically decrements in SQLite DB!

2. **Food Order Flow**:
   - Go to **Food Order** (`/food-order`).
   - Select dish -> Click **Order Now** (`/payment`).
   - Enter Name, Email, and Quantity.
   - Click **Pay with Stripe Checkout**.
   - Complete test payment -> Redirected to `/payment-result`.

3. **My Orders**:
   - Go to **My Orders** (`/orders`) to view all historical orders dynamically loaded from `database.db`.

---

## 🔒 Security Best Practices

- ❌ **Never expose secret keys** in frontend HTML or JavaScript.
- 🔒 **Backend Amount Calculation**: Order total amount is always computed on Flask backend (`amount = price * quantity`) to prevent client-side parameter tampering.
- 📜 **Signature Verification**: Paytm callback signature checksums and PayPal capture statuses are verified before updating orders to `Success`.
- 📁 `.env` is added to `.gitignore` to prevent committing sensitive keys.
