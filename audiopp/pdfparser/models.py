import uuid
from django.db import models
from django.urls import reverse


class Figure(models.Model):

    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')


class Reference(models.Model):

    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    journal = models.CharField(max_length=200)
    volume = models.CharField(max_length=200)
    issue = models.CharField(max_length=200)
    pages = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    doi = models.CharField(max_length=200)


class Section(models.Model):

    heading = models.CharField(max_length=200)
    body = models.TextField()
    figures = models.ManyToManyField(Figure)


class Paper(models.Model):

    paper_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, blank=True)
    authors = models.CharField(max_length=200, blank=True)
    abstract = models.TextField(blank=True)
    sections = models.ManyToManyField(Section, blank=True)
    references = models.ManyToManyField(Reference, blank=True)
    figures = models.ManyToManyField(Figure, blank=True)
    doi = models.CharField(max_length=200, blank=True)
    pdf = models.FileField(upload_to='pdfs/', blank=True)

    def get_absolute_url(self):
        return reverse('papers:paper_detail', args=[str(self.paper_id)])

    def __str__(self):
        return "%s" % self.title
