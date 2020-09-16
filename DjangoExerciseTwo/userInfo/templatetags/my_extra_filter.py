from django import template

register = template.Library()

#using decorator to run a funtion 
@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of arg from the string
    """

    return value.replace(arg,"")

#register.filter('cut',cut)# 1:tag name,2:function
