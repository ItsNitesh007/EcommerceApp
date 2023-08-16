from django.db import models
import datetime

# Create your models here.

'''
=============================================
Database:
=============
1) UserMaster(userId(pk), password,usertype[buyer/seller]

2) UserProfile(FullName, mobile, email, gender, location, optional= [dob,alternate mobile, alternate email])

3) Product_Category
Discount, Exchange (Boolean), EMI, options: (Default=Others, choices=Others, Electronics, Fashion, Sports, Collectibles and Art, Health, Furniture, Grocery, Appliances)

4) Product (Product ID(pk), name, category(fk), sellerID, brandName, price, description, reviews & ratings(fk - complaint & Feedback) )

5) complaint & Feedback (complaintID(pk), Complain_category, userID (fk) description, status, product(fk), productID, product_category

6) Order & Return (OrderID, productID(s), product_name(s), userID(buyer & seller both), totalPrice, optional[Complaint (Return) /Feedback (Orders)])

'''

user_choices = [("Seller", "Seller"), ("Buyer", "Buyer")]


class userMaster(models.Model):
    userId = models.CharField(primary_key=True,  max_length=30)
    password = models.CharField(max_length=30)
    userType = models.CharField(max_length=30, choices=user_choices)

    def __str__(self):
        return self.userType + " - " + self.userId


class userProfile(models.Model):
    userName = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.CharField(max_length=150)
    mob = models.CharField(max_length=10, unique=True)
    email = models.EmailField(primary_key=True)
    userId = models.ForeignKey(userMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.userName+" - "+str(self.userId)+" - "+self.mob+" - "+self.email


class productCategory(models.Model):
    pcId = models.CharField(max_length=30, primary_key=True)
    pcName = models.CharField(max_length=30)

    def __str__(self):
        return self.pcId + " - "+self.pcName


class product(models.Model):
    pId = models.CharField(max_length=30, primary_key=True)
    pName = models.CharField(max_length=30)
    pDesc = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    discount = models.IntegerField()
    pcId = models.ForeignKey(productCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.pName+" - "+str(self.pId)

    def get_pro(self):
        return {
            'pId': self.pId,
            'pName': self.pName,
            'pDesc': self.pDesc,
            'price': self.price,
            'discount': self.discount
        }


class orderMaster(models.Model):
    orderId = models.IntegerField(auto_created=True, primary_key=True)
    orderDate = models.DateField()
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    userId = models.ForeignKey(userMaster, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.orderDate)+" - "+self.userId+" - "+str(self.orderDate)


class orderDetails(models.Model):
    pId = models.ForeignKey(product, on_delete=models.CASCADE)
    qty = models.IntegerField()
    netPrice = models.IntegerField()
    orderId = models.ForeignKey(orderMaster, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.orderId)


class complaint(models.Model):
    compId = models.IntegerField(primary_key=True, auto_created=True)
    compDesc = models.CharField(max_length=1000)
    compDate = models.DateField()
    status = models.CharField(max_length=10, default='Open')
    response = models.CharField(max_length=1000)
    userId = models.ForeignKey(userMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.userId + " - " + str(self.compId)+" - "+str(self.compDate)


class Order(models.Model):
    pId = models.ForeignKey(product, on_delete=models.CASCADE)
    orderDate = models.DateField(default=datetime.date.today)
    userId = models.ForeignKey(userMaster, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pId)+"-"+str(self.orderDate)+"-"+str(self.userId)
