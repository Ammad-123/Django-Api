# myapp/views.py
from django.http import JsonResponse
from django.views import View
from .models import Product

class ProductListView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        product_list = [
            {
                'title': product.title,
                'description': product.description,
                'price': str(product.price),
                'created_at': product.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            }
            for product in products
        ]
        return JsonResponse({'products': product_list})
