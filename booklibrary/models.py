from django.db import models

class Nationality(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name
  
  class Meta:
    db_table = "nationality"

class Author(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"
  
  class Meta:
    db_table = "author"
  
class Genre(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  class Meta:
    db_table = "genre"

class Book(models.Model):
  isbn = models.CharField(max_length=13, primary_key=True)
  title = models.CharField(max_length=100)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  genre = models.ForeignKey(Genre, on_delete=models.CASCADE, db_index=True)
  publication_year = models.IntegerField(db_index=True)
  page_count = models.IntegerField()
  
  def __str__(self):
    return self.title
  
  class Meta:
    db_table = "book"