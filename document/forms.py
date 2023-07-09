from django import forms

from .models import Document


class UploadForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document', )

    def save_multiple(self, documents):
        for file in documents:
            document = Document(document=file)
            document.save()
