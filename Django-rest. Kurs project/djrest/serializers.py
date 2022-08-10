from rest_framework import serializers
from djrest.models import *

class kursSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = kurs
        fields = '__all__'
