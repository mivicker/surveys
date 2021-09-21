from django import forms
from .validators import validate_upload_dict

class UploadFileForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(
        attrs=({'id': 'upload-csv'})),
	validators=[validate_upload_dict]
	)