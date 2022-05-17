from django.urls import path

from lesson2app import views
from lesson2app.apps import Lesson2AppConfig

app_name = Lesson2AppConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view()),
    path("news/", views.NewPageView.as_view()),
    path("courses/", views.CoursesPageView.as_view()),
    path("contacts/", views.ContactsPageView.as_view()),
    path("doc_site/", views.DocSitePageView.as_view()),
    path("login/", views.LoginPageView.as_view()),
]