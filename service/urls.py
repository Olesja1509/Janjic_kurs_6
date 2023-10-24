from django.urls import path
from django.views.decorators.cache import cache_page

from service.apps import ServiceConfig
from service.views import MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView, \
    ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView

app_name = ServiceConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='index'),
    path('view/<int:pk>/', MailingDetailView.as_view(), name='mailing'),
    path('create/', MailingCreateView.as_view(), name='create_mailing'),
    path('update/<int:pk>', MailingUpdateView.as_view(), name='update_mailing'),
    path('delete/<int:pk>', MailingDeleteView.as_view(), name='delete_mailing'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('client/view/<int:pk>/', cache_page(60)(ClientDetailView.as_view()), name='client'),
    path('client/create/', ClientCreateView.as_view(), name='create_client'),
    path('client/update/<int:pk>', ClientUpdateView.as_view(), name='update_client'),
    path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='delete_client'),
]
