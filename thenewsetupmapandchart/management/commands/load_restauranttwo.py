import csv
import re
from django.conf import settings
from django.core.management.base import BaseCommand
from thenewsetupmapandchart.models import newsetupFoodmapStore


class Command(BaseCommand):
    help = 'Load data from Foodmap store file'

    def handle(self, *args, **options):
        data_file = settings.BASE_DIR / 'mapdatainforecord' / 'finalversionfoodmapinfo_modified_one_two_three_four.csv'
        keys = ('district', 'restaurantName', 'address', 'contactInfo', 'googlereviewlink', 'openingtime', 'latitude',
                'longitude', 'ratingintotaloffive', 'ratingcategories', 'restauranttype', 'restaurantcoverphotourl')

        records = []
        with open(data_file, 'r', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                records.append({k: row[k] for k in keys})

        # Iterate through records
        for record in records:
            # Extract the PNG file name from restaurantcoverphotourl using regex
            cover_photo_url = record['restaurantcoverphotourl']
            match1 = re.search(r'([^/]+)$', cover_photo_url)  # First regex pattern
            match2 = re.search(r'/([^/]+)?', cover_photo_url)  # Second regex pattern
            # match1 = re.search(r'([^/]+)\.PNG$', cover_photo_url)  # First regex pattern
            # match2 = re.search(r'/([^/]+)\.PNG\?raw=true$', cover_photo_url)  # Second regex pattern
            # match3 = re.search(r'/([^/]+)\.jpg$', cover_photo_url)  # Third regex pattern
            # match4 = re.search(r'/([^/]+)\.jpg\?raw=true$', cover_photo_url)  # Fourth regex pattern

            # Determine the PNG file name based on the regex matches
            if match1:
                record['extractedpngfilename'] = match1.group(1)
            elif match2:
                record['extractedpngfilename'] = match2.group(1)
            # elif match3:
            #    record['extractedpngfilename'] = match3.group(1)
            # elif match4:
            #    record['extractedpngfilename'] = match4.group(1)
            else:
                record['extractedpngfilename'] = None  # Set to None if no match is found

            # Add the data to the database
            newsetupFoodmapStore.objects.get_or_create(
                district=record['district'],
                restaurantname=record['restaurantName'],
                address=record['address'],
                contactinfo=record['contactInfo'],
                googlereviewlink=record['googlereviewlink'],
                openingtime=record['openingtime'],
                latitude=record['latitude'],
                longitude=record['longitude'],
                ratingintotaloffive=record['ratingintotaloffive'],
                ratingcategories=record['ratingcategories'],
                restauranttype=record['restauranttype'],
                restaurantcoverphotourl=record['restaurantcoverphotourl'],
                # png_file_name=png_file_name  # Add the extracted PNG file name to the model
                extractedpngfilename=record['extractedpngfilename']

            )
