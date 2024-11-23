from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

arr = ['Java', 'Python', 'Cplusplus', 'C', 'DotNET', 'Javascript', 'PHP', 'Swift', 'SQL', 'React', 'Ruby', 'Objective C', 'Go', 'Assemblylanguage', 'MongoDB', 'MySQL']
globalcount = dict()
# Create your views here.
def index(request):
    mydict = {
        'arr' : arr
    }
    return render(request, 'voting/index.html', context=mydict)

def getquery(request):
    q = request.GET['languages']
    if q in globalcount:
        globalcount[q] = globalcount[q] + 1
    else :
        #first occurance
        globalcount[q] = 1
    mydict = {
        "arr" : arr,
        "globalcount" : globalcount
    }
    return render(request, 'voting/index.html', context=mydict)

def sortdata(request):
    global globalcount
    globalcount = dict(sorted(globalcount.items(), key=lambda x:x[1], reverse=True))
    mydict = {
        'arr' : arr,
        "globalcount" : globalcount
    }
    return render(request, 'voting/index.html', context=mydict)