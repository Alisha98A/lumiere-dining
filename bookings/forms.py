from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Form for user registration, extending UserCreationForm to include an email field
class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=200, 
        help_text='Required. Please provide a valid email address.'
    )

    # Password field with input widget and validation for strength
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        help_text=(
            'Required. Must be at least 8 characters long, '
            'not entirely numeric, and should not be too similar to your username.'
        ),
        min_length=8
    )

    class Meta:
     # Specify the user model and fields to include in the form
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # Validate email uniqueness in the database
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

    # Validate password strength and requirements
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:  
            raise forms.ValidationError("Password must be at least 8 characters long.")
        if password1.isnumeric():  
            raise forms.ValidationError("Password cannot be entirely numeric.")
        return password1

    # Validate that both password fields match
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        # Raise an error if passwords do not match
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data