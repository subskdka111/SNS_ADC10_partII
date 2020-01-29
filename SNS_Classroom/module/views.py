from django.shortcuts import render
from module.models import Module

# Create your views here.
def view_modules(request):
    if request.method == 'POST':
        moduleObj = Module(
            moduleCode=request.POST['moduleCode'],
            moduleName=request.POST['moduleName']
        )
        moduleObj.save()
    modules = Module.objects.all()
    context_variable = {
        'modules': modules
    }
    return render(request, 'modules.html', context_variable)
