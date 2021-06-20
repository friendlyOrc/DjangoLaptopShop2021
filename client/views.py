from __future__ import unicode_literals
from django.shortcuts import redirect, render
from .models import Comment, Fullname, Address, OrderProduct, Shipment, User, Attribute, Category, Rating, Product, Order, Payment

from datetime import datetime

def index(request):
    num_Cate = Category.objects.all().count()
    cate = Category.objects.all()

    prod = Product.objects.all()

    userId = request.session.get('user', -1)
    orderId = request.session.get('order', -1)
    logged = True;
    user = User()
    order = Order()
    num_item = 0

    if userId == -1:
        logged = False
    else:
        user = User.objects.filter(id = userId)[0]
        order = Order.objects.filter(id = orderId)[0]
        num_item = len(OrderProduct.objects.filter(order=order))
    context = {
        'numCate': num_Cate,
        'cate': cate,
        'prod': prod,
        'logged': logged,
        'user': user,
        'order': order,
        'num_item': num_item
    }

    return render(request, 'index.html', context=context)

def login(request):
    if request.method == 'GET':
    
        return render(request, 'login.html')
    
    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']
        user = User.objects.filter(username=un, password=pw)


        if len(user) == 1:
            
            request.session['user'] = user[0].id

            order = Order.objects.filter(status = 0, client=user[0])

            if len(order) == 0:
                order = Order(client = user[0])
                order.save()
            else:
                order = order[0]
            request.session['order'] = order.id
            
            return redirect('/')
        else:
            context = {
                'fail': True
            }
            return render(request, 'login.html', context=context)
