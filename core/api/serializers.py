from django.db.models import fields
from rest_framework.fields import SerializerMethodField
from core import models


from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(ModelSerializer):

    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = (
            "id",
            "nome",
            "descricao",
            "aprovado",
            "atracoes",
            "comentarios",
            "avaliacoes",
            "endereco",
            "foto",
            "descricao_completa2",
            "descricao_completa",
            "endereco",
            "atracoes",
        )

    def get_descricao_completa(self, obj):
        return "%s - %s" % (obj.nome, obj.descricao)
