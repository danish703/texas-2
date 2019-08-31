from django.shortcuts import render,HttpResponse
from .forms import ExpensesCategoryForm,ExpenseForm
# Create your views here.
def add(request):
    if request.method=='GET':
        context = {
            'cform':ExpensesCategoryForm(),
            'form':ExpenseForm()
        }
        return render(request,'add_expenses.html',context)
    else:
        if request.POST['what']=='cat':
            c = ExpensesCategoryForm(request.POST)
            if c.is_valid():
                d = c.save(commit=False)
                d.user_id = request.user.id
                d.save()
                return HttpResponse("successfully saved")
            else:
                return render(request,'add_expenses.html',{'cform':c,'from':ExpenseForm()})
        else:
            form = ExpenseForm(request.POST,request.FILES or None)
            if form.is_valid():
                form.save()
                return HttpResponse("successfully saved")
            else:
                return render(request, 'add_expenses.html', {'cform': ExpensesCategoryForm(), 'from': form})