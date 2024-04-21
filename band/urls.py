from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'band'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:song_id>', views.detail, name='detail'),
    path('<int:song_id>/results/', views.results, name='results'),
    path('<int:song_id>/vote/', views.vote, name='vote'),
    path('concert_locations/', views.concert_locations, name='concert_locations'),
    path('contact_details/', views.contact_details, name='contact_details')
]