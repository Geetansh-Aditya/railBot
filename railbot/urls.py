
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/', include('client.urls')),
    path('employee/', include('employee.urls')),
]
