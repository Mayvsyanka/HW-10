from django.db import models


class Author (models.Model):
    fullname = models.CharField(max_length=50)
    born_date = models.CharField(max_length=50, null=True)

    born_location = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)


class Quote(models.Model):
    quote = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)