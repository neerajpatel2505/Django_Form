from django.shortcuts import render
from .forms import SyudentRegistration
# Create your views here.

def formdata(request):
    form = SyudentRegistration(auto_id=True) # not include lebel tag
    return render(request,'app/registration.html',{'form':form})

    # form = SyudentRegistration(auto_id=True) # <label for="name">Name:</label>
    # return render(request,'app/registration.html',{'form':form})

    # form = SyudentRegistration(auto_id='neeraj') # act as auto_id=True
    # return render(request,'app/registration.html',{'form':form})

    # form = SyudentRegistration(auto_id='id_%s', initial={'first_name':'Neeraj','email':'neeraj@gmail.com','contact':'9424444348'}) # bydefault----<label for="id_name">
    # form.order_fields(['contact','email'])
    # return render(request,'app/registration.html',{'form':form})
    
    # form = SyudentRegistration(auto_id='id_%s')
    # return render(request,'app/registration.html',{'form':form})
