from django.shortcuts import render
from .forms import User_form
from django.http import HttpResponseRedirect
from .models import Storage

# Create your views here.
# the following function is the correct format to display a form. Don't memorize it, comprehend it. 

def picker(req):
    #myform = User_form()
    if req.method == 'POST':
        global myform
        myform = User_form(req.POST)
        #print(myform)
    
        if myform.is_valid():
            global store
            store = Storage(name=myform.cleaned_data['name'], 
                            net=myform.cleaned_data['net'], 
                            ex=myform.cleaned_data['ex'], 
                            sex=myform.cleaned_data['sex'], 
                            pet=myform.cleaned_data['pet'], 
                            neighbourhood=myform.cleaned_data['neighbourhood'])
            store.save()
            print(myform.cleaned_data) # >>> Cleaned_data returns a dictionary of entered data by user in different fields including name of fields as keys and entered data as values
            return HttpResponseRedirect('/result')
    
    else:        
        myform = User_form() # >>> myform instance of the User_form class should be created here, otherwise Django returns local variable error. Actually, the instance gets created when the html form is shown to the user 
        #passion = myform.fields['sex']


    return render(req, 'beta/beta.html', {'myform': myform})


def result(req):
    current_user = Storage.objects.filter(name=myform.cleaned_data['name'])
    #current_net = Storage.objects.filter(net=myform.cleaned_data['net'])
    return render(req, 'beta/result.html', {'mymodel': current_user})


def onboard(req):
    return render(req, 'beta/onboard.html')