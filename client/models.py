from django.db import models
from django.db.models.fields import DateTimeField
from django.db.models.fields.related import ForeignKey
from django.db.models.query_utils import select_related_descend
from django.contrib.postgres.fields import ArrayField
from datetime import datetime
# Create your models here.

class Fullname(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False, default= None)
    fName = models.CharField(max_length=224, null=True, blank=True, default= "")
    mName = models.CharField(max_length=224, null=True, blank=True, default= "")
    lName = models.CharField(max_length=224, null=True, blank=True, default= "")

    def __str__(self):
        return self.fName + " " + self.mName + " " + self.lName
    

class Address(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False, default= None)
    des = models.CharField(max_length=224, null=True, blank=True, default= "")
    road = models.CharField(max_length=224, null=True, blank=True, default= "")
    ward = models.CharField(max_length=224, null=True, blank=True, default= "")
    province = models.CharField(max_length=224, null=True, blank=True, default= "")
    city = models.CharField(max_length=224, null=True, blank=True, default= "")

    def __str__(self):
        return self.des + " " + self.road + " " + self.ward + " " + self.province + " " + self.city

class User(models.Model):
    
    id = models.AutoField(primary_key=True, null=False, blank=False, default=None)
    name = models.OneToOneField('Fullname', on_delete=models.CASCADE, default= "")
    email = models.EmailField(max_length=224, null=False, blank=False, default= "")
    phone = models.CharField(max_length=224, null=False, blank=False, default= "")
    username = models.CharField(max_length=224, null=False, blank=False, default= "")
    password = models.CharField(max_length=224, null=False, blank=False, default= "")
    role = models.IntegerField(null=False, blank=False, default= 0) 
    rank = models.IntegerField(null=False, blank=False, default= 0)
    
    addr = models.OneToOneField('Address', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.username

    def __str__(self):
        return self.username

class Category(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False, default= None)
    name = models.CharField(max_length=224, null=True, blank=True, default= "")
    
    def __str__(self):
        return self.name

class Attribute(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False, default= None)
    name = models.CharField(max_length=224, null=False, blank=False, default= "")
    rate = models.ForeignKey('Rating', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Rating(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False, default= None)

    rate = models.IntegerField(null=False, blank=False, default= 0)
    
    def __str__(self):
        return str(self.id)

class Product(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False, default=None)
    name = models.CharField(max_length=224,  default= "")
    price = models.FloatField(max_length=224,  default= "")
    des = models.CharField(max_length=224,  default= "")
    year = models.IntegerField(null=False, blank=False, default=0)
    screen = models.FloatField(max_length=224,  default= "")
    image = models.CharField(max_length=224,  default= "")
    battery = models.IntegerField(null=False, blank=False, default=0)
    memory = models.FloatField(max_length=224,  default= 0)
    ram = models.IntegerField(null=False, blank=False, default=0)
    os = models.CharField(max_length=224,  default= "")

    rate = models.OneToOneField('Rating', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, )

    def __str__(self):
        return self.name

class Comment(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False, default=None)
    content = models.CharField(max_length=224,  default= "")
    createDate = models.DateTimeField(default=datetime.now())
    like = models.IntegerField(null=False, blank=False, default=0)
    dislike = models.IntegerField(null=False, blank=False, default=0)
    rate = models.IntegerField(null=False, blank=False, default=0)
    prod = models.ForeignKey('Product', on_delete=models.DO_NOTHING)
    client = models.ForeignKey('User', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.prod.name + " - " + self.content

class Reply(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False, default=None)
    content = models.CharField(max_length=224,  default= "")
    createDate = models.DateTimeField(default=datetime.now())
    like = models.IntegerField(null=False, blank=False, default=0)
    dislike = models.IntegerField(null=False, blank=False, default=0)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)
    client = models.ForeignKey('User', on_delete=models.DO_NOTHING)

    def __str__(self):
        return  self.comment.prod.name + " - " + self.content

class Shipment(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False, default=None)
    speed = models.IntegerField(null=False, blank=False, default=0)
    note = models.CharField(max_length=224, null=False, blank=False, default="")
    addr = ForeignKey('Address', on_delete=models.DO_NOTHING)
    
    def __str__(self):
        text = ""
        if self.speed == 1: 
            text = "[Fast]"
        elif self.speed == 2:
            text = "[Mormal]"
        return text + str(self.addr)

class Payment(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False, default=None)
    type = models.IntegerField(null=False, blank=False, default=0)
    bank = models.CharField(max_length=224, null=False, blank=False, default="")
    total = models.FloatField(null=False, blank=False, default=0)

    def __str__(self):
        text = ""
        if self.type == 1: 
            text = "[COD]"
        elif self.type == 2:
            text = "[Chờ xác nhận]"
        return text + " - " + str(self.bank)

class Order(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False, default=None)
    createDate = models.DateTimeField(default=datetime.now())
    total = models.FloatField(null=False, blank=False, default=0)
    sale = models.FloatField(null=False, blank=False, default=0)
    status = models.IntegerField(null=False, blank=False, default=0)
    pay = models.OneToOneField('Payment', on_delete=models.CASCADE, null=True,)
    ship = models.OneToOneField('Shipment', on_delete=models.CASCADE, null=True,)
    client = models.ForeignKey('User', on_delete=models.DO_NOTHING)

    note = models.CharField(max_length=224, null=True, blank=True, default="")

    def __str__(self):
        text = ""
        if self.status == 0: 
            text = "[Chưa đặt]"
        elif self.status == 1:
            text = "[Chờ xác nhận]"
        elif self.status == 2:
            text = "[Đã xác nhận]"
        else:
            # status == 1
            text = "[Huỷ]"
        return text + " - " + str(self.createDate) + " - " + str(self.client.name)

class OrderProduct(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False, default=None)
    quanity = models.IntegerField(null=False, blank=False, default=0)
    sale = models.FloatField(null=False, blank=False, default=0)
    prod = models.ForeignKey('Product', on_delete=models.DO_NOTHING)
    order = models.ForeignKey('Order', on_delete=models.DO_NOTHING)
    total = models.FloatField(null=False, blank=False, default=0)

    def __str__(self):
        return self.prod.name + " - " + str(self.quanity)




