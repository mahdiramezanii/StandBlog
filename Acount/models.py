from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    fiestname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    fathername=models.CharField(max_length=50)
    nation_code=models.CharField(max_length=10)
    image=models.FileField(upload_to="Acount/profile/img",blank=True,null=True)


    def __str__(self):
        return self.fiestname


    class Meta:
        verbose_name="حساب کاربری"
        verbose_name_plural="حساب های کاربری"

