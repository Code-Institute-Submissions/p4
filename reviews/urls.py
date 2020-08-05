from django.contrib import admin
from django.urls import path
import reviews.views

urlpatterns = [
    path('', reviews.views.reviews),
    path('create/', reviews.views.create_review, name="create_review_route")
]