from rest_framework import serializers
from catalog.models import Variation, ImageProduct


class ImageProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProduct
        fields = ('image',)


class VariationSerializer(serializers.ModelSerializer):
    image = ImageProductSerializer(many=True, read_only=True, source='product.images')

    class Meta:
        model = Variation
        fields = ('id', 'name', 'product', 'price', 'stock', 'image')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Variation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.product = validated_data.get('product', instance.product)
        instance.price = validated_data.get('price', instance.price)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.save()
        return instance
