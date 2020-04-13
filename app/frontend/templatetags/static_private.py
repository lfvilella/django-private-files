from django import template
from django.conf import settings


register = template.Library()


@register.simple_tag
def static_private(static_path):
    return settings.PRIVATE_STATIC_URL + static_path
