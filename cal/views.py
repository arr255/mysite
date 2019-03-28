from django.shortcuts import render
from sympy import *
from django.http import HttpResponse
from sympy.abc import x,y,z
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

def myInt(request):
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
    data={"result": str(result), "result2": str(result2)}
    response = HttpResponse(json.dumps(data))
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response
def myDiff(request):
    expr=request.GET.get('expr')
    variable=request.GET.get('variable')
    number=request.GET.get('number')
    x=symbols("x")
    result=diff(expr,variable).subs(variable,float(number))
    response = HttpResponse(json.dumps({"result":str(result)}))
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response


def mySum(request):
    formula = request.GET.get('formula')
    downNumber = request.GET.get('downNumber')
    upNumber = request.GET.get('upNumber')
    result = Sum(formula, ('x', downNumber, upNumber)).doit()
    if (isinstance(result, float)):
        result = eval(str(result))
    else:
        result = result.evalf()
    data = {"result": str(result)}
    response = HttpResponse(json.dumps(data))
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response


def myProd(request):
    formula = request.GET.get('formula')
    downNumber = request.GET.get('downNumber')
    upNumber = request.GET.get('upNumber')
    result = Product(formula, ('x', downNumber, upNumber)).doit()
    if (isinstance(result, float)):
        result = eval(str(result))
    else:
        result = result.evalf()
    data = {"result": str(result)}
    response = HttpResponse(json.dumps(data))
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response
