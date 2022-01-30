from django import forms
from django.conf import settings
from django.core.validators import FileExtensionValidator


class UploadForm(forms.Form):
    file = forms.FileField(
        validators=[FileExtensionValidator(settings.SUPPORTED_FILE_EXT)])
