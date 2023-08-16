from django.urls import path, include
from . import views, views2


urlpatterns = [
    # url for Homepage
    path('', views.home),
    path('home', views.home, name='home'),
    # userManagement paths
    path('logins', views.LoginView.as_view(), name='logins'),
    path('adduser', views.AddUser.as_view(), name='adduser'),
    path('showprofile', views.showProfile.as_view(), name='showprofile'),
    path('showuser', views.showUsers.as_view(), name='showuser'),
    path('logouts', views.logouts, name='logouts'),
    path('userdetails/<id>', views.userDetailsView.as_view(), name='userdetails'),
    # Product Category Urls
    path('addpc', views.addProductCategoryView.as_view(), name='addpc'),
    path('showpc', views.showProductCategoryView.as_view(), name='showpc'),
    path('updatepc/<id>', views.updatePC.as_view(), name='updatepc'),
    path('removepc/<id>', views.deletePC.as_view(), name='removepc'),
    # Products urls
    path('addpro', views.addpro.as_view(), name='addpro'),
    path('updatepro/<id>', views.updatepro.as_view(), name='updatepro'),
    path('deletepro/<id>', views.deletepro.as_view(), name='deletepro'),
    path('showpro', views.showpro, name='showpro'),
    # complaint urls
    path('addcomp', views.addCompView.as_view(), name='addcomp'),
    path('showcomp', views.showComp, name='showcomp'),
    path('response/<id>', views.ResponseView.as_view(), name='response'),
    # Buyer related
    path('shopnow', views.ShopNowView.as_view(), name='shopnow'),
    path('prolist', views.showProlist, name='prolist'),
    path('cart', views.showCart.as_view(), name='cart'),
    path('delcart/<id>', views.delCart, name='delcart'),
    path('orders', views.showOrders.as_view(), name='orders'),
    # API urls
    path('apiuserlist', views2.userListView.as_view()),
    path('apiuserlist/<pk>', views2.userDetailsView.as_view()),
    path('apiprofile', views2.UserProfileView.as_view()),
    path('apiprofile/<pk>', views2.UserProfileDetailsView.as_view()),
    path('apipc', views2.pcListView.as_view()),
    path('apipc/<pk>', views2.pcListDetailsView.as_view()),
    path('apiproducts', views2.productsListView.as_view()),
    path('apiproducts/<int:pk>', views2.productsDetailView.as_view()),
    path('apicomplaint', views2.ComplaintListView.as_view()),
    path('apicomplaint/<int:pk>', views2.ComplaintDetailsView.as_view()),
    path('apiorder', views2.orderListView.as_view()),
    path('apiorder/<int:pk>', views2.orderDetailsView.as_view()),
]
