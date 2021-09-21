from django import forms
from .file_handling import read_csv
from django.utils.translation import gettext as _ # This is for translation

def validate_upload_dict(file):
    dictionaries = read_csv(file)
    for field in ['member_id', 'main_contact', 'phone']:
       if any(field not in dictionary for dictionary in dictionaries):
           raise forms.ValidationError(_("CSV row is missing a field value."), code="bad-columns")