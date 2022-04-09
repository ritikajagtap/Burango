from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]
admin.site.site_header = "Burango Burgers Admin"
admin.site.site_title = "Burango Burgers Admin Portal"
admin.site.index_title = "Welcome to Burango burgers Portal"