from djng.forms import NgFormValidationMixin, NgModelFormMixin
from django.forms import ModelForm

class SignatureForm(NgModelFormMixin, forms.ModelForm):
     """
     Signature Form with a little crispy forms added!
     """
     def __init__(self, *args, **kwargs):
         super(SignatureForm, self).__init__(*args, **kwargs)
         setup_bootstrap_helpers(self)

     class Meta:
         model = Player
         fields = ('username', 'playerid',)

def setup_bootstrap_helpers(object):
     object.helper = FormHelper()
     object.helper.form_class = 'form-horizontal'
     object.helper.label_class = 'col-lg-3'
     object.helper.field_class = 'col-lg-8'
