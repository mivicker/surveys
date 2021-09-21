from django.db import models
from multiselectfield import MultiSelectField
from django.utils.timezone import now


class Survey(models.Model):
    submission_time = models.DateTimeField(default=now, editable=False)
    """
    Because this is sort of non-core, I'm going to develop this survey
    as a one off model.
    """

    patient = models.CharField(max_length=10)

    """
    We want to know what you think about the Henry's Groceries for Health program so we can make sure we are meeting your needs.
    Your answers will help us improve the program as needed. Thank you for your time! 
    """

    # Question one:
    # How much of the food from our deliveries have you and your family eaten?
    choices_one = [('little', 'Little or none (0% - 50%)'),
                   ('some', 'Some (50% - 75%)'),
		   ('most', 'Most or all (75% - 100%)')]
    
    answer_one = models.CharField(max_length=6, choices=choices_one, blank=False, default='Unspecified')


    # Question two:
    # What are some of the reasons you did not use of the food?
    choices_two = [('too-much','Too much food.'),
                   ('didnt-like', 'Did not like the food'),
		   ('unknown-prep', 'Did not know how to prepare the food'),
		   ('no-time', 'Did not have time to prepare'),
		   ('not-well', 'Did not feel well enough to prepare myself and no one was available to assist me'),
		   ('went-bad', 'Food went bad before I could eat it'),
		   ('poor-quality', 'Food I received was not the quality I expected'),
		   ('unusual-type', 'Not the types of food my family typically eats')]

    answer_two = MultiSelectField(choices=choices_two)
    answer_two_a = models.CharField(max_length=256, blank=True, null=True)

    # Question three:
    # Were all the ingredients familiar to you?

    choices_three = [('Y', 'Yes'),
                     ('N', 'No')]

    answer_three = models.CharField(max_length=1, choices=choices_three, blank=False, default='Unspecified')

    # Question three b:
    # If no, what ingredients were unfamiliar?

    answer_three_b = models.TextField(blank=True, null=True)

    # Question four:
    # The food you receive from this program is designed to supplement other foods 
    # that you might be getting from other sources/places. Is this program providing 
    # enough food to meet your needs?

    choices_four = [('Y', 'Yes'),
                     ('N', 'No')]

    answer_four = models.CharField(max_length=1, choices=choices_four, blank=False, default='Unspecified')

    # Question four b:
    # If no, can you explain?

    answer_four_b = models.TextField(blank=True, null=True)

    # Question five:
    # Overall, how satisfied are you with the quality of food provided?

    choices_five = [('5', 'Very satisfied'),
                    ('4', 'Somewhat satisfied'),
		            ('3', 'Neither satisfied or dissatisfied'),
		            ('2', 'Somewhat dissatisfied'),
		            ('1', 'Very dissatisfied')]

    answer_five = models.CharField(max_length=1, choices=choices_five, blank=False, default='Unspecified')

    # Question six:
    # Overall, how satisfied are you with the quality of service provided?

    choices_six = [('5', 'Very satisfied'),
                   ('4', 'Somewhat satisfied'),
		           ('3', 'Neither satisfied or dissatisfied'),
		           ('2', 'Somewhat dissatisfied'),
		           ('1', 'Very dissatisfied')]

    answer_six = models.CharField(max_length=1, choices=choices_six, blank=False, default='Unspecified')

    # Question seven:
    # Did you use any of the recipes from the recipe book you received?

    choices_seven = [('Y', 'Yes'),
                     ('N', 'No')]

    answer_seven = models.CharField(max_length=1, choices=choices_seven, blank=False, default='Unspecified')

    # Question seven b:
    # If no, why not?
    choices_seven_b = [('something-else','Preferred to make something else'),
                       ('no-time', 'Did not have time'),
		               ('didnt-like', "Didn't like it"),
		               ('no-time', 'Did not have time to prepare'),
		               ('someone-else-cooks', 'Someone else cooks for me'),
		               ('not-equipt', "Didn't have equipment needed to make the recipe"),
		               ('couldnt-read', "Couldn't read the card"),
		               ('not-well', "Didn't feel well enough to cook"),
                       ('didnt-receive', 'Did not receive a recipe book')]

    answer_seven_b = MultiSelectField(choices=choices_seven_b, blank=True, null=True)

    # Other reason not in choices
    answer_seven_c = models.CharField(max_length=256, blank=True, null=True)

# Question eight:
    # What other nutritional resources would be useful to you?
    choices_eight = [('more-recipes', 'More recipes'),
                     ('food-storage-tips', 'Food storage tips'),
		             ('cooking-tips', 'Healthy cooking tips'),
		             ('cooking-class-referrals', 'Referrals to cooking or nutrition classes'),
		             ('other', 'Other food resources like: pantries, drive through food distributions, SNAP application, assistance, 211')]

    answer_eight = MultiSelectField(choices=choices_eight, null=True, blank=True)


# Question nine:
    # What else would you like to share about your experience in the program so far?

    answer_nine = models.TextField(blank=True, null=True)