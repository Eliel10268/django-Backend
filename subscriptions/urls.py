from django.urls import path
from .views import SubscriptionList

urlpatterns = [
    path('', SubscriptionList.as_view(), name='subscription-list'),
]
