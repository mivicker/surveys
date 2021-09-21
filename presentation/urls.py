from django.urls import path
from .views import (survey, error_and_retry, error_no_token,
                    error_attempted_resubmission, thank_you)

urlpatterns = [
    path('take/<str:uid>', survey, name='survey'),
    path('try-again/<str:uid>', error_and_retry, name='error-and-retry'),
    path('no-token', error_no_token, name='no-token'),
    path('no-resubmit', error_attempted_resubmission, name='no-resubmit'),
    path('thank-you', thank_you, name='thank-you'),
]