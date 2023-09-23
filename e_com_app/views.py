from django.shortcuts import render
from django.views.generic import View

from .models import Product


# Create your views here.
class HomeView(View):
    def get(self, *args, **kwargs):
        # We have to get the data from the DB, for example: products

        products = Product.objects.all().values()

        context = {
            'products': products
        }


        return render(self.request, "home.html", context)