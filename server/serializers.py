from django.contrib.auth.models import User, Group
from rest_framework import serializers


class Restaurant(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"
