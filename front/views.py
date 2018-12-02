from django.shortcuts import render,reverse,redirect
from django.views.generic import View
from .forms import HostInfoForm, UserInfoForm
from django.http import HttpResponse
from .models import HostInfo,UserInfo
import re
from django.contrib import messages
# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')
    def post(self, request):
        form = HostInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('添加成功')
        else:
            errors = form.get_error()
            #print(form.errors.get_json_data())
            for error in errors:
                messages.info(request, error)
            return redirect(reverse('index'))



class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        form = UserInfoForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = UserInfo.objects.filter(username=username,password=password)
            if user:
                request.session['user_id'] = user.id
                return redirect(reverse('management'))
            else:
                messages.info(request, '用户名或者密码错误！')
                return redirect(reverse('login'))
        else:
            errors = form.errors.get_json_data()
            print(errors)
            return redirect(reverse('login'))


class QueryView(View):
    def get(self, request):
        return render(request, 'query.html')
    def post(self, request):
        pass
class ManagementView(View):
    def get(self, request):
        return render(request, 'management.html')
