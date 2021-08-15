from django.db import models


class Question(models.Model):
    content = models.CharField(max_length=255, verbose_name="質問文")


class Choice(models.Model):
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    content = models.CharField(max_length=255, verbose_name="選択肢")
