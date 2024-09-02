from django.urls import path
from .views import ClientListCreateView, ClientRetrieveUpdateDeleteView, ProjectCreateView, UserProjectListView

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDeleteView.as_view(), name='client-detail'),
    path('projects/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/assigned/', UserProjectListView.as_view(), name='user-project-list'),
]
