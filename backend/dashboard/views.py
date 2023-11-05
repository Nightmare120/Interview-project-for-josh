from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, LandingPage
import json

# Create your views here.
def dashboard(request):
    all_project = Project.objects.all()
    context = {"projects": all_project}
    return render(request,"index.html", context=context)

def create_project_page(request):
    return render(request,"create-project.html")

def project(request):
    id = (request.GET.get('id', None))
    if id:
        context = {"project": Project.objects.get(id=id)}
        return render(request,"project.html",context=context)
    return HttpResponse(status=405)

def create_new_project(request):
    if (request.method == "POST"):
        data = (json.loads(request.body))
        print(data)
        Project.objects.create(
            name=data['name'],
            description= data['desc'],
            product_name= data['productName'],
            product_description= data['productDesc'],
            user_ideas= data['userIdeas'],
            traffic_description= data['trafficDesc'],
            base_landing_page= create_landing_page(data)
        )
        return HttpResponse(status=200)
    return HttpResponse(status=405)

def create_landing_page(data):
    a = LandingPage.objects.create(
        name=data['pageName'],
        conversion_rate= float(data['conversionRate']),
        html= data['pageHtml']
    )
    return a

def delete_project(request):
    if (request.method == "POST"):
        data = (json.loads(request.body))
        id = data['id']
        instance = Project.objects.get(id=id)
        instance.delete()
        return HttpResponse(status=200)
    return HttpResponse(status=405)

def save_project(request):
    if (request.method == "POST"):
        data = (json.loads(request.body))
        id = data['id']
        instance = Project.objects.get(id=id)
        instance.product_name = data['productName']
        instance.product_description = data['productDesc']
        instance.user_ideas = data['userIdeas']
        instance.traffic_description = data['trafficDesc']
        instance.base_landing_page.conversion_rate = data['conversionRate']
        instance.base_landing_page.html = data['pageHtml']
        instance.base_landing_page.save()
        # instance.

        if bool(int(data['isAB_Active'])):
            handle_AB_testing(instance,data['pageHtml2'],data['conversionRate'])
        else:
            instance.base_landing_page2 = None
        print(instance.base_landing_page2)

        instance.save()
        return HttpResponse(status=200)
    return HttpResponse(status=405)

def handle_AB_testing(project,html,conversion_rate):
    if project.base_landing_page2 == None:
        project.base_landing_page2 = create_landing_page({
            "pageName":"",
        "conversionRate":conversion_rate,
        "pageHtml":html,
        })
    else:
        project.base_landing_page2.conversion_rate = conversion_rate
        project.base_landing_page2.html = html
    
    project.base_landing_page2.save()

def show_html_page(request):
    id = (request.GET.get('id', None))
    split = request.GET.get('split', None)

    context = {"html": getHtmlBySplit(id,split)}
    return render(request,"html-page.html", context=context)

def getHtmlBySplit(id,split):
    instance = Project.objects.get(id=id)
    if split == 'b':
        return instance.base_landing_page2.html
    return instance.base_landing_page.html