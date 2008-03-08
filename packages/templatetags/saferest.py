"""
"Safely" render reST -> HTML (i.e. don't throw an exception, and fall back to
linebreaks if necessary).
"""

from django import template
from django.contrib.markup.templatetags.markup import restructuredtext
from django.template.defaultfilters import linebreaks

register = template.Library()

@register.filter
def saferest(content):
    try:
        return restructuredtext(content)
    except:
        return linebreaks(content)