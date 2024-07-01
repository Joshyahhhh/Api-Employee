from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'', include(('app1.urls', 'app1'), namespace='app1')),
    path('admin/', admin.site.urls),
]
