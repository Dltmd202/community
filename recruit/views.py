from django.shortcuts import render
from .models import *

import json


# Create your views here.
def Tag_list(request, name):
    tag = Tag.objects.get(name=name)
    projects = Project.objects.filter(tag_id=tag)

    return render(
        request,
        '',
        {
            'projects': projects,
        }
    )


def get_random_tag_color():
    letters = "0123456789ABCDEF"
    color = "#"
    for i in range(6):
        color += letters[randrange(17)]
    return color


def application_encoder(request):
    # FE 에서 input 항목의 이름과 유형 선택해서 post
    # 항목 개수도 cnt로 매핑해서 post
    if request.method == 'POST':
        application = []
        cnt = int(request.POST.get('cnt'))
        for i in range(1, cnt + 1):
            application_form = request.POST.get(str(i))
            application_form["answer"] = ""
            application.append(application_form)
        application_info = {
            "application": application
        }


def application_parser(application_id):
    application = Application.object.get(pk=application_id).json()
    application_data = json.dumps(application)
    return application_data


def draw_up_application(request, application_id):
    # current_user == self.request.user
    # application = application_parser(application_id)
    # if current_user.is_authenticated:
    #     if request.method == 'POST':
    #         application = request.POST.get('application')
    #         current_user.object.application
    pass
