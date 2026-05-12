import re
from django import forms
from .models import Enquiry


class EnquiryForm(forms.ModelForm):

    website = forms.CharField(required=False)

    class Meta:
        model = Enquiry
        fields = [
            'name',
            'email',
            'phone',
            'message',
        ]

    def clean_website(self):
        website = self.cleaned_data.get('website')

        if website:
            raise forms.ValidationError("Spam detected.")

        return website

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()

        if len(name) < 2:
            raise forms.ValidationError("Name must be at least 2 characters long.")

        return name

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()

        digits_only = re.sub(r'\D', '', phone)

        if digits_only.startswith('91') and len(digits_only) == 12:
            digits_only = digits_only[2:]

        if len(digits_only) != 10:
            raise forms.ValidationError("Please enter a valid 10 digit phone number.")

        return digits_only

    def clean_message(self):
        message = self.cleaned_data.get('message', '').strip()

        if len(message) < 10:
            raise forms.ValidationError("Message must be at least 10 characters long.")

        return message

    def clean(self):
        cleaned_data = super().clean()

        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')

        if email and phone:
            exists = Enquiry.objects.filter(
                email__iexact=email,
                phone=phone
            ).exists()

            if exists:
                raise forms.ValidationError(
                    "You have already submitted an enquiry with this email and phone number. Our team will contact you soon."
                )

        return cleaned_data