from rest_framework import routers
from django.urls import path, include, re_path
from .views import *

# Создаем router и регистрируем наш ViewSet
router = routers.SimpleRouter()

router.register(r'product', ProductViewSet)

# URLs настраиваются автоматически роутером
urlpatterns = [
    path("", include(router.urls)),

]