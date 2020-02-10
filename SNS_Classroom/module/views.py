from django.shortcuts import render
from module.models import Module
from assignment.models import Assignment
from posts.models import Post
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

        # getting all modules enrolled by "request.user"
        # from module model
        enrolledModules = request.user.student.all()

        context_variable = {
            'modules': modules,
            'enrolledModules': enrolledModules,
            'staff_roles' : STAFF_ROLES
        }
        return render(request, 'modules.html', context_variable)
    messages.error(request, "Login to view modules")
    return redirect('/')

def add_student_in_module(request,id):
    if checkRole(request, 'student'):
        moduleToEnroll = Module.objects.get(id=id)
        moduleToEnroll.studentsEnrolled.add(request.user)
    return redirect('/modules/')

def view_all_post_of_certain_module(request,id):
    if request.user.is_authenticated:
        module = Module.objects.get(id=id)
        posts = Post.objects.filter(module=module)
        assignments = Assignment.objects.filter(module=module)
        context_variable = {
            'module' : module,
            'posts' : posts,
            'assignments' : assignments
        }
        return render(request, 'module.html', context_variable)
