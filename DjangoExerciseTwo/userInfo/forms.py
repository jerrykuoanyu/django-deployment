from django import forms
from django.core import validators
from userInfo.models import User
from userInfo.models import UserProfile
from django.contrib.auth.models import User as User_default



class login_Form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User_default
        fields = ('username','email','password')

class UserProfile_Form(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('porfolio_site','profile_pic')


class model_Form(forms.ModelForm):

    class Meta:
        model = User
        fields = "__all__"


    def save_user_form(self):
        all_clean_data = super().clean()
        fname = all_clean_data['first_name']
        lname = all_clean_data['last_name']
        email = all_clean_data['email']

        if len(fname)==0 or len(lname)==0 or len(email)==0:
            print("Make sure all fields are filled!")
        else:
            #t = User.objects.get_or_create(first_name=fname,last_name=lname,email=email)[0]
            #t.save()
            return True


# check if the first letter of name is z or not
def check_for_z(value):
    if value[0].lower() != "z":
        raise forms.ValidationError("Name needs to start with z")


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])

    email = forms.EmailField()

    # check the email
    verify_email = forms.EmailField(label="Enter your Email again")
    text = forms.CharField(widget=forms.Textarea)


    # clean the form
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Make sure emails match!")
    # botcatcher
    botcatcher = forms.CharField(required= False,widget=forms.HiddenInput,validators=[validators.MaxValueValidator(0)])

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("GOTCHA BOT!")
        return botcatcher
