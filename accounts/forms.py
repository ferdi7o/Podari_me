from django import forms
from .models import Profile

class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'city', 'profile_picture']
        labels = {
            'first_name': 'Име',
            'last_name': 'Фамилия',
            'email': 'Имейл',
            'city': 'Град',
            'profile_picture': 'URL на профилна снимка',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Въведете име...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Въведете фамилия...'}),
            'email': forms.EmailInput(attrs={'placeholder': 'example@gmail.com'}),
            'city': forms.TextInput(attrs={'placeholder': 'Вашият град...'}),
            'profile_picture': forms.URLInput(attrs={'placeholder': 'Линк на изображението...'}),
        }

        error_messages = {
            'email': {
                'unique': "Този имейл вече е регистриран. Моля, използвайте друг.",
            },
            'first_name': {
                'max_length': "Името е твърде дълго (макс. 20 символа).",
            }
        }
