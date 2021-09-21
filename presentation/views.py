import os

from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from facilitation.models import Token
from .models import Survey
from .forms import SurveyForm

def survey(request, uid):
    try:
        token = Token.objects.get(uid=uid)
    except ObjectDoesNotExist:
        return redirect('no-token')
    
    if request.method == 'POST':
        survey = Survey(patient=token.member_id)

        form = SurveyForm(request.POST, instance=survey)
        if form.is_valid():
            form.save()
            token.completed = True
            token.save()
            return redirect('thank-you')
        else:
            print(form.errors)
        return redirect('error-and-retry', uid=token.uid)

    form = SurveyForm
    return render(request, 
                  os.path.join('presentation', 'survey.html'), 
		  context={'form':form, 'uid':uid})

def error_and_retry(request, uid):
    return render(request, 
                  os.path.join('presentation', 'error.html'),
		  context={'uid': uid})

def error_attempted_resubmission(request):
    return render(request, 
                  os.path.join('presentation', 'attempted_resubmit.html'))

def error_no_token(request):
    return render(request, os.path.join('presentation', 'no_token.html'))

def thank_you(request):
    return render(request, os.path.join('presentation', 'thank_you.html'))