from rest_framework import serializers

from .models import User, Part, Type, UserStatus

class UserStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStatus
        fields = ('id', 'name')

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ('id', 'name')

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'name')

class UserSerializer(serializers.ModelSerializer):
    part = PartSerializer(read_only=True)
    type = TypeSerializer(read_only=True)
    status = UserStatusSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'status',
                  'name', 'nickname', 'home_address', 'work_address', 
                  'part', 'type', 'emergency_phone', 'note')
        #read_only_fields = ('status', 'part', 'type')
