from django.urls import path

from . import views

app_name = 'part'

urlpatterns = [
    path('new/', views.new_part, name='new_part'),
    path('search/', views.search, name='search'),
    path('results/', views.results, name='results'),
    path('<int:pk>/', views.part_details, name='part_details'),
    path('<int:pk>/sell/', views.sell_part, name='sell_part'),
    path('<int:pk>/add/', views.add_more, name='add_more'),
]