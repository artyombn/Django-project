from django import template

register = template.Library()

@register.filter
def check_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()