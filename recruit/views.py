from django.http.response import HttpResponseBadRequest
from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
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
    if request.user.is_authenticated:
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
    return application_info


def application_parser(project_id: int):
    question_list = get_question_list(project_id).json()
    cnt = question_list['question_cnt']
    questions = dict()
    for i in range(1, cnt + 1):
        questions[i] = question_list[i]
    return cnt, questions


def get_question_list(project_id):
    application: Project = Project.objects.get(applcation_id)
    return application.question_list_json


def draw_up_application(request, project_id):
    current_user == self.request.user
    cnt, questions = application_parser(project_id)
    if current_user.is_authenticated:
        application = Application.object.create()
        application['user_id'] = current_user
        application['project_id'] = project_id
        answers = dict()
        if request.method == 'POST':
            for i in range(1, cnt):
                ans = request.POST[str(i)]
            application['form_data_json'] = answers.json()
            application.save()
        else:
            return redirect()
    else:
        raise PermissionDenied


### PROJECT ###
def add_member(project: Project, user: int) -> bool:
    members = project.member.all()
    if (members.count() + 1) > project.max_recruit:
        return False
    elif members.filter(pk=user).exists():
        return False
    project.member.add(user)
    return True

def remove_member(project: Project, user: int) -> bool:
    user_obj = project.member.filter(pk=user)
    if not user_obj: return False
    project.member.remove(user)
    return True


def project_view(request, id):
    project = get_object_or_404(Project, pk=id)
    if request.method == 'POST':
        if not add_member(project, request.user.pk):
            return HttpResponseBadRequest()
    return render(request, 'project/project.html', {'project': project})

def kick_member_view(request, id):
    project= get_object_or_404(Project, pk=id)
    if request.method == 'POST':
        if not remove_member(project, request.user.pk):
            return HttpResponseBadRequest()
    return redirect('project', id)
