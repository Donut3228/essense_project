from django import template

register = template.Library()


@register.filter
def remainder(value):
    result = str.lower(value)
    return result
