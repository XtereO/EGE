from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import (QuestionSerializer,
    NumberDetailSerializer,
    VariantSerializer,
    VariantDetailSerializer,
    MaterialSerializer,
    ItemSerializer
    )
from ..models import (
    Question,Number,
    Variant,Material,
    Item
    )

class PaginationForQuestion(PageNumberPagination):
    page_size=5
    page_size_query_param='page_size'
    max_page_size=float('inf')

class QuestionView(ListAPIView):

    serializer_class=QuestionSerializer
    queryset=Question.objects.all()
    pagination_class=PaginationForQuestion

    def get_queryset(self):
        qs=super().get_queryset()

        category=self.request.query_params.get('category')
        if category:
            qs=qs.filter(categorys__id__iexact=category)

        number=self.request.query_params.get('number')
        if number:
            qs=qs.filter(number__number__iexact=number)

        qs=qs.order_by('-id')

        sort_by_difficult=self.request.query_params.get('sort_difficult')
        #true - easy , false - hard
        if sort_by_difficult and (sort_by_difficult=="true" or sort_by_difficult=="True"):
            qs=qs.order_by('difficult')
        elif sort_by_difficult=="false" or sort_by_difficult=="False":
            qs=qs.order_by('-difficult')

        randomize=self.request.query_params.get('randomize')
        if randomize:
            qs=qs.order_by('?')

        return qs


class QuestionDetailView(APIView):

    def get(self,request):
        ID=request.query_params.get('id')
        return Response(QuestionSerializer(Question.objects.get(id__iexact=ID)).data)

class MaterialView(APIView):

    def get(self,request):
        ID=request.query_params.get('id')
        return Response(MaterialSerializer(Material.objects.get(id__iexact=ID)).data)

class NumberView(ListAPIView):

    serializer_class=NumberDetailSerializer
    queryset=Number.objects.all()

    def get_queryset(self):
        qs=super().get_queryset()
        item=self.request.query_params.get('item')
        if item:
            qs=qs.filter(item__id__iexact=item)
        return qs.order_by("number")

class VariantView(ListAPIView):

    serializer_class=VariantSerializer
    queryset=Variant.objects.all()
    pagination_class=PaginationForQuestion
    def get_queryset(self):
        qs=super().get_queryset()
        item=self.request.query_params.get('item')
        if item:
            qs=qs.filter(item__id__iexact=item)

        qs=qs.order_by('-variantNumber')
        return qs


class VariantDetailView(APIView):

    def get(self,request):
        ID=request.query_params.get('id')
        return Response(VariantDetailSerializer(Variant.objects.get(variantNumber__iexact=ID)).data)

class ItemView(ListAPIView):
    
    serializer_class=ItemSerializer
    queryset=Item.objects.all()