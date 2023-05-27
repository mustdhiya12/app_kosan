from django.db import models

# Create your models here.
class user(models.Model):
    NIK = models.CharField(max_length=120, primary_key=True)
    username = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=100)
    alamat = models.TextField()
    phone_num = models.CharField(max_length=14)
    room = models.CharField(max_length=4)
    is_verified = models.BooleanField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

class transaction(models.Model):
    tr_id = models.CharField(max_length=120, primary_key=True)
    NIK = models.CharField(max_length=120)
    total = models.BigIntegerField()
    start_date = models.DateTimeField()

    JENIS_TRANSACTION = [
        ("C", "Cash"),
        ("R", "Credit"),
        ("W", "E-Wallet"),
    ]
    jenis_transaction = models.CharField(max_length=1 , choices=JENIS_TRANSACTION)
