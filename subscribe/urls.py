from django.urls import path
from subscribe.views import subscribe

urlpatterns = [
  path("", subscribe, name="polls_list"),
]