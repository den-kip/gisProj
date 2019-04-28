import os
import csv
from django.core.management.base import BaseCommand
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gisSite.settings')
# application = get_wsgi_application()

from django.apps import apps
mmodel = apps.get_model('gisApp','mmodel')

from mmodel import AOF

class Command(BaseCommand):
    def import_AOF_from_csv_file(self):
        data_folder = os.path .abspath(os.path.join(os.path.dirname(__file__),'store'))
        print(data_folder, 'data_folder')
        for data_file in os.listdir(data_folder):
            with open(os.path.join(data_folder, data_file), encoding='utf-8') as data_file:
                data = csv.reader(open('/home/aquila/Projects/gdal/tutorials_geodjango/ngocom/reporter/PROJECT/AOF_ID.csv'))
                for data_object in data:
                    SECTOR_ID = data_object[2]
                    SECTOR_NAME = data_object[3]        

                    try:
                        AOF, created = AOF.objects.get_or_create(
                            SECTOR_ID=SECTOR_ID,
                            SECTOR_NAME=SECTOR_NAME
                            
                        )
                        if created:
                            AOF.save()
                            display_format = "\nAOF, {}, has been saved."
                        
                    except Exception as ex:
                        print(str(ex))
                        msg = "\n\nSomething went wrong saving this file: {}\n{}"
                        print (msg)
    def handle(self, *args, **options):
        self.import_AOF_from_csv_file()



