import json

from django.core.management import BaseCommand

from books.models import Books
from writer.models import Writer


class Command(BaseCommand):
    help = 'Yazarları ve kitapları bir JSON dosyasından içe aktarır'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='JSON dosyasının yolu')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']

        with open(json_file, 'r') as file:
            data = json.load(file)

        for author_data in data['authors']:
            writer, created = Writer.objects.get_or_create(
                full_name=author_data['name'],
                defaults={
                    'birth_date': author_data['birth_date'],
                    'bio': author_data['bio']
                }
            )

            for book_data in author_data['books']:
                Books.objects.get_or_create(
                    writer=writer,
                    title=book_data['title'],
                    defaults={
                        'published_date': book_data['published_date'],
                        'genre': book_data['genre'],
                        'isbn': book_data['isbn']
                    }
                )

        self.stdout.write(self.style.SUCCESS('Yazarlar ve kitaplar başarıyla içe aktarıldı'))
