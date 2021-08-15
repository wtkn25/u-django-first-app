from django.urls import path

from . import views

app_name = "form_app"

urlpatterns = [
    path("", views.SampleView.as_view(), name="index"),
    path("create-question", views.QuestionCreateView.as_view(), name="create-question"),
]
