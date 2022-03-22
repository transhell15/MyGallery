from django.urls import path

from albumApp.views import (
    LandingPageView,
    ViewPhotoPageView,
    AddPhotoPageView,
)


urlpatterns = [
    path('', LandingPageView, name='landing_page'),
    path('view/<str:photo_id>/', ViewPhotoPageView, name='viewphoto_page'),
    path('add/', AddPhotoPageView, name="addphoto_page"),
]
