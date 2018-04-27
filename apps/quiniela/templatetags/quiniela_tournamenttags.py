from django import template

register = template.Library()

@register.simple_tag
def get_score(member_fixture, score_type):
    return member_fixture.get_score(score_type)