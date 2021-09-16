from django.db import models


# Create your models here.
class Application(models.Model):
    # project_id = models.ForeignKey(Project)
    # user_id = models.ForeignKey(User)
    from_data_json = models.TextField()


class Estimate(models.Model):
    timeframe = models.CharField(max_length=10)
    converted_months = models.DateTimeField()


class Tag_Type(models.Model):
    type = models.CharField(max_length=10)


class Tag(models.Model):
    name = models.CharField(max_length=10)
    color = models.CharField(default="FFFFFF")
    tag_type = models.ForeignKey(Tag_Type)