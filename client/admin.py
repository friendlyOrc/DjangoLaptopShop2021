from django.contrib import admin
from .models import Fullname, Address, User, Attribute, Category, Rating, Product, Comment, Reply, Shipment, Payment, Order, OrderProduct

# Register your models here.
admin.site.register(Fullname)
admin.site.register(Address)
admin.site.register(User)
admin.site.register(Attribute)
admin.site.register(Category)
admin.site.register(Rating)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Shipment)