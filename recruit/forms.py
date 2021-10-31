from django import forms
from django.forms.widgets import Select, TextInput, Textarea

# 프로젝트 생성 폼
INPUT_CLASSVALUE = "form-control px-3"
class ProjectCreateForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ProjectCreateForm, self).__init__(*args, **kwargs)

    title = forms.CharField(
        widget=TextInput(attrs={
            "placeholder": "프로젝트명", "class": INPUT_CLASSVALUE
        })
    )

    ESTIMATE_CHOICES = ( (1, '1개월'), (3, '3개월'), (6, '6개월'))
    estimate = forms.IntegerField(
        widget=Select(choices=ESTIMATE_CHOICES, attrs={
            "placeholder": "예상 소요기간", "class": INPUT_CLASSVALUE+" form-select"
        })
    )

    RECRUIT_CHOICES = ( (i, '{}명'.format(i)) for i in range(1, 100+1) )
    max_recruit = forms.IntegerField(
        widget=Select(choices=RECRUIT_CHOICES, attrs={
            "placeholder": "모집 인원", "class": INPUT_CLASSVALUE+" form-select"
        })
    )
    description = forms.CharField(
        widget=Textarea(attrs={
            "placeholder": "최대 2000자까지 작성 가능합니다.", "class": INPUT_CLASSVALUE
        })
    )

    def clean(self):
        cleaned_data = super(ProjectCreateForm, self).clean()
        return cleaned_data