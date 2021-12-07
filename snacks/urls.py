from django.urls import path
from .views import SnackListView, SnackDetailView, SnackCreateView, SnackUpdateView, SnackDeleteView

urlpatterns=[
    path('', SnackListView.as_view(), name= 'List_View'),
    path('<int:pk>/', SnackDetailView.as_view(), name= 'Detail_View'),
    path('create/', SnackCreateView.as_view(), name= 'Create_View'),
    path('<int:pk>/update/', SnackUpdateView.as_view(), name= 'Update_View'),
    path('<int:pk>/delete/', SnackDeleteView.as_view(), name= 'Delete_View'),

]