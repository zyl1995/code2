from django import template
from  rango.models import Lategory

register = template.Library()

@register.inclusion_tag('rango/cats.html')
def get_category_list(cat =None):
    return {'cats':Lategory.objects.all(),'act_cat': cat}
