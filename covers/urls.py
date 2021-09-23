from django.urls import path
from . import views

urlpatterns = [
    path('pianocovers/', views.pianocovers, name='pianocovers'),
    path('guitarcovers/', views.guitarcovers, name='guitarcovers'),
    path('<int:cover_id>', views.coverdetail, name='coverdetail'),
]
