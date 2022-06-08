from asyncore import write
from rest_framework import serializers
from .models import Adocao
from pet.serializers import PetSerializer
from pet.models import Pet

class AdocaoSerializer(serializers.ModelSerializer):
    pet = PetSerializer(many=False, read_only=True)
    pet_id = serializers.PrimaryKeyRelatedField(
      many=False,
      write_only=True,
      queryset=Pet.objects.all()      
    )

    class Meta:
        model = Adocao
        fields = ('id', 'email', 'valor', 'pet', 'pet_id')
    
    def create(self, validated_data):
        validated_data['pet'] = validated_data.pop('pet_id')
        return super().create(validated_data)

    def validate_valor(self, valor):
        if valor < 0:
            raise serializers.ValidationError("Valor não pode ser negativo")
        return valor