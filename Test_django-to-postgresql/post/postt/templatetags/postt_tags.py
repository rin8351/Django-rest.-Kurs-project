from django import template
from postt.models import *

register=template.Library()

@register.inclusion_tag('postt/script_for_sort_table.html')
def script_for_sort_table():
    return {}