# -*- coding: utf-8 -*-



from rest_framework import serializers
from models import books

class HomeBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = books
        # fields = ("id",)
        fields = '__all__'