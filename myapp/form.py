from django import forms
SHIFTS=(
    ('1','Morning'),
    ('2','Afternoon'),
    ('3','Evening'),
)
class CreateAccountForm (forms.Form):
    First_Name = forms.CharField(label='First Your name')
    Last_Name = forms.CharField(label='Last Your name')
    Shift = forms.ChoiceField(choices = SHIFTS)
    Time_Log = forms.TimeField()