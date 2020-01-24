from django.test import TestCase
from module.views import Module
from .models import Assignment, StudentsFile 
from django.contrib.auth.models import User

# Create your tests here.
class AssignmentModelsTestCase(TestCase):
    def setUp(self):
        user_1 = User.objects.create_user(
            username="user_1",
            email="user1@gmail.com"
        )
        user_2 = User.objects.create_user(
            username="user_2",
            email="user2@gmail.com"
        )
        module_1 = Module.objects.create(
            moduleCode="M01",
            moduleName="Module 1",
            moduleTeacher=user_1
        )
        assignment_1 = Assignment.objects.create(
            author=user_1,
            assignmentTitle="Assignment Title 1",
            module=module_1
        )
        studentsFile_1 = StudentsFile.objects.create(
            student=user_2,
            assignment=assignment_1
        )

    def test_postedBy(self):
        user1 = User.objects.get(pk=1)
        user2 = User.objects.get(pk=2)
        assignment = Assignment.objects.get(pk=1)
        self.assertTrue(assignment.postedBy() == user1)
        self.assertFalse(assignment.postedBy() == user2)

    def test_getAssignment(self):
        assignment = Assignment.objects.get(pk=1)
        studentsFile = StudentsFile.objects.get(pk=1)
        self.assertEqual(studentsFile.getAssignment(), assignment)

    def test_getModule(self):
        module = Module.objects.get(pk=1)
        assignment = Assignment.objects.get(pk=1)
        self.assertTrue(assignment.getModule(), module)