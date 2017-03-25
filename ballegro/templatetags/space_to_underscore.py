from django import template
register = template.Library()

@register.filter
def space_to_underscore(name):
    return name.replace(' ', '_')
