from django.urls import path
from .views import ClientList, DeleteClient, ChangeClient, CreateClient
from .view_ajax import (ClientListAjax, ViewClient)


urlpatterns = [
    path('', ClientList.as_view(), name="client_list"),

    # ajax views and actions
    path('create/', CreateClient.as_view(), name='crud_ajax_create'),
    path('delete/<int:id>/',  DeleteClient.as_view(), name='crud_ajax_delete'),
    path('update/<int:id>/', ChangeClient.as_view(), name='crud_ajax_update'),

    # ajax views
    path('list_client/',  ClientListAjax.as_view(), name='crud_ajax_list'),
    path('view_client/<int:id>/',  ViewClient.as_view(), name='view_client'),
]