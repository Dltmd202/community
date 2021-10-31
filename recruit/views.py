from django.http.response import HttpResponseBadRequest, HttpResponseForbidden
from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import *

import json
import datetime

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
# 프로젝트에 멤버 추가하는 메소드
def add_member(project: Project, user: int) -> bool:
    members = project.member.all()
    if (members.count() + 1) > project.max_recruit:
        return False
    elif members.filter(pk=user).exists():
        return False
    project.member.add(user)
    return True

# 프로젝트에서 멤버 제거하는 메소드
def remove_member(project: Project, user: int) -> bool:
    user_obj = project.member.filter(pk=user)
    if not user_obj: return False
    project.member.remove(user)
    return True

def project_list_view(request):
    projects = Project.objects.all()
    return render(request, 'project/project_list.html', {'projects': projects})

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

def project_create_view(request):
    if request.user.is_authenticated:
        user = request.user
        form = ProjectCreateForm()
        if request.method == 'POST':
            form = ProjectCreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                estimate = form.cleaned_data['estimate']
                max_recruit = form.cleaned_data['max_recruit']
                description = form.cleaned_data['description']
                estimate_obj = get_object_or_404(Estimate, converted_months=datetime.datetime(2021, 10, 31, 9, 57, 52))
                project = Project(
                    manager=user, estimate=estimate_obj, title=title, 
                    max_recruit=max_recruit, description=description
                )
                project.save()
                print(type(project.pk))
                return redirect('project', project.pk)
            else:
                return HttpResponseBadRequest("폼 형식이 옳지 않습니다.")
        return render(request, 'project/project_create.html', {'form': form})
    else:
        return HttpResponseForbidden("로그인을 해주세요.")