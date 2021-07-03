from rest_framework import serializers
from ..models import (
    Question,Variant,
    Number,Category,
    Benchmark,Material,
    Item)


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        fields="__all__"
        model=Item

class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        fields="__all__"
        model=Material

class CategorySerializer(serializers.ModelSerializer):

    material=MaterialSerializer()

    class Meta:
        fields="__all__"
        model=Category

class BenchmarkSerializer(serializers.ModelSerializer):

    class Meta:
        fields="__all__"
        model=Benchmark

class NumberDetailSerializer(serializers.ModelSerializer):

    categorys=CategorySerializer(many=True)
    benchmarks=BenchmarkSerializer(many=True)

    class Meta:
        fields="__all__"
        model=Number

class NumberSerializer(serializers.ModelSerializer):

    class Meta:
        fields="__all__"
        model=Number

class QuestionSerializer(serializers.ModelSerializer):

    number=NumberDetailSerializer()
    categorys=CategorySerializer()

    class Meta:
        fields="__all__"
        model=Question

class QuestionForVariantSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=Question

class VariantSerializer(serializers.ModelSerializer):

    class Meta:
        fields="__all__"
        model=Variant

class VariantDetailSerializer(serializers.ModelSerializer):

    questions=QuestionSerializer(many=True)

    class Meta:
        fields="__all__"
        model=Variant
