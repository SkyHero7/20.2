from django import template

register = template.Library()

@register.filter(name='media_url')
def media_url(image_url):
    if image_url:
        return f'/media/{image_url}'
    return '#'