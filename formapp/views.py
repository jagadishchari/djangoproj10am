from django.shortcuts import render
from django.http import HttpResponse
from.forms import NameForm
from.models import Name
def get_name(request):
    if request.method=='POST':
        form=NameForm(request.POST)
        if form.is_valid():
            n1=Name(first_name=form.cleaned_data["First_name"],
                    last_name=form.cleaned_data["Last_name"])
            n1.save()
            return HttpResponse('data inserted successfully')
    else:
        form=NameForm()
        return render(request,'name.html',{'form':form})
