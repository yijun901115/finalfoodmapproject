from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.


class newsetupFoodmapStore(models.Model):

    ratingcategories_choice = {
        ('4.5分或以上', '4.5分或以上'),
        ('4分或以上', '4分或以上'),
        ('3分或以上', '3分或以上'),
    }

    district_choice = {
        ('淡大校內', '淡大校內'),
        ('大學城', '大學城'),
        ('水源街', '水源街'),
        ('大田寮', '大田寮'),
        ('金雞母', '金雞母'),
    }

    restauranttype_choice = {
        ('健康餐廳', '健康餐廳'),
        ('台式料理店', '台式料理店'),
        ('早午餐店', '早午餐店'),
        ('滷味店', '滷味店'),
        ('義式料理餐廳', '義式料理餐廳'),
        ('炸物店', '炸物店'),
        ('美式料理餐廳', '美式料理餐廳'),
        ('麵食館', '麵食館'),
        ('便當店', '便當店'),
        ('中式料理餐廳', '中式料理餐廳'),
        ('日式料理餐廳', '日式料理餐廳'),
        ('吃到飽餐廳', '吃到飽餐廳'),
        ('串燒烤肉店', '串燒烤肉店'),
        ('冰品飲料店', '冰品飲料店'),
        ('火鍋餐廳', '火鍋餐廳'),
        ('韓式料理餐廳', '韓式料理餐廳'),
        ('素食餐廳', '素食餐廳'),
        ('咖啡廳', '咖啡廳'),
        ('甜品店', '甜品店'),
        ('輕食餐廳', '輕食餐廳'),
        ('自助餐店', '自助餐店'),
        ('排餐餐廳', '排餐餐廳'),
        ('港式料理餐廳', '港式料理餐廳'),
    }




    district = models.CharField(max_length=30, blank=True, null=True, choices=district_choice)
    restaurantname = models.CharField(max_length=250)
    address = models.TextField()
    contactinfo = models.TextField()
    googlereviewlink = models.TextField()
    # restaurantcoverphoto = models.ImageField(max_length=100, default=0, upload_to='staticFiles/img')
    restaurantcoverphotourl = models.URLField(max_length=300, default='')
    googlemapiframeembeddedcode = models.TextField()
    openingtime = models.TextField()
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    ratingintotaloffive = models.FloatField()
    ratingcategories = models.CharField(max_length=30, blank=True, null=True, choices=ratingcategories_choice)
    restauranttype = models.CharField(max_length=30, blank=True, null=True, choices=restauranttype_choice)
    totalreviewnumber = models.CharField(max_length=300, blank=False, null=False,)
    commentOne = models.TextField()
    commentTwo = models.TextField()
    commentThree = models.TextField()
    commentFour = models.TextField()
    commentFive = models.TextField()
    foodmapmenuOne = models.URLField(max_length=300, default='')
    foodmapmenuTwo = models.URLField(max_length=300, default='')
    foodmapmenuThree = models.URLField(max_length=300, default='')
    foodmapmenuFour = models.URLField(max_length=300, default='')
    foodmapmenuFive = models.URLField(max_length=300, default='')
    foodmapmenuSix = models.URLField(max_length=300, default='')
    foodmapmenuSeven = models.URLField(max_length=300, default='')
    foodmapmenuEight = models.URLField(max_length=300, default='')
    foodmapmenuNine = models.URLField(max_length=300, default='')
    foodmapDishesOne = models.URLField(max_length=300, default='')
    foodmapDishesTwo = models.URLField(max_length=300, default='')
    foodmapDishesThree = models.URLField(max_length=300, default='')
    # extractedpngfilename = models.CharField(max_length=200, default='', blank=True, null=True)

    def __str__(self):
        return self.restaurantname