# Generated by Django 4.2.5 on 2023-09-16 04:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='newsetupFoodmapStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(blank=True, choices=[('大學城', '大學城'), ('金雞母', '金雞母'), ('大田寮', '大田寮'), ('淡大校內', '淡大校內'), ('水源街', '水源街')], max_length=30, null=True)),
                ('restaurantname', models.CharField(max_length=250)),
                ('address', models.TextField()),
                ('contactinfo', models.TextField()),
                ('googlereviewlink', models.TextField()),
                ('restaurantcoverphotourl', models.URLField(default='', max_length=300)),
                ('googlemapiframeembeddedcode', models.TextField()),
                ('openingtime', models.TextField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('ratingintotaloffive', models.FloatField()),
                ('ratingcategories', models.CharField(blank=True, choices=[('3分或以上', '3分或以上'), ('4分或以上', '4分或以上'), ('4.5分或以上', '4.5分或以上')], max_length=30, null=True)),
                ('restauranttype', models.CharField(blank=True, choices=[('港式料理餐廳', '港式料理餐廳'), ('輕食餐廳', '輕食餐廳'), ('滷味店', '滷味店'), ('吃到飽餐廳', '吃到飽餐廳'), ('義式料理餐廳', '義式料理餐廳'), ('麵食館', '麵食館'), ('串燒烤肉店', '串燒烤肉店'), ('甜品店', '甜品店'), ('健康餐廳', '健康餐廳'), ('台式料理店', '台式料理店'), ('咖啡廳', '咖啡廳'), ('美式料理餐廳', '美式料理餐廳'), ('自助餐店', '自助餐店'), ('冰品飲料店', '冰品飲料店'), ('便當店', '便當店'), ('炸物店', '炸物店'), ('火鍋餐廳', '火鍋餐廳'), ('排餐餐廳', '排餐餐廳'), ('日式料理餐廳', '日式料理餐廳'), ('素食餐廳', '素食餐廳'), ('韓式料理餐廳', '韓式料理餐廳'), ('早午餐店', '早午餐店'), ('中式料理餐廳', '中式料理餐廳')], max_length=30, null=True)),
                ('totalreviewnumber', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('commentOne', models.TextField()),
                ('commentTwo', models.TextField()),
                ('commentThree', models.TextField()),
                ('commentFour', models.TextField()),
                ('commentFive', models.TextField()),
                ('foodmapmenuOne', models.URLField(default='', max_length=300)),
                ('foodmapmenuTwo', models.URLField(default='', max_length=300)),
                ('foodmapmenuThree', models.URLField(default='', max_length=300)),
                ('foodmapmenuFour', models.URLField(default='', max_length=300)),
                ('foodmapmenuFive', models.URLField(default='', max_length=300)),
                ('foodmapmenuSix', models.URLField(default='', max_length=300)),
                ('foodmapmenuSeven', models.URLField(default='', max_length=300)),
                ('foodmapmenuEight', models.URLField(default='', max_length=300)),
                ('foodmapmenuNine', models.URLField(default='', max_length=300)),
                ('foodmapDishesOne', models.URLField(default='', max_length=300)),
                ('foodmapDishesTwo', models.URLField(default='', max_length=300)),
                ('foodmapDishesThree', models.URLField(default='', max_length=300)),
            ],
        ),
    ]