from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clients', views.ClientViewSet)
router.register('games', views.GameViewSet)
router.register('rentals', views.RentalViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/client_rentals/<int:client_id>/', views.ClientRentalsView.as_view(), name='client_rentals'),
    path('api/create_rental/', views.CreateRentalView.as_view(), name='create_rental'),
    path('api/most_rented_game_by_age/', views.MostRentedGameByAgeView.as_view(), name='most_rented_game_by_age'),
]