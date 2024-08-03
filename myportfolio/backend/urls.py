from django.urls import path
from . import views


urlpatterns = [
    path("about/", views.about_view, name="about"),
    path("projects/", views.projects_view, name="projects"),
    path("experience/", views.experiences_view, name="experiences"),
    path("certifications/", views.certifications_view, name="certifications"),
    path("socials/", views.socials_view, name="socials"),
    path("tools-and-technologies/", views.tools_and_technologies_view, name="tools-and-technologies")
]