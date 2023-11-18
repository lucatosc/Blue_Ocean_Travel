from django import forms
from .models import contact_us

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact_us
        fields = ('full_name', 'email', 'phone_number',
                  'input_text', 'selection',
                  )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'input_text': 'How can we help you today?',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True