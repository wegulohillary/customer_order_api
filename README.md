# Customer Order API

**Customer Order API** is a backend service built with Django and Django REST Framework that allows you to manage customers and their orders. It supports:

- RESTful API endpoints  
- PostgreSQL database  
- Authentication and authorization using OpenID Connect (OIDC)  
- SMS alerts via Africa’s Talking  
- CI/CD using GitHub Actions  
- Docker & Docker Compose  
- Deployment to Heroku  

---

## Features

- **Customer Management**: Add, list, update, and delete customers  
- **Order Management**: Create and track customer orders  
- **SMS Alerts**: Customers receive an SMS when an order is created  
- **RESTful API**: Built using Django REST Framework  
- **Swagger Docs**: Available at `/swagger/`  
- **CI/CD**: Automated testing and deployment  
- **Deployment**: Easily deployable via Heroku and Docker  

---

## Tech Stack

- Python 3.10  
- Django 4.x  
- PostgreSQL  
- Docker & Docker Compose  
- Africa’s Talking (SMS Gateway)  
- GitHub Actions (CI/CD)  
- Heroku (Hosting)  

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/wegulohillary/customer-order-api.git
cd customer-order-api
```

---

### 2. Create and Configure `.env` File

```bash
cp .env.sample .env
```

Then edit `.env`:

```env
DEBUG=True
SECRET_KEY=your-secret-key
DB_NAME=orders_db
DB_USER=orders_user
DB_PASSWORD=securepassword
DB_HOST=localhost
DB_PORT=5432
AT_USERNAME=sandbox
AT_API_KEY=your_africas_talking_sandbox_key
```

---

### 3. Set Up PostgreSQL Database

**Option 1: Using Docker (Recommended)**

```bash
docker-compose up --build
```

**Option 2: Manually on Linux**

```bash
sudo -u postgres psql

CREATE DATABASE orders_db;
CREATE USER orders_user WITH PASSWORD 'securepassword';
ALTER ROLE orders_user SET client_encoding TO 'utf8';
ALTER ROLE orders_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE orders_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE orders_db TO orders_user;
```

---

### 4. Migrate and Start Server

```bash
python manage.py migrate
python manage.py runserver
```

Visit:

- API root: [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)  
- Swagger docs: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)  

---

## Running with Docker

```bash
docker-compose up --build
```

Your API will be available at [http://localhost:8000](http://localhost:8000)

---

## Authentication with OpenID Connect (OIDC)

1. Register your app with an OIDC provider (e.g., Google, Auth0, Keycloak).
2. Install OIDC package:

```bash
pip install mozilla-django-oidc
```

3. Add the following to `settings.py`:

```python
INSTALLED_APPS += ['mozilla_django_oidc']

AUTHENTICATION_BACKENDS = (
    'mozilla_django_oidc.auth.OIDCAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)

OIDC_RP_CLIENT_ID = 'your-client-id'
OIDC_RP_CLIENT_SECRET = 'your-client-secret'
OIDC_OP_AUTHORIZATION_ENDPOINT = 'https://example.com/auth'
OIDC_OP_TOKEN_ENDPOINT = 'https://example.com/token'
OIDC_OP_USER_ENDPOINT = 'https://example.com/userinfo'
LOGIN_URL = '/oidc/authenticate/'
LOGIN_REDIRECT_URL = '/'
```

4. Protect views using `@login_required` or middleware.

---

## SMS Alerts via Africa’s Talking

1. Sign up at [Africa’s Talking](https://africastalking.com)  
2. Get your **sandbox** username and API key  
3. Add them to your `.env`:

```env
AT_USERNAME=sandbox
AT_API_KEY=your_api_key
```

4. SMS is triggered in `OrderViewSet.perform_create()` when a new order is saved.

---

## API Endpoints

### Customers

- `GET /api/customers/` — List all customers  
- `POST /api/customers/` — Create a new customer  
- `GET /api/customers/{id}/` — Retrieve a customer  
- `PUT /api/customers/{id}/` — Update a customer  
- `DELETE /api/customers/{id}/` — Delete a customer  

### Orders

- `GET /api/orders/` — List all orders  
- `POST /api/orders/` — Create a new order  
- `GET /api/orders/{id}/` — Retrieve an order  

---

## Running Tests

```bash
pytest
```

To check code coverage:

```bash
coverage run -m pytest
coverage report -m
```

---

## GitHub Actions - CI/CD

GitHub Actions is configured via `.github/workflows/ci.yml`:

- Runs on every push or pull request  
- Uses PostgreSQL service  
- Installs dependencies and runs tests  

---

## Deploying to Heroku

1. Create Heroku App:

```bash
heroku create customer-order-api
```

2. Add PostgreSQL Addon:

```bash
heroku addons:create heroku-postgresql:hobby-dev
```

3. Push Your Code:

```bash
git push heroku main
```

4. Set Heroku Environment Variables:

```bash
heroku config:set SECRET_KEY='your-secret-key'
heroku config:set AT_USERNAME='sandbox'
heroku config:set AT_API_KEY='your_api_key'
```

5. Run Migrations:

```bash
heroku run python manage.py migrate
```

---

## Contributor

**Okumu Hillary**  
Email: [wegulohillary@gmail.com](mailto:wegulohillary@gmail.com)  
Role: Backend Developer  

---

## License

MIT License
