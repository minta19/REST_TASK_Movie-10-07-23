from django.urls import path
from .views import MovieCreateList,MovieUpdations

urlpatterns=[
    path('listcreate/',MovieCreateList.as_view(),name='list_create'),
    path('updations<int:pk>/',MovieUpdations.as_view(),name='upda_tions')
]

