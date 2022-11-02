from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
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


@login_required
def miac_submit_request(request, pk):
    user_request = Requests.objects.filter(id=pk)
    for item in user_request:
        if item.status == 2:
            if request.method == 'GET':
                form = MiacSubmitForm()
            else:
                form = MiacSubmitForm(request.POST)
                if form.is_valid():
                    date_container = date.today()
                    obj = form.save(commit=False)
                    # line собирает данные из бд с помощью request.session который хранит в себе id заявки с другого view
                    line = Requests.objects.get(id=pk)
                    line.numbers = obj.numbers
                    # Меня статус заявки на выполнена
                    line.status = 3
                    # Выставляем дату выполнения заявки
                    line.execution_date = date_container
                    line.save()
                    return redirect('/')
            return render(request, 'miac-submit-request-form.html', {'submit_form': form})


@login_required
def mo_submit_button(request, pk):
    user_request = Requests.objects.filter(id=pk)
    for item in user_request:
        if item.status == 1:
            date_container = date.today()
            item.status = 2
            item.date = date_container
            item.save()
        return redirect('/')


@login_required
def mo_delete_button(request, pk):
    user_request = Requests.objects.filter(id=pk)
    for item in user_request:
        if item.status == 1:
            item.delete()
        return redirect('/')


@login_required
def mo_update_button(request, pk):
    user_request = Requests.objects.filter(id=pk)
    for item in user_request:
        if item.status == 1:
            if request.method == 'GET':
                form = MoAlterForm(instance=item)
            else:
                form = MoAlterForm(request.POST)
                if form.is_valid():
                    obj = form.save(commit=False)
                    line = Requests.objects.get(id=pk)
                    line.doc_type = obj.doc_type
                    line.count = obj.count
                    line.save()
                    return redirect('/')
            return render(request, 'MO-alter-request-form.html', context={'alter_form': form})



@login_required
def request_list(request):
    # Находим юзера
    acc = Account.objects.get(user_id=request.user)
    # Страница пользователя МО, проверяем что юзер МО
    if acc.user_type.id == 1:
        # Собираем всего заявки юзера
        user_requests = Requests.objects.filter(user_id=acc)
        return render(request, 'request-list.html', {'user_requests': user_requests})
    # Страница пользователя МИАЦ
    else:
        user_requests = Requests.objects.filter(status=2) | Requests.objects.filter(status=3)
        return render(request, 'miac-request-list.html', {'user_requests': user_requests})
