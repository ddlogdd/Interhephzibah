# blog/templatetags/custom_filters.py

from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter
def truncate_words(value, num_words):
    try:
        num_words = int(num_words)
    except ValueError:
        return value  # Fail silently if the argument is not an integer

    # Split the content into words
    words = re.findall(r'\w+|\s+|[^\w\s]+', value)
    
    if len(words) <= num_words:
        return value  # No truncation needed

    truncated_words = ''.join(words[:num_words]) + '...'

    return mark_safe(truncated_words)
