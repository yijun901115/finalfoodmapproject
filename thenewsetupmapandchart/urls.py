from django.urls import path
from thenewsetupmapandchart import views
app_name = 'chartandmap'
urlpatterns = [
    path('charts/', views.charts, name="charts"),
    path('map/', views.maps, name="map"),
    path('chartsormapdetails/<int:pk>', views.chartsandmapdetail, name="detail"),
    path('menu/<int:pk>', views.menu, name="menu"),
    path('reviewdisplay/<int:pk>', views.reviewdisplay, name="reviewdisplay"),
    path('meals/<int:pk>', views.meals, name="meals"),
]