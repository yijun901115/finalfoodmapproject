import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from thenewsetupmapandchart.models import newsetupFoodmapStore


class Command(BaseCommand):
    help = 'Load data from Foodmap store file'

    def handle(self, *args, **options):
        data_file = settings.BASE_DIR / 'mapdatainforecord' / 'review_edited_finalversionfoodmapinfo_modified_one_two_finalVersion_copy_reencoded_reformatted.csv'
        keys = ('district', 'restaurantName', 'address', 'contactInfo', 'googlereviewlink', 'openingtime', 'latitude',
                'longitude', 'ratingintotaloffive', 'ratingcategories', 'restauranttype', 'restaurantcoverphotourl', 'googlemapiframeembeddedcode', 'totalreviewnumber', 'commentOne','commentTwo','commentThree','commentFour','commentFive','foodmapmenuOne','foodmapmenuTwo','foodmapmenuThree','foodmapmenuFour','foodmapmenuFive','foodmapmenuSix','foodmapmenuSeven','foodmapmenuEight','foodmapmenuNine','foodmapDishesOne','foodmapDishesTwo','foodmapDishesThree')  # the CSV columns we will gather data from.

        records = []
        with open(data_file, 'r', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                records.append({k: row[k] for k in keys})

        # extract the latitude and longitude from the Point object
        # longitude = record['longitude'] = float(longitude)
        # latitude = record['latitude'] = float(latitude)

        # add the data to the database
        for record in records:
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
                googlemapiframeembeddedcode=record['googlemapiframeembeddedcode'],
                totalreviewnumber=record['totalreviewnumber'],
                commentOne=record['commentOne'],
                commentTwo=record['commentTwo'],
                commentThree=record['commentThree'],
                commentFour=record['commentFour'],
                commentFive=record['commentFive'],
                foodmapmenuOne=record['foodmapmenuOne'],
                foodmapmenuTwo =record['foodmapmenuTwo'],
                foodmapmenuThree =record['foodmapmenuThree'],
                foodmapmenuFour =record['foodmapmenuFour'],
                foodmapmenuFive =record['foodmapmenuFive'],
                foodmapmenuSix=record['foodmapmenuSix'],
                foodmapmenuSeven=record['foodmapmenuSeven'],
                foodmapmenuEight=record['foodmapmenuEight'],
                foodmapmenuNine=record['foodmapmenuNine'],
                foodmapDishesOne=record['foodmapDishesOne'],
                foodmapDishesTwo=record['foodmapDishesTwo'],
                foodmapDishesThree=record['foodmapDishesThree'],
            )
