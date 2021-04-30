from django import template
from markdown import markdown
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter("markdown", is_safe=True)
def to_markdown(value):
    return mark_safe(markdown(value))