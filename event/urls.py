from django.urls import path
from .views import EventListCreate, EventDetail, RegistrationListCreate

urlpatterns = [
    path('events/', EventListCreate.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventDetail.as_view(), name='event-detail'),
    path('registrations/', RegistrationListCreate.as_view(), name='registration-list-create'),
]