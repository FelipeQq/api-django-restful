from django.db.models import query
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ("nome", "descricao", "^endereco__linha1")

    def get_queryset(self):
        id = self.request.query_params.get("id", None)
        nome = self.request.query_params.get("nome__iexact", None)
        descricao = self.request.query_params.get("descricao__iexact", None)

        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(id=id)

        if nome:
            queryset = queryset.filter(nome=nome)

        if descricao:
            queryset = queryset.filter(descricao=descricao)

        return queryset
