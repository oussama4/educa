from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    """
    subject of the courses
    """

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

class Course(models.Model):
    # the instructor that created this course
    owner = models.ForeignKey(User, related_name='courses_created')
    # the subject that this course belong to
    subject = models.ForeignKey(Subject, related_name='courses')
    title = models.CharField(max_length=200)
    # a short label that identifies this course
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

class Module(models.Model):
    """
    each course has multiple modules
    """

    course = models.ForeignKey(Course, related_name='modules')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title