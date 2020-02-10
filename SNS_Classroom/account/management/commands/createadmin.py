from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from account.models import UserRole

class Command(BaseCommand):
    help = 'Creates admin user'

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating Admin user...")
        flag = True
        while flag:
            self.stdout.write("Enter your username:")
            adminUsername=input()
            if User.objects.filter(username=adminUsername):
                self.stdout.write("That username is already taken!!!")
                flag = True
                self.stdout.write("====================")
            else:
                flag = False

        self.stdout.write("Enter password:")
        adminPassword=input()
        
        admin = User.objects.create_user(username=adminUsername, password=adminPassword, is_superuser=1, is_staff=1)
        adminRole = UserRole.objects.create(user=admin, role="admin")
        self.stdout.write("Admin user created Successfully!!")
