import requests

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


@register.simple_tag
def get_oscarcoin_date():
        ocoin = OscarCoin.objects.all()
        if ocoin:
                ocoin = ocoin[0]
        else:
                ocoin = OscarCoin()
                ocoin.save()
        return str(ocoin.modified).split('.')[0]


@register.simple_tag
def get_btc():
    btc = requests.get('https://api.coinmarketcap.com/v1/ticker/bitcoin/').json()[0]
    return str(btc['price_usd']) + ' ' + str(btc['percent_change_1h']) + '% last hour'
