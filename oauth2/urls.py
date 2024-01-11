from django.contrib import admin
from django.urls import path, include
from oauth2app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/', helloWorld, name='api'),
]
