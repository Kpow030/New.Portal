from django import forms



from .models import Post, Category


class PostSearchForm(forms.Form):
    q = forms.CharField(required=False, label='Поиск по названию.')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, label='Поиск по категории.')
    date_after = forms.DateField(input_formats=[{'format': '%Y-%m-%d'}], required=False, label='Поиск по дате.')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'Text']
