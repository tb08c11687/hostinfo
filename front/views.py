from django.shortcuts import render
from django.views.generic import View
from .forms import HostInfoForm
from django.http import HttpResponse
# Create your views here.
class IndexView(View):
    def get(self,request):

        return render(request,'index.html')
    def post(self,request):
        form = HostInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('添加成功')
        else:
            print(form.errors.get_json_data())
            return HttpResponse(form.errors.get_json_data().items())