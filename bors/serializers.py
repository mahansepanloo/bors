from rest_framework.serializers import ModelSerializer
from .models import Investment

class Karbarserialazers(ModelSerializer):
    class Meta:
        model = Investment
        fields = "__all__"

