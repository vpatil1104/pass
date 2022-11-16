from django.db import models

# Create your models here.
 
class registerPage(models.Model):
    #accounts = accounts
    #print(accounts)
    Accno = models.IntegerField(primary_key=True)
    Balance = models.FloatField()
    usertype = models.FloatField()
    #Name = models.CharField(max_length=200)
    class Meta:
        db_table = 'account'
        
class Wallet(models.Model): 
    uid=models.IntegerField()
    Amount=models.DecimalField(max_digits=15, decimal_places=2)
    balance=models.DecimalField(max_digits=15, decimal_places=2)
    crdr=models.CharField(max_length=5)
    remarks=models.CharField(max_length=500)
    date= models.DateField()

class Send_money(models.Model):
    uid=models.IntegerField()
    username=models.CharField(max_length=122)
    Amount=models.DecimalField(max_digits=15, decimal_places=2)
    balance=models.DecimalField(max_digits=15, decimal_places=2)
    date= models.DateField()
    
class Request_money(models.Model):
    username=models.CharField(max_length=122)
    Amount=models.CharField(max_length=122)
    date= models.DateField()
