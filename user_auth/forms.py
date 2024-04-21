from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class ExtendedUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your first name.')

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize password error messages
        self.fields['password1'].help_text = _(
            "Your password must contain at least 8 characters, "
            "not be too common, and not be too similar to your other personal information."
        )

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        # Custom password validation
        if len(password1) < 8:
            raise forms.ValidationError(
                _("Password must be at least 8 characters."),
                code='password_too_short',
            )
        return password1
