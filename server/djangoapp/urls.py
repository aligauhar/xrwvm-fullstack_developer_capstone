from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'djangoapp'

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('get_cars/', views.get_cars, name='get_cars'),
    path('get_dealers/', views.get_dealerships, name='fetch_dealers'),
    path('get_dealers/<str:state>/', views.get_dealerships, name='get_dealers_by_state'),
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),
    path('reviews/dealer/<int:dealer_id>/', views.get_dealer_reviews, name='dealer_reviews'),
    path('add_review/', views.add_review, name='add_review'),
    path('fetchDealers/', views.fetch_dealers, name='fetch_dealers'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
