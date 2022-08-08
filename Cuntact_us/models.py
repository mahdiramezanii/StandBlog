from django.db import models



class Message(models.Model):

    titel=models.CharField(max_length=100)
    text=models.TextField()
    email=models.EmailField()
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return self.titel


    class Meta:
        verbose_name="پیام"
        verbose_name_plural="پیام ها"
