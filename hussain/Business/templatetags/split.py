from django import template                                                                                                                                                        

register = template.Library()

# Create your tests here.
@register.filter(name='split')
def Split(value, key):
    return value.split(key)
