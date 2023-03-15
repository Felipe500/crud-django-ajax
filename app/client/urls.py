from django.urls import path
from .views import ClientList
from .view_ajax import (ClientListAjax, DeleteClient, UpdateClient, CreateClient,
                        ViewClient, ViewCreateClient, ViewDeleteClient, ViewUpdateClient)


urlpatterns = [
    path('', ClientList.as_view(), name="client_list"),

    # ajax actions
    path('create/', CreateClient.as_view(), name='crud_ajax_create'),
    path('delete/<int:id>/',  DeleteClient.as_view(), name='crud_ajax_delete'),
    path('update/<int:id>/', UpdateClient.as_view(), name='crud_ajax_update'),
    path('list_client/',  ClientListAjax.as_view(), name='crud_ajax_list'),
    # ajax get views
    path('view_create_client/',  ViewCreateClient.as_view(), name='create_view_client'),
    path('view_client/<int:id>/',  ViewClient.as_view(), name='view_client'),
    path('view_update_client/<int:id>/',  ViewUpdateClient.as_view(), name='update_view_client'),
    path('view_delete_client/<int:id>/',  ViewDeleteClient.as_view(), name='delete_view_client1'),

]