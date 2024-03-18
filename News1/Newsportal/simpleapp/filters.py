from django import forms
from django_filters import FilterSet, DateFilter, CharFilter, ModelChoiceFilter
from .models import Post, Category


class NewFilter(FilterSet):
    date_after = DateFilter(field_name='created_at', lookup_expr='gte', input_formats=['%Y-%m-%d'],
                            widget=forms.DateInput(attrs={'type': 'date'}))
    title = CharFilter(field_name='title', lookup_expr='icontains')
    category = ModelChoiceFilter(queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ['title', 'category', 'date_after']