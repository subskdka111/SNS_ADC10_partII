from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def isEnrolled(module, enrolledModule):
    if module in enrolledModule:
        return "Enrolled"
    else:
        return mark_safe("<a href='enroll/"+str(module.id)+"'>Click to enroll</a>")
