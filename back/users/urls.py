from django.urls import path, re_path, include

urlpatterns = [
    # drf_social_oauth2
    re_path(r"^auth/", include("drf_social_oauth2.urls", namespace="drf")),
]
