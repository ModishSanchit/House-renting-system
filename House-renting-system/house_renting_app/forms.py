

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:   #This will connect models to the actual form
        model=User
        fields=('first_name','last_name','username','password',)

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model=UserProfileInfo    #this is model
#         fields=('phone_number',)
