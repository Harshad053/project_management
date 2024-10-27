from django.urls import path
from .views import ClientListCreateView, ClientRetrieveUpdateDestroyView, ProjectCreateView, UserAssignedProjectsView

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyView.as_view(), name='client-detail'),
    path('projects/create/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/assigned/', UserAssignedProjectsView.as_view(), name='assigned-projects'),  
]
