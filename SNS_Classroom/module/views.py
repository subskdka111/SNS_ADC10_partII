from django.shortcuts import render
from module.models import Module
from django.shortcuts import redirect

# Create your views here.
def view_modules(request):
    if request.method == 'POST':
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

def add_student_in_module(request,id):
    moduleToEnroll = Module.objects.get(id=id)
    moduleToEnroll.studentsEnrolled.add(request.user)
    return redirect('/modules/')

