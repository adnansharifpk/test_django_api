from django.urls import path
from .views import LoginView, LogoutView, ProductListView, UpdateProductSelectionView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('products/', ProductListView.as_view()),
    path('product/select/<int:product_id>/', UpdateProductSelectionView.as_view(), name='update-product-selection'),
]
