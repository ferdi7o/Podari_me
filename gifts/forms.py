from django import forms
from .models import Gift, Tag

class GiftCreateForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = ['title', 'description', 'category', 'image_url', 'tags']
        labels = {
            'title': 'Заглавие на подаръка',
            'description': 'Описание',
            'category': 'Категория',
            'image_url': 'URL на снимка',
            'tags': 'Тагове (Етикети)',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Напр: Стара книга'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Опишете подаръка...'}),
            'tags': forms.CheckboxSelectMultiple(),
        }

class GiftEditForm(GiftCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].disabled = True