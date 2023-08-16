from . import models, serializers
from rest_framework import generics


class userListView(generics.ListCreateAPIView):
    queryset = models.userMaster.objects.all()
    serializer_class = serializers.UserSerializer


class userDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.userMaster.objects.all()
    serializer_class = serializers.UserSerializer


class UserProfileView(generics.ListCreateAPIView):
    queryset = models.userProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer


class UserProfileDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.userProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer


class pcListView(generics.ListCreateAPIView):
    queryset = models.productCategory.objects.all()
    serializer_class = serializers.PCSerializer


class pcListDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.productCategory.objects.all()
    serializer_class = serializers.PCSerializer


class productsListView(generics.ListCreateAPIView):
    queryset = models.product.objects.all()
    serializer_class = serializers.ProductSerializer


class productsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.product.objects.all()
    serializer_class = serializers.ProductSerializer


class ComplaintListView(generics.ListCreateAPIView):
    queryset = models.complaint.objects.all()
    serializer_class = serializers.ComplaintSerializer


class ComplaintDetailsView(generics.RetrieveUpdateAPIView):
    queryset = models.complaint.objects.all()
    serializer_class = serializers.ComplaintSerializer


class orderListView(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class orderDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
