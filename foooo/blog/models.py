from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=250)
    url = models.URLField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    published = models.BooleanField(default=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name="posts")

    def __str__(self):
        return f"{self.title} {self.content} {self.blog.name} {self.authors}"
