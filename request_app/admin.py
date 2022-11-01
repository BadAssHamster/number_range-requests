from django.contrib import admin

from request_app.models import Requests, UserTypes, Account, DocTypeNames

admin.site.register(Requests)
admin.site.register(UserTypes)
admin.site.register(Account)
admin.site.register(DocTypeNames)
