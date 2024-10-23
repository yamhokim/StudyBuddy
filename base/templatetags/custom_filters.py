from django import template

register = template.Library()

@register.filter
def trim_description(value, word_limit=20):
    words = value.split()
    if len(words) > word_limit:
        return ' '.join(words[:word_limit]) + '...'
    
    return value