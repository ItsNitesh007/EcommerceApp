from django.forms import ModelForm
from django import forms
from . import models


class userMasterForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = models.userMaster
        fields = "__all__"


class register(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = models.userMaster
        exclude = ["userType"]


class userProfileForm(ModelForm):
    class Meta:
        model = models.userProfile
        exclude = ["userId"]


class productCategoryForm(ModelForm):
    class Meta:
        model = models.productCategory
        labels = {
            'pcId': 'Product Category ID',
            'pcName': 'Category Name',
        }
        fields = "__all__"


class productForm(ModelForm):
    class Meta:
        model = models.product
        labels = {
            'pId': 'Product ID:',
            'pName': 'Product Name:',
            'pDesc': 'Description:',
            'price': 'Price:',
            'discount': 'Discount(%):',
            'pcId': 'Product Category ID:'
        }
        fields = "__all__"


class orderMasterForm(ModelForm):
    class Meta:
        model = models.orderMaster
        fields = "__all__"


class orderDetailsForm(ModelForm):
    class Meta:
        model = models.orderDetails
        fields = "__all__"


class complaintForm(ModelForm):
    compDesc = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 7, 'cols': 40}))

    class Meta:
        model = models.complaint
        labels = {
            'compId': 'Complaint ID:',
            'compDesc': 'Complaint Description',
            'compDate': 'Date',
            'status': 'Status',
            'userId': 'User Id',
            'response': 'Response'
        }
        fields = '__all__'
