from django import forms
from .models import Management


class ManagementCreateForm(forms.ModelForm):
    class Meta:
        model = Management
        fields = ('title', 'description', 'category', 'upload')
        widgets = {
            'title': forms.TextInput(attrs={  # <input type="text" class="form-control"
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={  # <textarea class="form-cotrol"
                'class': 'form-control',
            }),
            'category': forms.Select(attrs={
                'class': "form-control",
            }),
            'upload': forms.ClearableFileInput(attrs={
                'class': "form-control-file",
            }),
        }
