from django.core.management.base import BaseCommand
from module.models import Module

class Command(BaseCommand):
    help = 'Creates some modules'

    def handle(self, *args, **kwargs):
        Module.objects.bulk_create([
            Module(moduleCode="ADipIT01",moduleName="Software Engineering"),
            Module(moduleCode="ADipIT02",moduleName="Object Oriented Design and Programming"),
            Module(moduleCode="ADipIT03",moduleName="Database Design and Implementation"),
            Module(moduleCode="ADipIT04",moduleName="Software Project Management"),
            Module(moduleCode="ADipIT05",moduleName="System Analysis and Design Methods"),
            Module(moduleCode="ADipIT06",moduleName="Research and Development Skills in Computing"),
            Module(moduleCode="ADipIT07",moduleName="Current Technologies: Mobile and Cloud Computing"),
            Module(moduleCode="ADipIT08",moduleName="Introductory Computer Networking and IT Security"),
        ])
        self.stdout.write("Modules created successfully!!")
