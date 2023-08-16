import json
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import logout
from . import models, forms
from datetime import datetime
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict


def home(request):
    return render(request, 'homepage.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'loginpage.html')

    def post(self, request):
        uid = request.POST['uid']
        pwd = request.POST['pwd']
        userdata = models.userMaster.objects.filter(
            userId__exact=uid).filter(password__exact=pwd)
        if userdata:
            for dt in userdata:
                request.session['userId'] = dt.userId
                request.session['userType'] = dt.userType
                unm = models.userProfile.objects.get(userId=dt.userId)
                request.session['userName'] = unm.userName
            return redirect('home')
        else:
            HttpResponse("<h1>Invalid Credentials...</h1>")


def logouts(request):
    logout(request)
    return redirect('home')

# regsiter new user


class AddUser(View):
    def get(self, request):
        myform = forms.userMasterForm()
        return render(request, 'adduser.html', {'myform': myform})

    def post(self, request):
        myform = forms.userMasterForm(request.POST)
        if myform.is_valid():
            myform.save()
        return redirect('home')


class showProfile(View):
    def get(self, request):
        myform = forms.userProfileForm()
        return render(request, 'showprofile.html', {'myform': myform})

    def post(self, request):
        myform = forms.userProfileForm(request.POST)
        if myform.is_valid():
            unm = myform.cleaned_data['userName']
            age = myform.cleaned_data['age']
            add = myform.cleaned_data['address']
            mob = myform.cleaned_data['mob']
            email = myform.cleaned_data['email']
            userId = request.session['userId']
            pr = models.userProfile(unm, age, add, mob, email, userId)
            pr.save()
            return redirect('home')


# to show all the users
class showUsers(View):
    def get(self, request):
        userData = models.userMaster.objects.exclude(userType__exact="admin")
        return render(request, 'showuser.html', {'userData': userData})


class userDetailsView(View):
    def get(self, request, id):
        mydata = models.userMaster.objects.get(userId__exact=id)
        return render(request, 'singleuser.html', {'mydata': mydata})

    def post(self, request, id):
        obj = get_object_or_404(models.userMaster, userId=id)
        obj.delete()
        return redirect('showuser')


class addProductCategoryView(View):
    def get(self, request):
        myform = forms.productCategoryForm()
        return render(request, 'addproductcategory.html', {'myform': myform})

    def post(self, request):
        myform = forms.productCategoryForm(request.POST)
        if myform.is_valid():
            myform.save()
        return redirect('showpc')


class showProductCategoryView(View):
    def get(self, request):
        mydata = models.productCategory.objects.all()
        return render(request, 'showproductcategory.html', {'mydata': mydata})


class updatePC(View):
    def get(self, request, id):
        obj = get_object_or_404(models.productCategory, pcId=id)
        myform = forms.productCategoryForm(instance=obj)
        return render(request, 'updatecategory.html', {'myform': myform})

    def post(self, request, id):
        obj = get_object_or_404(models.productCategory, pcId=id)
        myform = forms.productCategoryForm(request.POST, instance=obj)
        if myform.is_valid():
            myform.save()
        return redirect('showpc')


class deletePC(View):
    def get(self, request, id):
        # obj me jo id btayi hai wo leke aao
        obj = get_object_or_404(models.productCategory, pcId=id)
        # myform me obj ka data enter krke lao
        myform = forms.productCategoryForm(instance=obj)
        return render(request, 'removecategory.html', {'myform': myform})

    def post(self, request, id):
        obj = get_object_or_404(models.productCategory, pcId=id)
        obj.delete()
        return redirect('showpc')


class addpro(View):
    def get(self, request):
        # send form to html
        myform = forms.productForm()
        return render(request, 'addpro.html', {'myform': myform})

    def post(self, request):
        # receiving form from HTML
        myform = forms.productForm(request.POST)
        if myform.is_valid():
            myform.save()
        return redirect('showpro')


class updatepro(View):
    def get(self, request, id):
        obj = get_object_or_404(models.product, pId=id)
        myform = forms.productForm(instance=obj)
        return render(request, 'updatepro.html', {'myform': myform})

    def post(self, request, id):
        obj = get_object_or_404(models.product, pId=id)
        myform = forms.productForm(request.POST, instance=obj)
        if myform.is_valid():
            myform.save()
        return redirect('showpro')


class deletepro(View):
    def get(self, request, id):
        obj = get_object_or_404(models.product, pId=id)
        myform = forms.productForm(instance=obj)
        return render(request, 'deletepro.html', {'myform': myform})

    def post(self, request, id):
        obj = get_object_or_404(models.product, pId=id)
        obj.delete()
        return redirect('showpro')


def showpro(request):
    mydata = models.product.objects.all()
    return render(request, 'showpro.html', {'mydata': mydata})


def showComp(request):
    mydata = models.complaint.objects.all()
    return render(request, 'showcomp.html', {'mydata': mydata})


class addCompView(View):
    def get(self, request):
        myform = forms.complaintForm()
        return render(request, 'addcomp.html', {'myform': myform})

    def post(self, request):
        try:
            compId = models.complaint.objects.order_by('-compId')[0].compId
            print('Complaint Id is ', compId)
        except:
            compId = 0
        compDesc = request.POST['compDesc']
        compDate = datetime.today().date()
        status = 'Open'
        response = ""
        userId = request.session['userId']
        obj = models.complaint(compId+1, compDesc, compDate,
                               status, response, userId)
        obj.save()
        return redirect('showcomp')


class ResponseView(View):
    def get(self, request, id):
        mydata = models.complaint.objects.get(compId=id)
        return render(request, 'response.html', {'mydata': mydata})

    def post(self, request, id):
        obj = models.complaint.objects.get(compId=id)
        response = request.POST['response']
        obj.response = response
        obj.save()
        return redirect('showcomp')


class ShopNowView(View):
    prolist = []

    def get(self, request):
        pcdata = models.productCategory.objects.all()
        return render(request, 'shopnow.html', {'mydata': pcdata})

    def post(self, request):
        pId = request.POST['proid']
        self.prolist.append(pId)
        request.session['mycart'] = self.prolist
        return redirect(home)


def showProlist(request):
    pcdata = models.productCategory.objects.get(pcId=request.GET['id'])
    # print('product category is', pcdata)
    products = models.product.objects.filter(pcId=pcdata.pcId)
    # print('products are \n', products)
    mydata = []
    for pro in products:
        mydata.append(pro.get_pro())
    # print('mydata value is', mydata)
    # it is same as JSON.stringify()
    data = json.dumps(mydata, cls=DjangoJSONEncoder)
    return HttpResponse(data)


class showCart(View):
    def get(self, request):
        cart = request.session['mycart']
        mydata = []
        for i in cart:
            prodata = models.product.objects.get(pId__exact=i)
            mydata.append(prodata)
        return render(request, 'showcart.html', {'mydata': mydata})

    def post(self, request):
        userId = request.session['userId']
        userId1 = models.userMaster.objects.get(userId__exact=userId)
        proIds = request.POST.getlist('chk')
        for i in proIds:
            print("product Id is ", i)
            prodata = models.product.objects.get(pId=i)
            obj = models.Order(pId=prodata, userId=userId1)
            obj.save()
            request.session['mycart'].remove(i)
            request.session.modified = True
        return redirect('home')


def delCart(request, id):
    request.session['mycart'].remove(id)
    request.session.modified = True
    return redirect('cart')


class showOrders(View):
    def get(self, request):
        userId = request.session['userId']
        mydata = models.Order.objects.filter(userId__exact=userId)
        price = []
        for items in mydata:
            netprice = items.pId.price - \
                ((items.pId.price*items.pId.discount)/100)
            price.append(netprice)
        total = sum(price)
        return render(request, 'showorder.html', {'mydata': mydata, 'total': total})
        # return render(request, 'showorder.html',)

    def post(self, request):
        return render(request, 'payment.html')
