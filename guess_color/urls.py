from django.urls import path

from guess_color import views


urlpatterns = [
    path('', views.ItemNumberView.as_view(), name='color'),
    path('<int:pk>/', views.ItemColorViev.as_view()),
]