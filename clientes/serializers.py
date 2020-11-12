from rest_framework import serializers
from clientes.models import Cliente
import re
from validate_docbr import CPF

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate_cpf(self,cpf):
        cpf1 = CPF()
        if not cpf1.validate(cpf):
            raise serializers.ValidationError("CPF INVALIDO")
        return cpf
    
    def validate_nome(self,nome):
        if not nome.isalpha():
            raise serializers.ValidationError("Não inclua numeros neste campo ")
        return nome
    
    def validate_rg(self,rg):
        if len(rg) != 9:
            raise serializers.ValidationError("o RG deve ter 9 digitos")
        return rg
    
    def Validate_celular(self,celular):
        """Verifica se o celular é valido"""
        modelo ='[0-9]{2} [0-9]{5}-[0-9}{4}'
        if not re.match(modelo,celular):
            raise serializers.ValidationError("O celular deve ter no minimo 11 digitos")
        return celular