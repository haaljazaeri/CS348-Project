from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
  def handle(self, *args, **kwargs):
    with connection.cursor() as cursor:
      
      # populate nationality table
      cursor.execute("INSERT INTO `nationality` (`id`, `name`) VALUES\
                      (1, 'American'),\
                      (2, 'British'),\
                      (3, 'Canadian'),\
                      (4, 'French'),\
                      (5, 'German'),\
                      (6, 'Russian');")
      self.stdout.write(self.style.SUCCESS(f'Nationality table populated successfully.'))
      
      # populate author table
      cursor.execute("INSERT INTO `author` (`id`, `first_name`, `last_name`, `nationality_id`) VALUES \
                      (1, 'Mark', 'Twain', 1),\
                      (2, 'Jane', 'Austen', 2),\
                      (3, 'J.K.', 'Rowling', 2),\
                      (4, 'Jules', 'Verne', 4),\
                      (5, 'Fyodor', 'Dostoevsky', 6),\
                      (6, 'Hermann', 'Hesse', 5);")
      self.stdout.write(self.style.SUCCESS(f'Author table populated successfully.'))
      
      # populate genre table
      cursor.execute("INSERT INTO `genre` (`id`, `name`) VALUES\
                      (1, 'Fiction'),\
                      (2, 'Non-Fiction'),\
                      (3, 'Science Fiction'),\
                      (4, 'Fantasy'),\
                      (5, 'Mystery'),\
                      (6, 'Biography'),\
                      (7, 'Adventure');")
      self.stdout.write(self.style.SUCCESS(f'Genre table populated successfully.'))

      # populate book table
      cursor.execute("INSERT INTO `book`\
                      (`isbn`, `title`, `publication_year`, `author_id`, `genre_id`, `page_count`) VALUES\
                      ('9780000000001', 'Adventures of Huckleberry Finn', 1884, 1, 1, 279),\
                      ('9780000000002', 'Pride and Prejudice', 1813, 2, 1, 635),\
                      ('9780000000003', 'Harry Potter and the Philosopher\\'s Stone', 1997, 3, 4, 180),\
                      ('9780000000004', 'Twenty Thousand Leagues Under the Sea', 1870, 4, 3, 1225),\
                      ('9780000000005', 'Crime and Punishment', 1866, 5, 5, 671),\
                      ('9780000000006', 'Siddhartha', 1922, 6, 1, 277),\
                      ('9780000000007', 'Emma', 1815, 2, 1, 281),\
                      ('9780000000008', 'Harry Potter and the Chamber of Secrets', 1998, 3, 4, 328),\
                      ('9780000000009', 'Journey to the Center of the Earth', 1864, 4, 3, 824),\
                      ('9780000000010', 'The Brothers Karamazov', 1880, 5, 1, 730),\
                      ('9780000000011', 'Steppenwolf', 1927, 6, 1, 268),\
                      ('9780000000012', 'Persuasion', 1817, 2, 1, 416),\
                      ('9780000000013', 'Harry Potter and the Prisoner of Azkaban', 1999, 3, 4, 541),\
                      ('9780000000014', 'Around the World in Eighty Days', 1873, 4, 7, 1463),\
                      ('9780000000015', 'The Idiot', 1869, 5, 1, 328),\
                      ('9780000000016', 'The Glass Bead Game', 1943, 6, 3, 863),\
                      ('9780000000017', 'Harry Potter and the Goblet of Fire', 2000, 3, 4, 532),\
                      ('9780000000019', 'The Mysterious Island', 1874, 4, 3, 683),\
                      ('9780000000020', 'Notes from Underground', 1864, 5, 5, 864),\
                      ('9780000000021', 'Narcissus and Goldmund', 1930, 6, 1, 366),\
                      ('9780000000022', 'Mansfield Park', 1814, 2, 1, 192),\
                      ('9780000000023', 'Harry Potter and the Order of the Phoenix', 2003, 3, 4, 505),\
                      ('9780000000024', 'The Green Ray', 1882, 4, 1, 880),\
                      ('9780000000025', 'The Gambler', 1867, 5, 1, 1276),\
                      ('9780000000026', 'Demian', 1919, 6, 1, 280),\
                      ('9780000000027', 'Lady Susan', 1871, 2, 1, 254),\
                      ('9780000000028', 'Harry Potter and the Half-Blood Prince', 2005, 3, 4, 188),\
                      ('9780000000029', 'The Survivors of the Chancellor', 1875, 4, 7, 326),\
                      ('9780000000030', 'The Eternal Husband', 1870, 5, 1, 418);")
      self.stdout.write(self.style.SUCCESS(f'Book table populated successfully.'))
