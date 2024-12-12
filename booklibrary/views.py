from django.contrib import messages
from .models import Book, Genre, Nationality, Author
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import Count
from django.db import connection

def index(request):
  return redirect(reverse('reports_books'))

def manage_genres(request):
  genres = Genre.objects.all().order_by('name')
  return render(request, 'genres/manage_genres.html', {'genres' : genres})

def add_genre(request):
  
  # if form submitted
  if request.method == 'POST':

    # get input
    name = request.POST.get('name')
    
    # validate input (mustn't be empty)
    if not name:
      messages.error(request,'Fields cannot be left empty!', extra_tags='danger')
      return redirect(reverse('add_genre'))
    
    name = name.strip()
    
    # if genre exists, go back to add genre page with error message
    if Genre.objects.filter(name=name):
      messages.error(request,'Genre already exists!', extra_tags='danger')
      return redirect(reverse('add_genre'))
    
    # otherwise, create genre and go to add genre page with success message
    else:
      genre = Genre(name=name)
      genre.save()
      messages.success(request, 'Genre created successfully.', extra_tags='info')
      return redirect(reverse('add_genre'))
    
  return render(request, 'genres/add_genre.html')

def edit_genre(request, id):

  genre = get_object_or_404(Genre, id=id)

  # if form submitted
  if request.method == 'POST':

    # get input
    name = request.POST.get('name')
    
    # validate input (mustn't be empty)
    if not name:
      messages.error(request,'Fields cannot be left empty!', extra_tags='danger')
      return redirect(reverse('edit_genre', args=[genre.id]))
    
    name = name.strip()
    
    # if genre exists, go back to edit genre page with error message
    if Genre.objects.filter(name=name):
      messages.error(request,'Genre already exists!', extra_tags='danger')
      return redirect(reverse('edit_genre', args=[genre.id]))
    
    # otherwise, create genre and go to edit genre page with success message
    else:
      genre.name = name 
      genre.save()
      messages.success(request, 'Genre updated successfully.', extra_tags='info')
      return redirect(reverse('edit_genre', args=[genre.id]))
  else:
    return render(request, 'genres/edit_genre.html', {'genre': genre})

def delete_genre(request, id):
  genre = get_object_or_404(Genre, id=id)
  if genre:
    genre.delete()
    messages.success(request, 'Genre deleted succesfully.', extra_tags='info')
    return redirect(reverse('manage_genres'))
  
def manage_nationalities(request):
  nationalities = Nationality.objects.all().order_by('name')
  return render(request, 'nationalities/manage_nationalities.html', {'nationalities' : nationalities})

def add_nationality(request):
  
  # if form submitted
  if request.method == 'POST':

    # get input
    name = request.POST.get('name')
    
    # validate input (mustn't be empty)
    if not name:
      messages.error(request,'Fields cannot be left empty!', extra_tags='danger')
      return redirect(reverse('add_nationality'))
    
    name = name.strip()
    
    # if nationality exists, go back to add nationality page with error message
    if Nationality.objects.filter(name=name):
      messages.error(request,'Nationality already exists!', extra_tags='danger')
      return redirect(reverse('add_nationality'))
    
    # otherwise, create nationality and go to add nationality page with success message
    else:
      nationality = Nationality(name=name)
      nationality.save()
      messages.success(request, 'Nationality created successfully.', extra_tags='info')
      return redirect(reverse('add_nationality'))
    
  return render(request, 'nationalities/add_nationality.html')

def edit_nationality(request, id):

  nationality = get_object_or_404(Nationality, id=id)

  # if form submitted
  if request.method == 'POST':

    # get input
    name = request.POST.get('name')
    
    # validate input (mustn't be empty)
    if not name:
      messages.error(request,'Fields cannot be left empty!', extra_tags='danger')
      return redirect(reverse('edit_nationality', args=[nationality.id]))
    
    name = name.strip()
    
    # if nationality exists, go back to edit nationality page with error message
    if Nationality.objects.filter(name=name):
      messages.error(request,'Nationality already exists!', extra_tags='danger')
      return redirect(reverse('edit_nationality', args=[nationality.id]))
    
    # otherwise, create nationality and go to edit nationality page with success message
    else:
      nationality.name = name 
      nationality.save()
      messages.success(request, 'Nationality updated successfully.', extra_tags='info')
      return redirect(reverse('edit_nationality', args=[nationality.id]))
  else:
    return render(request, 'nationalities/edit_nationality.html', {'nationality': nationality})

def delete_nationality(request, id):
  nationality = get_object_or_404(Nationality, id=id)
  if nationality:
    nationality.delete()
    messages.success(request, 'Nationality deleted succesfully.', extra_tags='info')
    return redirect(reverse('manage_nationalities'))
  
def manage_authors(request):
  authors = Author.objects.all()
  return render(request, 'authors/manage_authors.html', {'authors' : authors})

