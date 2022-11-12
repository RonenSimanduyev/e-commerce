from django.db import router
from . import views
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

router.register('category', views.CategoryView)
router.register('order', views.OrderView)
router.register('product', views.ProductView)

urlpatterns = [
    path('', include(router.urls))
]
