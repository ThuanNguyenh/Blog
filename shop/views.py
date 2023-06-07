from django.shortcuts import render, get_object_or_404, redirect
from .models import Shop
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

# Create your views here.

class PostListView(ListView):
    queryset = Shop.objects.all().order_by("-date")
    template_name = 'productShop.html'
    context_object_name = 'shops'
    paginate_by = 16


def productDetail(request,pk):
    shop = get_object_or_404(Shop, pk=pk)
    return render(request, 'productDetail.html', {'shop':shop})

# @login_required
# def add_to_cart(request, product_id):
#     product = Shop.objects.get(pk=product_id)
#     cart, created = Cart.objects.get_or_create(user=request.user)
#     cart.products.add(product)
#     cart.total_price += product.price
#     cart.save()
#     return redirect('productShop.html')

# def cart_detaail(request):
#     cart = Cart.objects.filter(user=request.user).first()
#     return render(request, 'cart.html', {'cart': cart})