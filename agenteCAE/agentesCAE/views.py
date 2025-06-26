from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AgenteCAE
from .serializers import AgenteCAESerializer

class AgenteCAEAPIView(APIView):
    # LISTAR TODOS OS AGENTES CAE (GET)
    def get(self, request):
        agentes = AgenteCAE.objects.all()
        serializer = AgenteCAESerializer(agentes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # CRIAR UM NOVO AGENTE CAE (POST)
    def post(self, request):
        serializer = AgenteCAESerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AgenteCAEDetalheAPIView(APIView):
    # BUSCAR UM AGENTE CAE ESPECÍFICO (GET)
    def get(self, request, pk):
        try:
            agente = AgenteCAE.objects.get(matricula_agente=pk)  # Usando matrícula como chave
            serializer = AgenteCAESerializer(agente)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except AgenteCAE.DoesNotExist:
            return Response(
                {"erro": "Agente CAE não encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )

    # ATUALIZAR AGENTE CAE (PUT)
    def put(self, request, pk):
        try:
            agente = AgenteCAE.objects.get(matricula_agente=pk)
            serializer = AgenteCAESerializer(agente, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except AgenteCAE.DoesNotExist:
            return Response(
                {"erro": "Agente CAE não encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )

    # DELETAR AGENTE CAE (DELETE)
    def delete(self, request, pk):
        try:
            agente = AgenteCAE.objects.get(matricula_agente=pk)
            agente.delete()
            return Response(
                {"mensagem": "Agente CAE excluído com sucesso"},
                status=status.HTTP_204_NO_CONTENT
            )
        except AgenteCAE.DoesNotExist:
            return Response(
                {"erro": "Agente CAE não encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )