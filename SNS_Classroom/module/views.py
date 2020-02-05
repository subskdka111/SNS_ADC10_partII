from django.shortcuts import render
from module.models import Module
from django.shortcuts import redirect
from account.checkRole import *

def view_modules(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and checkRole(request, 'admin'):
            moduleObj = Module(
                moduleCode=request.POST['moduleCode'],
                moduleName=request.POST['moduleName']
            )
            moduleObj.save()

        modules = Module.objects.all()
        enrolledModules = request.user.student.all()

        context_variable = {
            'modules': modules,
            'enrolledModules': enrolledModules
        }
        return render(request, 'modules.html', context_variable)
    messages.error(request, "Login to view modules")
    return redirect('/')

def add_student_in_module(request,id):
    if checkRole(request, 'student'):
        moduleToEnroll = Module.objects.get(id=id)
        moduleToEnroll.studentsEnrolled.add(request.user)
    return redirect('/modules/')