def add_author(request):
  
   # if form submitted
  if request.method == 'POST':

    # get input
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    nationality = request.POST.get('nationality')

    try:
      nationality = Nationality.objects.get(id=nationality)
    except:
      nationality = None

    # validate input (mustn't be empty)
    if not first_name or not last_name or not nationality:
      messages.error(request,'Fields cannot be left empty!', extra_tags='danger')
      return redirect(reverse('add_author'))
    
    first_name = first_name.strip()
    last_name = last_name.strip()
    
    # if author already exists, go back to add author page with error message
    if Author.objects.filter(first_name=first_name, last_name=last_name, nationality=nationality):
      messages.error(request,'Author already exists!', extra_tags='danger')
      return redirect(reverse('add_author'))
    
    # otherwise, create author and go to add author page with success message
    else:
      author = Author(first_name=first_name, last_name=last_name, nationality=nationality)
      author.save()
      messages.success(request, 'Author created successfully.', extra_tags='info')
      return redirect(reverse('add_author'))
  
  nationalities = Nationality.objects.all().order_by('name')
  return render(request, 'authors/add_author.html', {'nationalities': nationalities})

def edit_author(request, id):
  
  author = get_object_or_404(Author, id=id)

  # if form submitted
  if request.method == 'POST':

    # get input
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    nationality = request.POST.get('nationality')

    try:
      nationality = Nationality.objects.get(id=nationality)
    except:
      nationality = None

    # validate input (mustn't be empty)
    if not first_name or not last_name or not nationality:
      messages.error(request,'Fields cannot be left empty!', extra_tags='danger')
      return redirect(reverse('edit_author', args=[author.id]))

    first_name = first_name.strip()
    last_name = last_name.strip()

    # if author exists, go back to edit author page with error message
    if Author.objects.filter(first_name=first_name, last_name=last_name, nationality=nationality):
      messages.error(request,'Author already exists!', extra_tags='danger')
      return redirect(reverse('edit_author', args=[author.id]))
    else:
      author.first_name = first_name 
      author.last_name = last_name 
      author.nationality = nationality 
      author.save()
      
      messages.success(request, 'Author updated successfully.', extra_tags='info')
      return redirect(reverse('edit_author', args=[author.id]))
  else:
    nationalities = Nationality.objects.all().order_by('name')
    return render(request, 'authors/edit_author.html', {'author': author, 'nationalities': nationalities})

def delete_author(request, id):
  author = get_object_or_404(Author, id=id)
  if author:
    author.delete()
    messages.success(request, 'Author deleted succesfully.', extra_tags='info')
    return redirect(reverse('manage_authors'))

def manage_books(request):
  books = Book.objects.all().order_by('title')
  return render(request, 'books/manage_books.html', {'books': books})

def add_book(request):
  
   # if form submitted
  if request.method == 'POST':

    # get input
    isbn = request.POST.get('isbn')
    if len(isbn) != 13:
      messages.error(request,'Invalid ISBN!', extra_tags='danger')
      return redirect(reverse('add_book'))
    
    title = request.POST.get('title')
    genre = request.POST.get('genre')
    author = request.POST.get('author')
    publication_year = request.POST.get('publication_year')
    page_count = request.POST.get('page_count')

    try:
      genre = Genre.objects.get(id=genre)
    except:
      genre = None
    
    try:
      author = Author.objects.get(id=author)
    except:
      author = None

    # validate input (mustn't be empty)
    if not isbn or not title or not genre or not author or not publication_year:
      messages.error(request,'Fields cannot be left empty!', extra_tags='danger')
      return redirect(reverse('add_book'))
    
    isbn = isbn.strip()
    title = title.strip()

    # if book already exists, go back to add author page with error message
    if Book.objects.filter(isbn=isbn):
      messages.error(request,'Book already exists!', extra_tags='danger')
      return redirect(reverse('add_book'))
    
    # otherwise, create author and go to add author page with success message
    else:
      book = Book(isbn=isbn, title=title, genre=genre, author=author, publication_year=publication_year, page_count=page_count)
      book.save()
      messages.success(request, 'Book created successfully.', extra_tags='info')
      return redirect(reverse('add_book'))
  
  genres = Genre.objects.all().order_by('name')
  authors = Author.objects.all().order_by('first_name', 'last_name')
  return render(request, 'books/add_book.html', {'genres': genres, 'authors': authors})

