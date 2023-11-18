from rest_framework import serializers
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 


class UserGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'name', 'description', 'creation_time']


class UserPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'description']
        read_only_fields = ['username']
