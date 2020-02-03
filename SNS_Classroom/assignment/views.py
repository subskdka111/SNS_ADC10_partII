from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import Template, Context
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from assignment.models import *
from module.models import Module
from django.contrib import messages

def view_assignments(request):
    listOfassignments = Assignment.objects.all()
    context_variable = {
        'assignments': listOfassignments
    }
    return render(request, 'assignments.html', context_variable)

def view_assignment(request, id):
    assignment = Assignment.objects.get(id=id)
    files = StudentsFile.objects.filter(student=request.user)
    comments = AssignmentComment.objects.filter(assignment=assignment)
    context_variable = {
        'assignment': assignment,
        'comments': comments,
        'files': files,
    }
    return render(request, 'assignment.html', context_variable)

def view_create_assignment(request):
    if request.user.is_authenticated:
        context_variable = {
            'modules': Module.objects.all()
        }
        return render(request, 'createAssignment.html', context_variable)
    else:
        return redirect('/assignments/')

def create_assignment(request):
    if request.user.is_authenticated:
        get_author = request.user
        get_assignmentTitle = request.POST['assignmentTitle']
        get_assignmentContent = request.POST['content']
        get_moduleID = request.POST['module']
        uploaded_file = request.FILES.get('assignmentQuestionPapers')
        assignmentObj = Assignment(
            author=get_author,
            assignmentTitle=get_assignmentTitle,
            content=get_assignmentContent,
            module=Module.objects.get(pk=get_moduleID)
        )
        if uploaded_file:
            fs = FileSystemStorage()
            get_assignmentImage = fs.save(uploaded_file.name, uploaded_file)
            assignmentObj.assignmentQuestionPapers = get_assignmentImage
        assignmentObj.save()
    return redirect('/assignments/')


def view_update_assignment(request, id):
    get_assignment_to_update = Assignment.objects.get(id=id)
    if request.user.is_authenticated and request.user == get_assignment_to_update.author:
        context_variable = {
            'assignment': get_assignment_to_update
        }
        return render(request, 'updateAssignment.html', context_variable)
    else:
        messages.error(request, "Not authenticated to edit this assignment")
        return redirect('/assignments/')


def update_assignment(request, id):
    get_assignment_to_update = Assignment.objects.get(id=id)
    if request.user.is_authenticated and request.user == get_assignment_to_update.author:
        get_author = request.user
        get_assignment_to_update.assignmentTitle = request.POST['assignmentTitle']
        get_assignment_to_update.content = request.POST['content']
        uploaded_file = request.FILES.get('assignmentQuestionPapers')
        if uploaded_file:
            fs = FileSystemStorage()
            get_assignmentImage = fs.save(uploaded_file.name, uploaded_file)
            get_assignment_to_update.assignmentQuestionPapers = get_assignmentImage
        get_assignment_to_update.save()
    else:
        messages.error(request, "Not authenticated to edit this assignment")
    return redirect('/assignments/' + str(id))


def delete_assignment(request, id):
    get_assignment_to_delete = Assignment.objects.get(id=id)
    if request.user.is_authenticated and request.user == get_assignment_to_delete.author:
        get_assignment_to_delete.delete()
    else:
        messages.error(request, "Not authenticated to edit this assignment")
    return redirect('/assignments/')

def assignment_comment(request, id):
    if request.method == 'POST' and request.user.is_authenticated:
        commentObj = AssignmentComment(
            commenter=request.user,
            assignment=Assignment.objects.get(id=id),
            commentContent=request.POST['commentContent']
        )
        commentObj.save()
    return redirect('/assignments/' + str(id))

def upload_file(request, id):
    if request.method == 'POST' and request.user.is_authenticated:
        uploaded_file = request.FILES.get('studentsFile')
        if uploaded_file:
            fs = FileSystemStorage()
            uploaded_file = fs.save(uploaded_file.name, uploaded_file)
            studentFile = StudentsFile(
                student=request.user,
                assignment=Assignment.objects.get(id=id),
                Studentsfile=uploaded_file
            )
            studentFile.save()
        else:
            messages.error(request, "No file attached!!")
    return redirect('/assignments/' + str(id))

def delete_file(request, id):
    s = StudentsFile.objects.get(id=id)
    id = s.assignment.id
    s.delete()
    return redirect('/assignments/' + str(id))
        
