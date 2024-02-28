# Django Product Management API

## Overview
This Django project implements a simple API for managing products. It covers tasks such as model creation, URL mapping, view handling, and signals for automatic updates.

## Tasks

### Task 1: Model Creation
Create a Django model named "Product" with the following fields:
- `title` (CharField, max_length=100)
- `description` (TextField)
- `price` (DecimalField, max_digits=10, decimal_places=2)
- `created_at` (DateTimeField, auto_now_add=True)

### Task 2: URL Mapping
Create a URL mapping to display a list of all products at the URL "/products/".

### Task 3: View Handling
Create a view/method to handle the URL "/products/" and return a dummy product list in the API.

### Task 4: Signals
Implement a signal that automatically updates the "created_at" field of the product whenever a new product instance is saved.

## Getting Started

### Prerequisites
- Python (3.6 or higher)
- Django (3.0 or higher)

### Installation
1. Clone the repository: `git clone https://github.com/yourusername/django-product-management-api.git`
2. Navigate to the project directory: `cd django-product-management-api`
3. Install dependencies: `pip install -r requirements.txt`

### Run the Development Server
Run the Django development server:
```bash
python manage.py runserver
