from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path("result", views.result, name="result"),
    # path('social_links', views.social_links),
    path('send-email/', views.send_email, name='send_email'),
    path('', views.weather_with_activities, name='base'),
]
