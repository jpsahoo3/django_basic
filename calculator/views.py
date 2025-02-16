from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'calculator/index.html')

def submitquery(request):
    q = request.GET['query']
    try:
        ans = eval(q)
        mydict = {
            "q" : q,
            "ans" : ans,
            "error" : False,
            "result" : True
        }
        return render(request, 'calculator/index.html', context=mydict)
    except:
        mydict = {
            "error" : True,
            "result" : False
        }
        return render(request, 'calculator/index.html', context=mydict)