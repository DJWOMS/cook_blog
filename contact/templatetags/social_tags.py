from django import template
from contact.models import Social, About


register = template.Library()


@register.simple_tag()
def get_social_links():
    """Вывод ссылок соц. сетей"""
    return Social.objects.all()


@register.simple_tag()
def get_about():
    """Вывод about"""
    return About.objects.last()
