from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blogs/<int:pk>/', views.BlogRetrieveUpdateDestroyAPIView.as_view(), name='update'),
]