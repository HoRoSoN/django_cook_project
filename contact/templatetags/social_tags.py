from django import template
from contact.models import SocialModel, AboutModel

register = template.Library()


@register.simple_tag()
def get_social_links():
    """Вывод ссылок соцю сетей """
    return SocialModel.objects.all()


@register.simple_tag()
def get_about():
    """Вывод about"""
    return AboutModel.objects.last()

