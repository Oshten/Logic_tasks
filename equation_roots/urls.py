from django.urls import path

from equation_roots import views

urlpatterns = [
    path('', views.EquationView.as_view(), name='equation'),
    path('<int:pk>/solution/', views.SolutionView.as_view(), name='solution'),
]
