from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('items', views.MenuItemsView.as_view()),
    path('items/<int:pk>', views.SingleMenuItemView.as_view()),


    # URLS for static HTML
    path('home', views.homepage, name='home'),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    # # Add the remaining URL path configurations here
    path('menuitems/', views.menu, name="menu"),
    path('menuitems/<int:pk>/', views.display_menu_item, name="menu_item"),
]
