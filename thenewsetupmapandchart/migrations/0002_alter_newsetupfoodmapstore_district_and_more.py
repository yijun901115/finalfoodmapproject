# Generated by Django 4.2.5 on 2023-09-16 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thenewsetupmapandchart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsetupfoodmapstore',
            name='district',
            field=models.CharField(blank=True, choices=[('大學城', '大學城'), ('大田寮', '大田寮'), ('金雞母', '金雞母'), ('水源街', '水源街'), ('淡大校內', '淡大校內')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='newsetupfoodmapstore',
            name='ratingcategories',
            field=models.CharField(blank=True, choices=[('3分或以上', '3分或以上'), ('4.5分或以上', '4.5分或以上'), ('4分或以上', '4分或以上')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='newsetupfoodmapstore',
            name='restauranttype',
            field=models.CharField(blank=True, choices=[('輕食餐廳', '輕食餐廳'), ('健康餐廳', '健康餐廳'), ('甜品店', '甜品店'), ('排餐餐廳', '排餐餐廳'), ('火鍋餐廳', '火鍋餐廳'), ('素食餐廳', '素食餐廳'), ('中式料理餐廳', '中式料理餐廳'), ('滷味店', '滷味店'), ('台式料理店', '台式料理店'), ('便當店', '便當店'), ('麵食館', '麵食館'), ('冰品飲料店', '冰品飲料店'), ('咖啡廳', '咖啡廳'), ('義式料理餐廳', '義式料理餐廳'), ('自助餐店', '自助餐店'), ('吃到飽餐廳', '吃到飽餐廳'), ('港式料理餐廳', '港式料理餐廳'), ('韓式料理餐廳', '韓式料理餐廳'), ('炸物店', '炸物店'), ('早午餐店', '早午餐店'), ('日式料理餐廳', '日式料理餐廳'), ('串燒烤肉店', '串燒烤肉店'), ('美式料理餐廳', '美式料理餐廳')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='newsetupfoodmapstore',
            name='totalreviewnumber',
            field=models.IntegerField(),
        ),
    ]
