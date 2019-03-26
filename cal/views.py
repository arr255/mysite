from django.shortcuts import render
from sympy import *
from django.http import HttpResponse
import json
# Create your views here.
def inte(request):
    formula = request.GET['formula']
    variable=request.GET['variable']
    downNumber=request.GET['downNumber']
    upNumber=request.GET['upNumber']
    return HttpResponse(integrate(formula,(variable,downNumber,upNumber)))

def calHtml(request):
    return render(request,'cal.html')

def cal(request):
    formula = request.GET.get('formula')
    variable=request.GET.get('variable')
    downNumber=request.GET.get('downNumber')
    upNumber=request.GET.get('upNumber')
    if(not downNumber and not upNumber):
        result=integrate(formula)
        result2=""
    else:
        result = integrate(formula, (variable, downNumber, upNumber))
        if(isinstance(result,float)):
            result2=eval(str(result))
        else:
            result2=result.evalf()
    data={"result":str(result),"result2":str(result2)}
    return HttpResponse(json.dumps(data))
def myDiff(request):
    expr=request.GET.get('expr')
    variable=request.GET.get('variable')
    number=request.GET.get('number')
    x=symbols("x")
    result=diff(expr,variable).subs(variable,float(number))
    data={"result":str(result)}
    return HttpResponse(json.dumps(data))