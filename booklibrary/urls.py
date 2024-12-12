from django.urls import path

from . import views

urlpatterns = [
  path("", views.index, name="index"),

  # GENRES
  path('genres/manage/', views.manage_genres, name='manage_genres'),
  path('genres/add/', views.add_genre, name='add_genre'),
  path('genres/edit/<int:id>/', views.edit_genre, name='edit_genre'),
  path('genres/delete/<int:id>/', views.delete_genre, name='delete_genre'),
  
  # NATIONALITIES
  path('nationalities/manage/', views.manage_nationalities, name='manage_nationalities'),
  path('nationalities/add/', views.add_nationality, name='add_nationality'),
  path('nationalities/edit/<int:id>/', views.edit_nationality, name='edit_nationality'),
  path('nationalities/delete/<int:id>/', views.delete_nationality, name='delete_nationality'),

  # AUTHORS
  path('authors/manage/', views.manage_authors, name='manage_authors'),
  path('authors/add/', views.add_author, name='add_author'),
  path('authors/edit/<int:id>/', views.edit_author, name='edit_author'),
  path('authors/delete/<int:id>/', views.delete_author, name='delete_author'),

  # BOOKS
  path('books/manage/', views.manage_books, name='manage_books'),
  path('books/add/', views.add_book, name='add_book'),
  path('books/edit/<str:isbn>/', views.edit_book, name='edit_book'),
  path('books/delete/<str:isbn>/', views.delete_book, name='delete_book'),

  # REPORTS
  path('reports/books/', views.reports_books, name='reports_books'),

]