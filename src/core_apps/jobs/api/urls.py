from django.urls import path

from .views import JobFetchAPIView


urlpatterns = [
    path("fetch/", JobFetchAPIView.as_view(), name="fetch"),
]
