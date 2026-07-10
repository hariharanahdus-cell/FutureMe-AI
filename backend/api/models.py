from django.db import models



class FuturePrediction(models.Model):

    name = models.CharField(
        max_length=100
    )


    age = models.IntegerField()


    goal = models.CharField(
        max_length=200
    )


    skills = models.TextField()


    prediction = models.TextField()


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.name