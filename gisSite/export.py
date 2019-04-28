import os
import csv
from gisApp.models import AOF

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gisSite.settings')

data = csv.DictReader(open("/home/aquila/Projects/gdal/tutorials_geodjango/ngocom/reporter/PROJECT/AOF_ID.csv"))
for row in data:
    AOF.objects.create(name=row['sector_id'], number=row['sectors'])
