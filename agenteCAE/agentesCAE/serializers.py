from rest_framework import serializers
from .models import AgenteCAE

class AgenteCAESerializer(serializers.ModelSerializer):
    class Meta:
        model = AgenteCAE
        fields = '__all__'
        extra_kwargs = {
            'matricula_agente': {'required': True},
            'cpf_agente': {'required': True},
            'nome_agente': {'required': True},
            'data_nascimento_agente': {'required': True},
        }