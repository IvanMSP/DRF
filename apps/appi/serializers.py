from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Producto
from django.contrib.auth.models import User



class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

# from appi.serializers import ProductoSerializer
# from appi.models import Producto

# prod_serializer = ProductoSerializer(data={"subcategoria":1,"descripcion":"Desarrollo Web con Python usando Django 1.1","fecha_creado":"2018-10-01T12:11:37.090335Z"})
# prod_serializer.is_valid()
# prod1 = prod_serializer.save()
# prod1.pk