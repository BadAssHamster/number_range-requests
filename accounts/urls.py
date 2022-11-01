from django.contrib.auth import views
from django.urls import path, include


urlpatterns = [
    path('', include('django.contrib.auth.urls'))
]