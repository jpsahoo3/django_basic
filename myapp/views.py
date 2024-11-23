from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import *

# Create your views here.
def myfunction(request):
    return HttpResponse("Hello")

def myfunctionabout(request):
    return HttpResponse("About")

def intro(request, name, age):
    mydict = {
        "name" : name,
        "age" : age
    }

    return JsonResponse(mydict)

def myfirstpage(request):
    return render(request, 'index.html')

def mysecondpage(request):
    return render(request, 'second.html')

def mythirdpage(request):
    var = "hello"
    greet = "how are you"
    fruits = ["apple", "banana", "orange"]
    n1, n2 = 10, 5
    ans = n1 > n2

    mydict = {
        "var" : var,
        "msg" : greet,
        "fruits" : fruits,
        "num1" : n1,
        "num2" : n2,
        "ans" : ans
    }
    return render(request, 'third.html', context=mydict)

def myimage(request):
    return render(request, 'image.html')

def myimage2(request):
    return render(request, 'image2.html')

def myimage3(request):
    return render(request, 'image3.html')

def myimage4(request):
    return render(request, 'image4.html')

def myimage5(request, imagename):
    myimg = str(imagename).lower()
    if myimg == "django":
        val = True
    elif myimg == "python":
        val = False

    mydict = {
        "val" : val
    }
    return render(request, 'image5.html', context = mydict)

def myform(request):
    return render(request, 'myform.html')

def submitmyform(request):
    mydict = {
        "var1" : request.POST['mytext'],
        "var2" : request.POST['mytextarea'],
        "method" : request.method
    }
    # return render(request, 'myform.html')
    return JsonResponse(mydict)

def myform2(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            email = request.POST['email']
            # var = str("Form Submitted " + str(request.method))
            # return HttpResponse(var)
            mydict = {
                "form" : FeedbackForm()
            }
            errorflag = False
            Errors = []
            if title != title.upper():
                # mydict['error'] = True
                # mydict['errormsg'] = "Title should be in capital"
                # return render(request, 'myform2.html', context=mydict)
                errorflag = True
                errormsg = "Title should be in capital"
                Errors.append(errormsg)
            import re
            regex = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.search(regex, email):
                errorflag = True
                errormsg = "Enter a valid email"
                Errors.append(errormsg)
            # else:
            if errorflag != True:
                mydict['success'] = True
                mydict['successmsg'] = "Form Submitted"
            mydict['error'] = errorflag
            mydict['errors'] = Errors
            return render(request, 'myform2.html', context=mydict)

        else:
            mydict = {
            "form" : form
            }

            return render(request, 'myform2.html', context=mydict)
    elif request.method == "GET":
        form = FeedbackForm()  # FeedbackForm(None)
        mydict = {
            "form" : form
        }

        return render(request, 'myform2.html', context=mydict)

def error_404_view(request, exception):
    return render(request, '404.html')