from django.shortcuts import render
from .models import newsetupFoodmapStore


# Create your views here.


def charts(request):
    foodstoresinfochart = newsetupFoodmapStore.objects.all();
    return render(request, 'charts.html', {'foodstoresinfochart': foodstoresinfochart})


def maps(request):
    foodstores = list(
        newsetupFoodmapStore.objects.values('id', 'district', 'restaurantname', 'address', 'contactinfo',
                                            'googlereviewlink', 'openingtime', 'latitude', 'longitude',
                                            'ratingintotaloffive', 'ratingcategories', 'restauranttype',
                                            'restaurantcoverphotourl')[:85])

    # 'district', 'restaurantname', 'address', 'contactinfo', 'googlereviewlink',
    # 'openingtime',
    # 'latitude', 'longitude', 'ratingintotaloffive', 'ratingcategories',
    # 'restauranttype', 'restaurantcoverphoto', 'restaurantcoverphotourl')[:85])
    foodstoresinfo = newsetupFoodmapStore.objects.all();

    context = {'foodstores': foodstores,
               'foodstoresinfo': foodstoresinfo, }

    return render(request, 'map.html', context)


def chartsandmapdetail(request, pk):
    foodstoresinfodetail = newsetupFoodmapStore.objects.get(id=pk);
    return render(request, 'chartsandmapdetail.html', {'foodstoresinfodetail': foodstoresinfodetail})


def menu(request,pk):
    foodstoresmenu = newsetupFoodmapStore.objects.get(id=pk);
    return render(request, 'menu.html', {'foodstoresmenu': foodstoresmenu})


def reviewdisplay(request,pk):
    foodstoresreview = newsetupFoodmapStore.objects.get(id=pk);
    return render(request, 'review.html', {'foodstoresreview': foodstoresreview})


def meals(request,pk):
    foodstoresmeals = newsetupFoodmapStore.objects.get(id=pk);
    return render(request, 'meals.html', {'foodstoresmeals': foodstoresmeals})
