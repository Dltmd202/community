from django import forms
from django.forms.widgets import Select, TextInput, Textarea

# 프로젝트 생성 폼
class ProjectCreateForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ProjectCreateForm, self).__init__(*args, **kwargs)

    title = forms.CharField(
        widget=TextInput(attrs={
            "placeholder": "프로젝트명"
        })
    )

    ESTIMATE_CHOICES = ( (1, '1개월'), (3, '3개월'), (6, '6개월'))
    estimate = forms.IntegerField(
        widget=Select(choices=ESTIMATE_CHOICES, attrs={
            "placeholder": "예상 소요기간"
        })
    )

    RECRUIT_CHOICES = ( (i, '{}명'.format(i)) for i in range(1, 100+1) )
    max_recruit = forms.IntegerField(
        widget=Select(choices=RECRUIT_CHOICES, attrs={
            "placeholder": "모집 인원"
        })
    )
    description = forms.CharField(
        widget=Textarea(attrs={
            "placeholder": "상세 설명"
        })
    )

    def clean(self):
        cleaned_data = super(ProjectCreateForm, self).clean()
        return cleaned_data