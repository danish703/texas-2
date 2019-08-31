from django import forms
from .models import IncomeCategory,Income


class IncomeCategoryForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = IncomeCategory
        fields = ['title']



class IncomeForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    rupes = forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control'}),queryset=IncomeCategory.objects.all())
    class Meta:
        model = Income
        fields = '__all__'