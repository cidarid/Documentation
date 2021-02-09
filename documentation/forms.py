from django import forms
from .models import Documentation, Category


class DocForm(forms.ModelForm):
    class Meta:
        model = Documentation
        labels = {
            "doc_title": "Documentation Title",
            "doc_text": "Documentation Text",
        }
        fields = ['doc_title', 'doc_text', 'category']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        labels = {
            "name": "Category Title",
        }
        fields = ['name']


class DocumentForm(forms.Form):
    doc_file = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes',
    )
    title = forms.CharField(max_length=256)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True, help_text="Category",
                                      empty_label=None)
