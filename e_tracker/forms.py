from django import forms

from e_tracker.models import Profile, Expense


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'budget': forms.NumberInput(),
        }


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        field = ['title', 'image_url', 'description', 'price']
        exclude=['profile']
        widgets = {
            'title': forms.TextInput(),
            'image_url': forms.TextInput(),
            'description': forms.Textarea(),
            'price': forms.NumberInput(),

        }
