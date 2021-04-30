from django.urls import path, include
from paste.views import pasteview, index
urlpatterns = [
    path("", index),
    path('<slug:url>', pasteview),
]