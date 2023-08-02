from django.contrib import admin
from django.urls import path, include

from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('extracurricular.urls')),
    path('accounts/', include('accounts.urls')),
]
