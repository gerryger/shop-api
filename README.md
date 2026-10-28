# Shop API

REST API for an e-commerce app, built with Django and Django REST Framework. This is an early prototype.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed            # sample products
python manage.py createsuperuser # optional, for /admin/
python manage.py runserver
```

Open http://127.0.0.1:8000/api/ to browse the API.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| POST | `/api/auth/register/` | Create an account |
| POST | `/api/auth/token/` | Get an auth token (`username`, `password`) |
| GET | `/api/auth/me/` | Current user |
| GET, POST | `/api/categories/` | List / create categories |
| GET, POST | `/api/products/` | List / create products (`?search=`, `?category=<slug>`) |
| GET, PUT, PATCH, DELETE | `/api/products/{id}/` | Product detail |
| GET, POST | `/api/orders/` | List / create orders |
| GET | `/api/orders/{id}/` | Order detail |
| POST | `/api/orders/{id}/pay/` | Pay for an order |
| POST | `/api/orders/{id}/cancel/` | Cancel an order |

Send the token as `Authorization: Token <token>`.

### Example: place an order

```bash
curl -X POST http://127.0.0.1:8000/api/orders/ \
  -H "Authorization: Token <token>" \
  -H "Content-Type: application/json" \
  -d '{"shipping_address": "Jl. Sudirman No. 1, Jakarta",
       "items": [{"product": 1, "quantity": 2, "price": 499000}]}'
```

## Tests

```bash
python manage.py test
```

## Your task

We want to launch this API to real customers. Review the codebase and get it as close to production-ready as you can in the time available. You may use any AI tools you normally use.

Talk us through:

1. What you would change before going live, and in what order.
2. How you are using AI to find and fix issues, and how you check its output.
3. What you would not trust the AI to decide on its own.
