from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.userMaster
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.userProfile
        fields = '__all__'


class PCSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.productCategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.product
        fields = '__all__'


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.complaint
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'
