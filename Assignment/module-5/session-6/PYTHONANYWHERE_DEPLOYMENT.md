# PythonAnywhere Deployment Guide for Django REST API

This guide provides step-by-step instructions for deploying this Django REST Framework API to **PythonAnywhere**.

---

## 1. Create & Log into PythonAnywhere Account
1. Sign up or log into your account at [PythonAnywhere](https://www.pythonanywhere.com/).
2. Open a **Bash Console** from your PythonAnywhere Dashboard.

---

## 2. Upload / Clone the Code
In the PythonAnywhere Bash console, clone or upload your project files:
```bash
git clone <YOUR_REPOSITORY_URL> session-6
cd session-6
```

---

## 3. Set Up Virtual Environment & Dependencies
1. Create a virtual environment with Python 3.11/3.10:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.11 myenv
   ```
2. Install the required Python packages:
   ```bash
   pip install django djangorestframework djangorestframework-simplejwt django-allauth requests twilio stripe python-dotenv
   ```

---

## 4. Configure Environment Variables (`.env`)
Create a `.env` file inside your project directory `/home/<username>/session-6/.env`:
```env
MAILGUN_API_KEY=key-your-mailgun-api-key
MAILGUN_DOMAIN=sandbox-your-domain.mailgun.org
MAILGUN_SENDER=postmaster@sandbox-your-domain.mailgun.org

TWILIO_ACCOUNT_SID=AC_your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=+1234567890

STRIPE_SECRET_KEY=sk_test_your_stripe_secret_key

GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
```

---

## 5. Run Database Migrations
Inside your virtualenv and project folder, run:
```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

---

## 6. Configure the Web App on PythonAnywhere
1. Go to the **Web** tab in the PythonAnywhere Dashboard.
2. Click **Add a new web app**.
3. Select **Manual configuration** and choose **Python 3.11** (or matching version).
4. Set **Virtualenv path**: `/home/<username>/.virtualenvs/myenv`.
5. Set **Source code path**: `/home/<username>/session-6`.
6. Edit the **WSGI configuration file** (click the WSGI link) and set its content to:

```python
import os
import sys

path = '/home/<username>/session-6'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'foodiehub.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

7. Click **Reload <username>.pythonanywhere.com**.

---

## 7. Postman Verification
Once deployed, send a `POST` request to `https://<username>.pythonanywhere.com/api/send-email/`:

- **URL**: `https://<username>.pythonanywhere.com/api/send-email/`
- **Method**: `POST`
- **Header**: `Content-Type: application/json`
- **Body**:
  ```json
  {
      "email": "user@example.com"
  }
  ```
- **Response (200 OK)**:
  ```json
  {
      "status": "success",
      "message": "Welcome email sent successfully",
      "mailgun_response": {
          "id": "<202608171254.123456@sandbox.mailgun.org>",
          "message": "Queued. Thank you."
      }
  }
  ```
