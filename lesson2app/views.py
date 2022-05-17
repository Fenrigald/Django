from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import TemplateView

class MainPageView(TemplateView):
    template_name = "lesson2app/index.html"

class NewPageView(TemplateView):
    template_name = "lesson2app/news.html"

class CoursesPageView(TemplateView):
    template_name = "lesson2app/courses_list.html"

class ContactsPageView(TemplateView):
    template_name = "lesson2app/contacts.html"

class DocSitePageView(TemplateView):
    template_name = "lesson2app/doc_site.html"

class LoginPageView(TemplateView):
    template_name = "lesson2app/login.html"