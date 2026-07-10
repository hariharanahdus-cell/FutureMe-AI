from django.urls import path

from .views import future_prediction



urlpatterns = [

    path(
        "future/",
        future_prediction
    ),

]