from django.db.models import fields


from rest_framework.serializers import ModelSerializer
from comentarios.models import Comentario


class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = "__all__"
