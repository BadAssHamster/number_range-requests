from django.urls import path
from .views import *

urlpatterns = [
    path('form/', request_form, name='form'),
    path('', request_list, name='request_table'),
    path('mo-alter-form/', mo_alter_request, name='alter_form'),
    path('miac-submit-form/', miac_submit_request, name='submit_form'),

]