from django import forms

from .models import *



class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(MembershipForm, self).__init__(*args, **kwargs)

        not_required = ('picture')
        for field in not_required:
            self.fields[field].required = False


            









# ['first_name', 'last_name', 'other_names', 'active', 'sex', 'discipler', 'telephone',
#                   'email', 'date_of_birth', 'country', 'state_of_origin', 'lga','marital_status', 'spouse_name', 'next_of_kin', 'relationship_with_nok', 'number_of_children', 'address', 'date_joined', 'tribe', 'fathers_name', 'mothers_name', 'guardians_name', 'home_cell', 'picture',
#                   'signtature']
