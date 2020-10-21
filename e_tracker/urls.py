from django.urls import path

from e_tracker import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('create/', views.create_expense, name='create expense'),
    path('edit/<int:pk>/', views.edit_expense, name='edit expense'),
    path('delete/<int:pk>/', views.delete_expense, name='delete expense'),
    path('profile/', views.profile_page, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile edit'),
    path('profile/delete/', views.profile_delete, name='profile delete'),

]
