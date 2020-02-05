STAFF_ROLES = ("admin", "teacher")

def checkRole(request, role):
    if request.user.is_authenticated:
        if request.user.userrole.role in role:
            return True
    return False
