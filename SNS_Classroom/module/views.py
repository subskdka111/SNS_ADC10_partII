from django.shortcuts import render
from module.models import Module

# Create your views here.
def view_modules(request):
    modules = Module.objects.all()
    context_variable = {
        'modules': modules
    }
    return render(request, 'modules.html', context_variable)
