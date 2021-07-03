from django.urls import path
from .views import (QuestionView,
    VariantView,
    NumberView,
    VariantDetailView,
    QuestionDetailView,
    MaterialView,
    ItemView
)

urlpatterns = [
    path('questions',QuestionView.as_view()),
    path('numbers',NumberView.as_view()),
    path('variants',VariantView.as_view()),
    path('variant',VariantDetailView.as_view()),
    path('question',QuestionDetailView.as_view()),
    path('material',MaterialView.as_view()),
    path('items',ItemView.as_view()) 
]
