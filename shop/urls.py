from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='shop'),
    path("<int:pk>/", views.productDetail, name='shopDetail'),
    # path('cart/add/<int:shop_id>/', views.add_to_cart, name='add_to_cart')
]