from django.db import models

# Create your models here.





class registerPage(models.Model):
    Accno = models.IntegerField(primary_key=True)
    Balance = models.FloatField()
    #Name = models.CharField(max_length=200)
    class Meta:
        db_table = 'account'
