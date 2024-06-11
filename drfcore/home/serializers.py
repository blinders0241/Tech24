from rest_framework import serializers
from home.models import NotesModel



class NotesModelSerializers (serializers.ModelSerializer):
    class Meta:
        model = NotesModel
        fields = '__all__'