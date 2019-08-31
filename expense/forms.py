from django import forms
from .models import ExpensesCategory,Expenses


class ExpensesCategoryForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = ExpensesCategory
        fields = ['title']



class ExpenseForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    cost = forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control'}),queryset=ExpensesCategory.objects.all())
    class Meta:
        model = Expenses
        fields = '__all__'