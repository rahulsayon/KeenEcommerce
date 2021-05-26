from django.urls import path
from .views import ProductView,DemoView

urlpatterns = [
    path('', ProductView.as_view() ),
    path('auth/' , DemoView.as_view())
]