def signup(request):
    if request.method == 'GET':
    
        return render(request, 'signup.html')
    
    if request.method == 'POST':
        fname = request.POST['fname']
        mname = request.POST['mname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        des = request.POST['des']
        ward = request.POST['ward']
        road = request.POST['road']
        province = request.POST['province']
        city = request.POST['city']
        un = request.POST['username']
        pw = request.POST['password']

        user = User.objects.filter(username=un)
        if len(user) > 0:
            context = {
                'dup': True
            }
            return render(request, 'signup.html', context=context)
        else:
            name = Fullname(fName=fname, mName=mname, lName=lname)
            name.save()
            print(name.id)
            addr = Address(des=des, ward=ward, road=road, province=province, city=city)
            addr.save()
            user = User(name=name, addr=addr, email=email, phone=phone, username=un, password=pw)
            user.save()
            context = {
                'signup': True
            }
            return render(request, 'login.html', context=context)
        
        
def logout(request):
    
    request.session.flush()

    return redirect('/')

def prdDetail(request, pk):
    rs = request.GET.get('msg', '')

    prod = Product.objects.filter(id=pk)[0]

    print(prod.rate)
    prod.rate = Rating.objects.filter(id = prod.rate.id)[0]
    attrs = Attribute.objects.filter(rate=prod.rate)
    comment = Comment.objects.filter(prod=prod)

    userId = request.session.get('user', -1)
    orderId = request.session.get('order', -1)
    logged = True;
    user = User()
    order = Order()
    num_item = 0

    if userId == -1:
        logged = False
    else:
        user = User.objects.filter(id = userId)[0]
        order = Order.objects.filter(id = orderId)[0]
        num_item = len(OrderProduct.objects.filter(order=order))
    msg = False
    if rs == 'succ':
        msg = True
    context = {
        'prod': prod,
        'attrs': attrs,
        'coms': comment,
        'logged': logged,
        'user': user,
        'order': order,
        'num_item': num_item,
        'msg': msg
    }

    return render(request, 'singleproduct.html', context=context)

def prdList(request, pk):

    cat = Category.objects.filter(id=pk)[0]
    prod = Product.objects.filter(category=cat)

    userId = request.session.get('user', -1)
    orderId = request.session.get('order', -1)
    logged = True;
    user = User()
    order = Order()
    num_item = 0

    if userId == -1:
        logged = False
    else:
        user = User.objects.filter(id = userId)[0]
        order = Order.objects.filter(id = orderId)[0]
        num_item = len(OrderProduct.objects.filter(order=order))
    context = {
        'cat': cat,
        'prod': prod,
        
        'logged': logged,
        'user': user,
        'order': order,
        'num_item': num_item
    }

    return render(request, 'productlist.html', context=context)

def search(request):
    if request.method == 'POST':
        key = request.POST['search']
        print(key)
        prod = []
        prod = Product.objects.filter(name__contains=key)
        
        userId = request.session.get('user', -1)
        orderId = request.session.get('order', -1)
        logged = True;
        user = User()
        order = Order()
        num_item = 0

        if userId == -1:
            logged = False
        else:
            user = User.objects.filter(id = userId)[0]
            order = Order.objects.filter(id = orderId)[0]
            num_item = len(OrderProduct.objects.filter(order=order))
        context = {
            'key': key,
            'prod': prod,
            
            'logged': logged,
            'user': user,
            'order': order,
            'num_item': num_item
        }
    return render(request, 'searchrs.html', context=context)

def cart(request):
    if request.method == 'GET':
        rs = request.GET.get('msg', '')

        userId = request.session.get('user', -1)
        orderId = request.session.get('order', -1)
        logged = True;
        user = User()
        order = Order()
        num_item = 0

        if userId == -1:
            logged = False
        else:
            user = User.objects.filter(id = userId)[0]
            order = Order.objects.filter(id = orderId)[0]
            num_item = len(OrderProduct.objects.filter(order=order))

            opList = OrderProduct.objects.filter(order = order)

        msg = False
        delete = False
        ordered = False
        if rs == 'succ':
            msg = True
        elif rs == 'del':
            delete = True
        elif rs == 'ordered':
            ordered = True
        context = {
            'logged': logged,
            'user': user,
            'order': order,
            'num_item': num_item,
            'prdList': opList,
            'msg': msg,
            'del': delete,
            'ord': ordered
        }

        return render(request, 'cart.html', context=context)
    
    if request.method == 'POST':

        userId = request.session.get('user', -1)
        orderId = request.session.get('order', -1)
        logged = True;
        user = User()
        order = Order()
        num_item = 0
        total = 0

        if userId == -1:
            logged = False
            return redirect('/')
        else:
            user = User.objects.filter(id = userId)[0]
            order = Order.objects.filter(id = orderId)[0]
            num_item = len(OrderProduct.objects.filter(order=order))

            opList = OrderProduct.objects.filter(order = order)
            for prd in opList:
                total += prd.total

            des = request.POST['des']
            ward = request.POST['ward']
            road = request.POST['road']
            province = request.POST['province']
            city = request.POST['city']
            addr = Address(des=des, ward=ward, road=road, province=province, city=city)
            addr.save()
            speed = request.POST['speed']
            note = request.POST['note']
            ship = Shipment(speed = speed, note = note, addr = addr)
            ship.save()
            if speed == 1:
                total += 30000
            else: 
                total += 15000
            

            type = request.POST['payment_type']
            bank = request.POST['bank']
            if type == 1:
                bank = 'COD'
            payment = Payment(type = type, bank = bank, total = total)
            payment.save()

            order.createDate = datetime.now()
            order.total = total
            order.status = 1
            order.pay = payment
            order.ship = ship

            order.save()

            
            new_order = Order(client = user)
            new_order.save()
            request.session['order'] = new_order.id

            return redirect('/orders?msg=ordered')

def cart_add(request, pk):
    
    userId = request.session.get('user', -1)
    orderId = request.session.get('order', -1)
    order = Order()

    if userId == -1:
        logged = False
        return redirect('/')
    else:
        amount = request.POST['amount']
        order = Order.objects.filter(id = orderId)[0]

        prod = Product.objects.filter(id = pk)[0]

        num_item1 = len(OrderProduct.objects.filter(order=order))
        msg = 'fail'
        op = OrderProduct.objects.filter(order = order, prod = prod)
        if len(op) > 0:
            op = op[0]
            op.quanity = op.quanity + int(amount)
            op.total = op.quanity * op.prod.price
            op.save()

            msg = 'succ'
        else:

            ordPrd = OrderProduct(prod = prod, order = order, quanity = amount, total = prod.price)
            ordPrd.save()

            num_item2 = len(OrderProduct.objects.filter(order=order))
            if num_item2 > num_item1:
                msg = 'succ'
    
    return redirect('/product/'+ str(pk) + '?msg=' + msg)

def cart_update(request, pk):
    
    userId = request.session.get('user', -1)

    if userId == -1:
        logged = False
        return redirect('/')
    else:
        msg = 'Fail'
        amount = request.POST['amount']
        op = OrderProduct.objects.filter(id = pk)
        if len(op) > 0:
            op = op[0]
            op.quanity = int(amount)
            op.total = op.quanity * op.prod.price
            op.save()

            msg = 'succ'
    
    return redirect('/cart?msg=' + msg)
def cart_remove(request, pk):
    
    userId = request.session.get('user', -1)

    if userId == -1:
        logged = False
        return redirect('/')
    else:
        msg = 'Fail'
        op = OrderProduct.objects.filter(id = pk)
        if len(op) > 0:
            op = op.delete()

            msg = 'del'
    
    return redirect('/cart?msg=' + msg)

def orderList(request):
    
    rs = request.GET.get('msg', '')

    userId = request.session.get('user', -1)
    orderId = request.session.get('order', -1)
    logged = True;
    user = User()
    order = Order()
    num_item = 0

    if userId == -1:
        logged = False
    else:
        user = User.objects.filter(id = userId)[0]
        order = Order.objects.filter(id = orderId)[0]
        num_item = len(OrderProduct.objects.filter(order=order))

        orderList = Order.objects.filter(client = user)

    ord = False
    if rs == 'ordered':
        msg = True
    context = {
        'logged': logged,
        'user': user,
        'order': order,
        'num_item': num_item,
        'ord': ord,
        'orderList': orderList
    }

    return render(request, 'orderlist.html', context=context)

def comment(request, pk):
    
    rs = request.GET.get('msg', '')

    userId = request.session.get('user', -1)
    orderId = request.session.get('order', -1)
    logged = True;
    user = User()
    order = Order()
    num_item = 0

    if userId == -1:
        logged = False
    else:
        user = User.objects.filter(id = userId)[0]
        order = Order.objects.filter(id = orderId)[0]
        num_item = len(OrderProduct.objects.filter(order=order))

        prod = Product.objects.filter(id = pk)[0]

        content = request.POST['review']

        cmt = Comment(createDate = datetime.now(), content = content, prod = prod, client = user)
        cmt.save()

    cmt = False
    if rs == 'cmt':
        msg = True
    context = {
        'logged': logged,
        'user': user,
        'order': order,
        'num_item': num_item,
        'ord': ord,
        'orderList': orderList
    }

    return redirect('/product/' + str(pk) + '?msg=cmt')