from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=2,
        widget=forms.TextInput(
            attrs={'placeholder': 'Ваше имя'}
        )
    )

    email=forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Ваш email'}
        )
    )

    message=forms.CharField(
        min_length=1,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Сообщение',
                'cols': 20,
                'rows': 9
            }
        )
    )