from rest_framework import serializers
from .models import Domain, Certificate
# from .models import Certificate
from .models import Brand, Model, Series, Category, Inventory


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


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'country', 'active', 'created_at', 'updated_at']


class ModelSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)  # Incluimos información de la marca asociada

    class Meta:
        model = Model
        fields = ['id', 'name', 'brand', 'active', 'created_at', 'updated_at']



class SeriesSerializer(serializers.ModelSerializer):
    model = ModelSerializer(read_only=True)  # Incluimos información del modelo asociado
    brand = BrandSerializer(read_only=True)  # Incluimos información de la marca asociada

    class Meta:
        model = Series
        fields = ['id', 'name', 'model', 'brand', 'active', 'created_at', 'updated_at']



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'active', 'created_at', 'updated_at']



# class InventorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Inventory
#         fields = ['id', 'batch_code', 'series', 'model', 'brand', 'category', 'quantity', 'date_added', 'active']

#     def create(self, validated_data):
#         series = validated_data.pop('series')
#         model = validated_data.pop('model')
#         brand = validated_data.pop('brand')
#         category = validated_data.pop('category')

#         inventory = Inventory.objects.create(
#             series=series,
#             model=model,
#             brand=brand,
#             category=category,
#             **validated_data
#         )
#         return inventory

class InventorySerializer(serializers.ModelSerializer):
    series = serializers.PrimaryKeyRelatedField(queryset=Series.objects.all())
    model = serializers.PrimaryKeyRelatedField(queryset=Model.objects.all())
    brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Inventory
        fields = ['id', 'batch_code', 'series', 'model', 'brand', 'category', 'quantity', 'status', 'date_added', 'active']

    def create(self, validated_data):
        inventory = Inventory.objects.create(**validated_data)
        return inventory
