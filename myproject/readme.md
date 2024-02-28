Below is Directory Structure of myproject:

myproject/
|-- product_app/
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- migrations/
|   |   |-- __init__.py
|   |-- models.py
|   |-- signals.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|-- myproject/
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   |-- asgi.py
|   |-- wsgi.py
|-- manage.py
----------------------------------------------------------------
Explanation:

**Added app in settings.py**
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'product_app',   ## app added 
]

**Model (product_app/models.py):**
Created a Product model with fields title, description, price, and created_at.

**Signal (product_app/signals.py):**
Implemented a signal to automatically update the created_at field of a product whenever a new product instance is saved.

**Admin Interface (product_app/admin.py):**
Used the Django admin interface to register the Product model, allowing you to add, edit, and delete products via the admin panel.

**View (product_app/views.py):**
Created a view (ProductListView) to handle the "/products/" URL and return a JSON response with a list of dummy products.

**URL Mapping (product_app/urls.py):**
Mapped the "/products/" URL to the ProductListView.

**App Configuration (product_app/apps.py):**
Configured the app and connected the signal in the ready method.

**Project URLs (myproject/urls.py):**
Included the app's URLs in the project's URL configuration.


**Admin Superuser:**
Created a superuser using python manage.py createsuperuser to access and manage the admin interface.
To access admin interface 
username:admin
password:admin



**Commands used in this project**

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 8001    //  I am using own port not the default one


