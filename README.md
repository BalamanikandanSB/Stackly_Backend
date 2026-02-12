# Stackly Backend Project

## Project Overview
Stackly Backend is a Django REST Framework based backend application built to manage products and orders efficiently. This project demonstrates RESTful APIs, JWT authentication, and proper project structuring.

## Folder Structure

stackly_backend/
├── core/
│ ├── models.py
│ ├── serializers.py
│ └── views.py
├── stackly_backend/
│ ├── settings.py
│ └── urls.py
├── manage.py
├── venv/ # virtual environment (excluded from git)
└── README.md # this file

## Requirements
- Python 3.x
- Django 4.x
- Django REST Framework
- drf-yasg (Swagger/OpenAPI docs)

## Setup Instructions

1. **Clone the repo**  
```bash
git clone <your_repo_url>
cd stackly_backend

2. Create virtual environment

python -m venv venv


3. Activate virtual environment

Windows PowerShell:

.\venv\Scripts\Activate.ps1


CMD:

.\venv\Scripts\activate.bat


4. Install dependencies

pip install -r requirements.txt


5. Apply migrations

python manage.py makemigrations
python manage.py migrate


6. Create superuser

python manage.py createsuperuser


7. Run server

python manage.py runserver

API Endpoints
Method	Endpoint	Description	Authentication
GET	/api/products/	List all products	Optional
POST	/api/products/	Create a new product	Required
GET	/api/orders/	List all orders	Required
POST	/api/orders/	Create a new order	Required
PUT	/api/orders/<id>/	Update entire order	Required
PATCH	/api/orders/<id>/	Update partial order	Required
DELETE	/api/orders/<id>/	Delete order	Required

Sample JSON for Product POST

{
  "name": "Laptop",
  "description": "High-end laptop",
  "price": 1200.50,
  "stock": 10
}


Sample JSON for Order POST

{
  "user": 1,
  "products": [1, 2]
}

Authentication

JWT authentication is implemented.

Pass token in Authorization header as:

Authorization: Bearer <your_token_here>

Professional Notes / Working Process

Built backend with proper modular structure (core, stackly_backend settings)

Implemented serializers for clean API responses

Followed best practices for migrations and virtual environments

Progress documented in README.md

Swagger documentation included at /swagger/

How to Submit

1. Push project to public GitHub repository

2. Ensure README.md includes setup, run instructions, API endpoints, authentication info

3. Share repository link via email as submission


---

### ✅ **Step 3: Paste & Save**
- Open your `README.md` file.
- **Delete any placeholder content**.
- **Copy the above full content** and paste.
- **Save the file**.

---

### **Step 4: Push to GitHub**
1. Open terminal in project root (`stackly_backend`)
2. Run:

```bash
git add README.md
git commit -m "Add full professional README.md with setup, API, instructions"
git push origin main