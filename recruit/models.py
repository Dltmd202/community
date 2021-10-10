from django.db import models
from django.contrib.auth.models import User as usr
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Estimate(models.Model):
    timeframe = models.CharField(max_length=10)
    converted_months = models.DateTimeField()

    def __str__(self):
        return self.timeframe


class Tag_Type(models.Model):
    type = models.CharField(max_length=10)


class Tag(models.Model):
    name = models.CharField(max_length=10)
    color = models.CharField(max_length=7, default="FFFFFF")
    tag_type = models.ForeignKey(Tag_Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class User(models.Model):
    user_id = models.CharField(max_length=50, unique=True)
    user_name = models.CharField(max_length=50)
    nick_name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100,  unique=True)
    # picture = models.ImageField(upload_to='')

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'


class Project(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False, 
        related_name="manager")
    member = models.ManyToManyField(usr)
    estimate = models.ForeignKey(Estimate, on_delete=models.SET_NULL, blank=False, null=True)
    tag = models.ManyToManyField(Tag)

    title = models.CharField(max_length=100)
    written_date = models.DateTimeField(auto_now=True, blank=False, null=False)
    max_recruit = models.PositiveIntegerField(blank=False, null=False,
        validators=[MinValueValidator(1), MaxValueValidator(100)])
    description = models.TextField(max_length=2000, blank=False, null=False)
    is_finished = models.BooleanField(blank=False, null=False, default=False)
    question_list_json = models.TextField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.title + " (팀장: {})".format(self.manager)


class Application(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    form_data_json = models.TextField()