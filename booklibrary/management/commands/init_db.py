from django.core.management.base import BaseCommand
from django.conf import settings
import mysql.connector

class Command(BaseCommand):
  def handle(self, *args, **kwargs):
    
    # get MYSQL settings
    name = settings.DATABASES['default']['NAME']
    user = settings.DATABASES['default']['USER']
    password = settings.DATABASES['default']['PASSWORD']
    host = settings.DATABASES['default']['HOST']
    port = settings.DATABASES['default']['PORT']

    # connect to MYSQL
    connection = mysql.connector.connect(host=host, port=port, user=user, password=password)
    cursor = connection.cursor()

    # create DB
    cursor.execute(f"drop database if exists {name};")
    cursor.execute(f"create database {name};")
    self.stdout.write(self.style.SUCCESS(f'Database "{name}" created successfully.'))
    
    # close connection
    connection.close()