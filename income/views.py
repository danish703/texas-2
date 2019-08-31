from django.shortcuts import render,HttpResponse
from .forms import IncomeCategoryForm,IncomeForm
# Create your views here.
def add(request):
    if request.method=='GET':
        context= {
            'cform':IncomeCategoryForm(),
            'form':IncomeForm,
            'id':request.user.id
        }
        return render(request,'add_income.html',context)
    else:
        if request.POST['what']=='cat':
            form = IncomeCategoryForm(request.POST)
            if form.is_valid():
                data = form.save(commit=False)
                data.user_id = request.user.id
                data.save()
                return HttpResponse("successfully saved")
        else:
            form = IncomeForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse("yes success")
