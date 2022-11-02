from django.urls import path
from .views import *

urlpatterns = [
    path('form/', request_form, name='form'),
    path('', request_list, name='request_table'),
    path('miac-submit-form/<pk>', miac_submit_request, name='submit_form'),
    path('mo_delete_button/<pk>', mo_delete_button, name='mo_delete_button'),
    path('mo_submit_button/<pk>', mo_submit_button, name='mo_submit_button'),
    path('mo_update_button/<pk>', mo_update_button, name='alter_form'),

]