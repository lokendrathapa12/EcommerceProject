from django.contrib import admin
from django.urls import path
from vendor import views
app_name = 'vendor'
urlpatterns = [
    path("",views.VendorHomeView.as_view(),name='vendorhomepage'),
    path('selectitem/',views.SlectProductView,name = 'selectitempage'),
]