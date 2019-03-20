from django.urls import path, include
from . import views


urlpatterns = [
    path('bucketlists/', views.CreateView.as_view(), name="create"),
    path('bucketlists/<int:pk>', views.DetailsView.as_view(), name="details")
]
