from django.db import models

class About(models.Model):
    name  = models.CharField(max_length=50, blank=False, null=False)
    about = models.CharField(max_length=1000, blank=False, null=False)

class Project(models.Model):
    pass


class Certification(models.Model):
    pass


class Experiences(models.Model):
    pass


class Social(models.Model):
    pass


class ToolsNTechnologies(models.Model):
    pass




