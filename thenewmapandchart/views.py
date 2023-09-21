from django.shortcuts import render
#from .models import newFoodmapStore


# Create your views here.


#def charts(request):
#    foodstoresinfochart = newFoodmapStore.objects.all();
#    return render(request, "charts.html", {'foodstoresinfochart': foodstoresinfochart})


#def maps(request):
#    foodstores = list(
#        newFoodmapStore.objects.values('district', 'restaurantname', 'address', 'contactinfo', 'googlereviewlink',
#                                    'openingtime',
#                                    'latitude', 'longitude', 'ratingintotaloffive', 'ratingcategories',
#                                    'restauranttype', 'restaurantcoverphoto', 'restaurantcoverphotourl')[:85])
#    foodstoresinfo = newFoodmapStore.objects.all();

#    context = {'foodstores': foodstores,
#               'foodstoresinfo': foodstoresinfo, }

#    return render(request, "map.html", context)


#def chartsandmapdetail(request, pk):
#    foodstoresinfodetail = newFoodmapStore.objects.get(id=pk);
#    return render(request, "chartsandmapdetail.html", {'foodstoresinfodetail': foodstoresinfodetail})

