from rest_framework import serializers
from essence_web_app.models import Item, Brand, Category, SubCategory


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(read_only=True)
    subcategory = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Item
        fields = ('url', 'id', 'name', 'description', 'price', 'brand', 'category', 'subcategory')


class BrandSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Brand
        fields = ('url', 'id', 'name')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    subcategories = serializers.PrimaryKeyRelatedField(many=True, queryset=SubCategory.objects.all())

    class Meta:
        model = Category
        fields = ('url', 'id', 'name')


class SubCategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SubCategory
        fields = ('url', 'id', 'name')