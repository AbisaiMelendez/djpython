from rest_framework import serializers
from .models import Domain, Certificate
from .models import Certificate

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        #fields = ('campouno', 'campodos')
        fields = '__all__'
        
    
class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'
        
        

# class DomainSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Domain
#         fields = '__all__'