from django import template

register = template.Library()

@register.filter(name='num_to_range') 
def num_to_range(number):
    return range(number)