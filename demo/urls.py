
from django.contrib import admin
from django.urls import path

from demo.views import CreateOrder

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', CreateOrder.as_view(), name="order-list"),
]
