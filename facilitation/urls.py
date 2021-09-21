from django.urls import path
from .views import upload_csv, error_page

urlpatterns = [
    path('', upload_csv, name='upload-csv'),
    path('error', error_page, name='upload-error'),
]