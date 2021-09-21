from django import forms
from .models import Survey

questions = {
    'answer_one': 'How much of the food from our deliveries have you and your family eaten?',
    'answer_two': 'What are some of the reasons you did not use of the food?',
    'answer_two_a': 'If other please specify',
    'answer_three': 'Were all the ingredients familiar to you?',
    'answer_four': 'The food you receive from this program is designed to supplement other foods that you might be getting from other sources/places. Is this program providing enough food to meet your needs?',
    'answer_four_b': 'If not, can you explain?',
    'answer_five': 'Overall, how satisfied are you with the quality of the food provided?',
    'answer_six': 'Overall, how satistied are you with the quality of the service provided?',
    'answer_seven': 'Did you use any of the recipes from the recipe book you received?',
    'answer_seven_b': 'If no, why not?',
    'answer_eight': 'What other nutritional resources would be useful to you?',
    'answer_nine': 'What else would you like to share about your experience in the program so far?',
}

choices_one = [('little', 'Little or none (0% - 50%)'),
               ('some', 'Some (50% - 75%)'),
		       ('most', 'Most or all (75% - 100%)')]
    
choices_three = [('Y', 'Yes'),
                 ('N', 'No')]

choices_four = [('Y', 'Yes'),
                     ('N', 'No')]

choices_five = [('5', 'Very satisfied'),
                    ('4', 'Somewhat satisfied'),
		            ('3', 'Neither satisfied or dissatisfied'),
		            ('2', 'Somewhat dissatisfied'),
		            ('1', 'Very dissatisfied')]

choices_six = [('5', 'Very satisfied'),
                   ('4', 'Somewhat satisfied'),
		           ('3', 'Neither satisfied or dissatisfied'),
		           ('2', 'Somewhat dissatisfied'),
		           ('1', 'Very dissatisfied')]

choices_seven = [('Y', 'Yes'),
                     ('N', 'No')]

widgets = {
    'answer_one': forms.RadioSelect(choices=choices_one),
    'answer_three': forms.RadioSelect(choices=choices_three),
    'answer_four': forms.RadioSelect(choices=choices_four),
    'answer_five': forms.RadioSelect(choices=choices_five),
    'answer_six': forms.RadioSelect(choices=choices_six),
    'answer_seven': forms.RadioSelect(choices=choices_seven),
}


class SurveyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        
        for field, question in questions.items():
            self.fields[field].label = question

        for field, widget in widgets.items():
            self.fields[field].widget = widget

    class Meta:
        model = Survey
        exclude = ('patient',
                   '')