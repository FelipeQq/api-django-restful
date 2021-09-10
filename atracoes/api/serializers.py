from django.db.models import fields

from rest_framework.serializers import ModelSerializer
from atracoes.models import Atracao


class AtracaoSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = "__all__"
