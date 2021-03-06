from django import forms

from edc_base.modelform_mixins import JSONModelFormMixin, CommonCleanModelFormMixin
from edc_base.modelform_validators import FormValidatorMixin

from ..models import SubjectVisit


class SubjectModelFormMixin(FormValidatorMixin, CommonCleanModelFormMixin,
                            JSONModelFormMixin, forms.ModelForm):

    visit_model = SubjectVisit
