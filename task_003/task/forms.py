from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['id'] = 'inputImage'
        self.fields['image'].widget.attrs['onchange'] = 'previewFile()'