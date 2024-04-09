from django.urls import include, path

urlpatterns = [
    path('auth', include('apps.Users.auth.urls')),
    path('cars', include('apps.cars_details.cars.urls')),
    path('car_views', include('apps.cars_details.car_views.urls')),
    path('brand_models', include('apps.cars_details.brand_models.urls')),
    # path('cars_model', include('apps.cars_details.car_model.urls')),
    # path('car_dealership', include('apps.partners.car_dealership.urls')),
    # path('car_dealership_admin', include('apps.partners.car_dealership_admin.urls')),
    # path('car_dealership_manager', include('apps.partners.car_dealership_manager.urls')),
    # path('car_dealership_mechanic', include('apps.partners.car_dealership_mechanic.urls')),
    # path('car_dealership_sales', include('apps.partners.car_dealership_sales.urls'))
    path('sellers', include('apps.Users.sellers.urls')),
    path('premium_sellers', include('apps.Users.premium_sellers.urls')),
    # path('sale_announcement', include('apps.sale_announcement')),
    # path('visitors', include('apps.Users.visitors.urls')),
    path('info', include('apps.info.urls')),
    path('managers', include('apps.Users.managers.urls')),
    path('admins', include('apps.Users.admins.urls')),
    path('users', include('apps.Users.users.urls')),
    # path('send_message', include('apps.messages.urls'))



]

