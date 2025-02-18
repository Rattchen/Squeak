from django.urls import path
from .views import IndexView

app_name = "squeak"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]