from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
  def handle(self, *args, **kwargs):
    with connection.cursor() as cursor:

      # procedure to get all genres
      cursor.execute("drop procedure if exists get_all_genres;\
                      create procedure get_all_genres ()\
                      begin\
                      	select g.id, g.`name`\
                          from genre g\
                          order by g.name;\
                      end")
      self.stdout.write(self.style.SUCCESS(f'get_all_genres procedure created successfully.'))

      # procedure to get books filtered
      cursor.execute("drop procedure if exists get_books;\
                      create procedure get_books (\
                      	in genre_id int,\
                          in from_year int,\
                          in until_year int\
                      )\
                      begin\
                      	declare updated_from_year int;\
                          declare updated_until_year int;\
                          create temporary table if not exists genre_ids (id int);\
                          if genre_id = -1 then\
                      		insert into genre_ids (select g.id from genre g);\
                          else\
                      		insert into genre_ids (select g.id from genre g where g.id = genre_id);\
                          end if;\
                          if from_year = -1 then\
                      		set updated_from_year = (select min(b.publication_year) from book b);\
                          else\
                      		set updated_from_year = from_year;\
                          end if;\
                          if until_year = -1 then\
                      		set updated_until_year = (select max(b.publication_year) from book b);\
                          else\
                      		set updated_until_year = until_year;\
                          end if;\
                          select b.isbn, b.title, a.first_name, a.last_name, n.`name`, g.`name`, b.publication_year, b.page_count\
                          from book b\
                          join author a on b.author_id = a.id\
                          join nationality n on a.nationality_id = n.id\
                          join genre g on b.genre_id = g.id\
                          where (b.genre_id in (select g.id from genre_ids g)) and \
                      		  (b.publication_year >= updated_from_year) and\
                                (b.publication_year <= updated_until_year)\
                          order by b.title;\
                          drop temporary table if exists genre_ids;\
                      end;")
      self.stdout.write(self.style.SUCCESS(f'get_books procedure created successfully.'))

      cursor.execute("drop procedure if exists get_nationalities_book_count;\
        create procedure get_nationalities_book_count (\
        	in genre_id int,\
            in from_year int,\
            in until_year int\
        )\
        begin\
        	declare updated_from_year int;\
            declare updated_until_year int;\
            create temporary table if not exists genre_ids (id int);\
            if genre_id = -1 then\
        		insert into genre_ids (select g.id from genre g);\
            else\
        		insert into genre_ids (select g.id from genre g where g.id = genre_id);\
            end if;\
            if from_year = -1 then\
        		set updated_from_year = (select min(b.publication_year) from book b);\
            else\
        		set updated_from_year = from_year;\
            end if;\
            if until_year = -1 then\
        		set updated_until_year = (select max(b.publication_year) from book b);\
            else\
        		set updated_until_year = until_year;\
            end if;\
            select n.`name`, count(b.isbn)\
            from book b\
            join author a on b.author_id = a.id\
            join nationality n on a.nationality_id = n.id\
            join genre g on b.genre_id = g.id\
            where (b.genre_id in (select g.id from genre_ids g)) and \
        		  (b.publication_year >= updated_from_year) and\
                  (b.publication_year <= updated_until_year)\
            group by n.`name`;\
            drop temporary table if exists genre_ids;\
        end")
      self.stdout.write(self.style.SUCCESS(f'get_nationalities_book_count procedure created successfully.'))

      cursor.execute("drop procedure if exists get_stats;\
                      create procedure get_stats (\
                      	in genre_id int,\
                          in from_year int,\
                          in until_year int\
                      )\
                      begin\
                      	declare updated_from_year int;\
                          declare updated_until_year int;\
                          create temporary table if not exists genre_ids (id int);\
                          if genre_id = -1 then\
                      		insert into genre_ids (select g.id from genre g);\
                          else\
                      		insert into genre_ids (select g.id from genre g where g.id = genre_id);\
                          end if;\
                          if from_year = -1 then\
                      		set updated_from_year = (select min(b.publication_year) from book b);\
                          else\
                      		set updated_from_year = from_year;\
                          end if;\
                          if until_year = -1 then\
                      		set updated_until_year = (select max(b.publication_year) from book b);\
                          else\
                      		set updated_until_year = until_year;\
                          end if;\
                          select count(b.isbn), count(distinct b.genre_id), avg(b.page_count), avg(year(curdate()) - b.publication_year)\
                          from book b\
                          join author a on b.author_id = a.id\
                          join nationality n on a.nationality_id = n.id\
                          join genre g on b.genre_id = g.id\
                          where (b.genre_id in (select g.id from genre_ids g)) and \
                      		  (b.publication_year >= updated_from_year) and\
                                (b.publication_year <= updated_until_year);\
                          drop temporary table if exists genre_ids;\
                      end;")
      self.stdout.write(self.style.SUCCESS(f'get_stats procedure created successfully.'))
      
