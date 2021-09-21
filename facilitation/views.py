import os
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import UploadFileForm
from .file_handling import read_csv, make_csv
from .models import create_tokens

# Workflow
# Gleaners end
# This will be through a survey admin page, all login required.
# 1. Select constituent csv (gets placed in session)
# 2. Confirm token creation
# 3. Redirect to download page
# 4. Use token to send surveys through text page
# 5. Error page

@login_required
def upload_csv(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            dictionaries = read_csv(request.FILES['file'].open())
            persistent = list(dictionaries)
            new_dictionaries = create_tokens(persistent)

            response = HttpResponse(make_csv(new_dictionaries))

            response['Content-Type'] = 'application/vnd.ms-excel'
            response['Content-Disposition'] = f'attachment; filename="NewTokens.csv"'

            return response
        print(form.errors)
        return redirect('upload-error')
    return render(request, 'facilitation/upload_csv.html', context={'form':UploadFileForm()})

@login_required
def error_page(request):
    return render(request, 'facilitation/upload_error.html')