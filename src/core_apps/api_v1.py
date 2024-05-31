from django.urls import path, include


urlpatterns = [
    path(
        "jobs/",
        include(("core_apps.jobs.api.urls", "jobs"), namespace="jobs"),
        name="jobs",
    ),
]
