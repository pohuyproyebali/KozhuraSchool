from django.db import models


# Create your models here.


class ApplicationFromEmployer(models.Model):
    employer_name = models.CharField(max_length=100)
    employer_email = models.EmailField(max_length=100)
    employer_phone = models.CharField(max_length=100)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.employer_name


class NewsBlock(models.Model):
    news_title = models.CharField(max_length=100)
    news_content = models.TextField()
    news_date = models.CharField(max_length=100)

    def __str__(self):
        return self.news_title


class NewsImage(models.Model):
    news = models.ForeignKey(NewsBlock, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='', blank=True)

    def __str__(self):
        return self.news


class InformationBlock(models.Model):
    information_title = models.CharField(max_length=100)
    information_content = models.TextField()

    def __str__(self):
        return self.information_title


class InnovationBlock(models.Model):
    innovation_name = models.CharField(max_length=150)
    innovation_image = models.ImageField(upload_to='', blank=True)
    innovation_file = models.FileField(upload_to='', blank=True)

    def __str__(self):
        return self.innovation_name
