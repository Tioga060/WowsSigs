from models import Player
from .apps.djangular.forms import NgFormValidationMixin, NgModelFormMixin, AddPlaceholderFormMixin

class SignatureForm(NgModelFormMixin, forms.ModelForm):
     """
     Signature Form with a little crispy forms added!
     """
     def __init__(self, *args, **kwargs):
         super(JSignatureForm, self).__init__(*args, **kwargs)
         setup_bootstrap_helpers(self)

     class Meta:
         model = Player
         fields = ('name', 'playerid',)

def setup_bootstrap_helpers(object):
     object.helper = FormHelper()
     object.helper.form_class = 'form-horizontal'
     object.helper.label_class = 'col-lg-3'
     object.helper.field_class = 'col-lg-8'
