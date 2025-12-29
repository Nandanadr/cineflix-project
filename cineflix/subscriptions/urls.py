from django.urls import path 

from  . import views

urlpatterns = [

    path('subscription-list/',views.SubscriptionsView.as_view(),name='subscription-list'),

    path('subscription-create/',views.SubscriptionsCreateView.as_view(),name='subscription-create'),
    
]