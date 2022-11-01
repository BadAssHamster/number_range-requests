from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponseRedirect
from request_app.models import Requests
from .forms import RequestForm, MoAlterForm, MiacSubmitForm
from .models import *
from datetime import datetime
from django.utils import dateformat


# Форма МО создания заявки
@login_required
def request_form(request):
    if request.method == 'GET':
        form = RequestForm()
    else:
        form = RequestForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            acc = Account.objects.get(user_id=request.user)
            obj.user_id = acc
            obj.save()
            return redirect('/')
    return render(request, 'request-form.html', {'form': form})


# Форма МО редактирования заявки
@login_required
def mo_alter_request(request):
    if request.method == 'GET':
        form = MoAlterForm()
    else:
        form = MoAlterForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            # line собирает данные из бд с помощью request.session который хранит в себе id заявки с другого view
            line = Requests.objects.get(id=request.session['id_to_update'])
            line.doc_type = obj.doc_type
            line.count = obj.count
            line.save()
            return redirect('/')
    return render(request, 'MO-alter-request-form.html', {'alter_form': form})


@login_required
def miac_submit_request(request):
    if request.method == 'GET':
        form = MiacSubmitForm()
    else:
        form = MiacSubmitForm(request.POST)
        if form.is_valid():
            date_container = date.today()
            obj = form.save(commit=False)
            # line собирает данные из бд с помощью request.session который хранит в себе id заявки с другого view
            line = Requests.objects.get(id=request.session['id_to_update'])
            line.numbers = obj.numbers
            # Меня статус заявки на выполнена
            line.status = 3
            # Выставляем дату выполнения заявки
            line.execution_date = date_container
            line.save()
            return redirect('/')
    return render(request, 'miac-submit-request-form.html', {'submit_form': form})


@login_required
def request_list(request):
    # Находим юзера
    acc = Account.objects.get(user_id=request.user)
    # Страница пользователя МО, проверяем что юзер МО
    if acc.user_type.id == 1:
        # Собираем всего заявки юзера
        user_requests = Requests.objects.filter(user_id=acc)
        if request.method == 'POST':
            for item in user_requests:
                # Узнаем какая именно кнопка была нажата
                if request.POST.get(f"{item.id}_delete") == 'clicked':
                    if item.status == 1:
                        item.delete()
                    return redirect('/')
                elif request.POST.get(f"{item.id}_send") == 'clicked':
                    if item.status == 1:
                        date_container = date.today()
                        item.status = 2
                        item.date = date_container
                        item.save()
                    return render(request, 'request-list.html', {'user_requests': user_requests})
                elif request.POST.get(f"{item.id}_update") == 'clicked':
                    if item.status == 1:
                        request.session['id_to_update'] = int(item.id)
                        return HttpResponseRedirect('mo-alter-form/')
                    return redirect('/')
                elif request.POST.get("create") == '1':
                    return HttpResponseRedirect('form/')
        else:
            return render(request, 'request-list.html', {'user_requests': user_requests})
    # Страница пользователя МИАЦ
    else:
        user_requests = Requests.objects.all()
    # Кнопка редактировать в таблице на форме
    if request.method == 'POST':
        for item in user_requests:
            if item.status == 2:
                if request.POST.get(f"{item.id}_update") == 'clicked':
                    request.session['id_to_update'] = int(item.id)
                    return HttpResponseRedirect('miac-submit-form/')
    return render(request, 'miac-request-list.html', {'user_requests': user_requests})