def edit_book(request, isbn):
  book = get_object_or_404(Book, isbn=isbn)

  # if form submitted
  if request.method == 'POST':

    # get input
    title = request.POST.get('title')
    genre = request.POST.get('genre')
    author = request.POST.get('author')
    publication_year = request.POST.get('publication_year')
    page_count = request.POST.get('page_count')

    try:
      genre = Genre.objects.get(id=genre)
    except:
      genre = None
    
    try:
      author = Author.objects.get(id=author)
    except:
      author = None

    # validate input (mustn't be empty)
    if not isbn or not title or not genre or not author or not publication_year:
      messages.error(request,'Fields cannot be left empty!', extra_tags='danger')
      return redirect(reverse('edit_book', args=[book.isbn]))

    isbn = isbn.strip()
    title = title.strip()

    book.title = title
    book.author = author
    book.genre = genre
    book.publication_year = publication_year
    book.page_count = page_count
    book.save()
      
    messages.success(request, 'Book updated successfully.', extra_tags='info')
    return redirect(reverse('edit_book', args=[book.isbn]))
  else:
    genres = Genre.objects.all().order_by('name')
    authors = Author.objects.all().order_by('first_name', 'last_name')
    return render(request, 'books/edit_book.html', {'book': book, 'genres': genres, 'authors': authors})

def delete_book(request, isbn):
  book = get_object_or_404(Book, isbn=isbn)
  if book:
    book.delete()
    messages.success(request, 'Book deleted succesfully.', extra_tags='info')
    return redirect(reverse('manage_books'))
  
def reports_books(request):

  if request.method == 'POST':
    
    genre = request.POST.get('genre')
    from_year = request.POST.get('from_year')
    until_year = request.POST.get('until_year')
    
    v_genre = genre
    if not genre:
      v_genre = -1

    v_from_year = from_year
    if not from_year:
      v_from_year = -1

    v_until_year = until_year
    if not until_year:
      v_until_year = -1
    
    # get books data
    results = None
    with connection.cursor() as cursor:
      cursor.callproc('get_books', [v_genre, v_from_year, v_until_year])
      results = cursor.fetchall()
    books = []
    for isbn, title, author_fname, author_lname, author_nationality, genre_name, publication_year, page_count in results:
      books.append({
        'isbn': isbn,
        'title': title,
        'author_fname': author_fname,
        'author_lname': author_lname,
        'author_nationality': author_nationality,
        'genre': genre_name,
        'publication_year': publication_year,
        'page_count': page_count
      })

    # get nationality book counts for chart
    results = None
    with connection.cursor() as cursor:
      cursor.callproc('get_nationalities_book_count', [v_genre, v_from_year, v_until_year])
      results = cursor.fetchall()
    chart_labels = []
    chart_data = []
    for l, d in results:
      chart_labels.append(l)
      chart_data.append(d)

    # get genres
    results = None
    with connection.cursor() as cursor:
      cursor.callproc('get_all_genres')
      results = cursor.fetchall()
    genres = []
    for genre_id, genre_name in results:
      genres.append({
        'id': genre_id,
        'name': genre_name
      })

    # get stats
    results = None
    with connection.cursor() as cursor:
      cursor.callproc('get_stats', [v_genre, v_from_year, v_until_year])
      results = cursor.fetchall()
    stats = {
      'Total Books': results[0][0],
      'Number of Genres': results[0][1],
      'Average Page Count': results[0][2],
      'Average Book Age (Years)': results[0][3]
    }

    return render(request, 'reports/books.html', {
      'genre': genre,
      'from_year': from_year,
      'until_year': until_year,
      'genres': genres, 
      'chart_labels': chart_labels,
      'chart_data': chart_data,
      'books': books,
      'stats': stats
      })
  
  else:
    
    # get books data
    results = None
    with connection.cursor() as cursor:
      cursor.callproc('get_books', [-1, -1, -1])
      results = cursor.fetchall()
    books = []
    for isbn, title, author_fname, author_lname, author_nationality, genre_name, publication_year, page_count in results:
      books.append({
        'isbn': isbn,
        'title': title,
        'author_fname': author_fname,
        'author_lname': author_lname,
        'author_nationality': author_nationality,
        'genre': genre_name,
        'publication_year': publication_year,
        'page_count': page_count
      }) 

    # get nationality book counts for chart
    results = None
    with connection.cursor() as cursor:
      cursor.callproc('get_nationalities_book_count', [-1, -1, -1])
      results = cursor.fetchall()
    chart_labels = []
    chart_data = []
    for l, d in results:
      chart_labels.append(l)
      chart_data.append(d)

    # get genres
    results = None
    with connection.cursor() as cursor:
      cursor.callproc('get_all_genres')
      results = cursor.fetchall()
    genres = []
    for genre_id, genre_name in results:
      genres.append({
        'id': genre_id,
        'name': genre_name
      })

    # get stats
    results = None
    with connection.cursor() as cursor:
      cursor.callproc('get_stats', [-1, -1, -1])
      results = cursor.fetchall()
    stats = {
      'Total Books': results[0][0],
      'Number of Genres': results[0][1],
      'Average Page Count': results[0][2],
      'Average Book Age (Years)': results[0][3]
    }

    return render(request, 'reports/books.html', {
      'genres': genres, 
      'chart_labels': chart_labels,
      'chart_data': chart_data,
      'books': books,
      'stats': stats
      })