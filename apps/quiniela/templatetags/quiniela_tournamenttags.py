from django import template

from apps.quiniela.models import OscarCoin

register = template.Library()

@register.simple_tag
def get_score(member_fixture, score_type):
    return member_fixture.get_score(score_type)

@register.simple_tag
def get_oscarcoin():
	ocoin = OscarCoin.objects.all()
	if ocoin:
		ocoin = ocoin[0]
	else:
		ocoin = OscarCoin()
		ocoin.save()
	return ocoin.value