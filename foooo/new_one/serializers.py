from rest_framework import serializers
from .models import MyUser


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = "__all__"


class MyUserSimpleSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    #
    # class Meta:
    #     model = MyUser
    #     fields = ["first_name", "last_name"]
