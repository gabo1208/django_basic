## Users an Oauth App Migration
python manage.py dumpdata --settings settings.settings --indent 2 users -o fixtures/users.json
python manage.py dumpdata --settings settings.settings --indent 2 oauth2_provider.application -o fixtures/applications.json

# Memberits Migration
python manage.py dumpdata --settings settings.settings --indent 2 memberits -o fixtures/memberits.json

## Quiniela Migrations
python manage.py dumpdata --settings settings.settings --indent 2 quiniela.team -o fixtures/quiniela_teams.json
python manage.py dumpdata --settings settings.settings --indent 2 quiniela.game -o fixtures/quiniela_games.json
python manage.py dumpdata --settings settings.settings --indent 2 quiniela.gameresult -o fixtures/quiniela_gamesresults.json
python manage.py dumpdata --settings settings.settings --indent 2 quiniela.gamecontext -o fixtures/quiniela_gamescontexts.json
python manage.py dumpdata --settings settings.settings --indent 2 quiniela.memberfixture -o fixtures/quiniela_membersfixtures.json
python manage.py dumpdata --settings settings.settings --indent 2 quiniela.team -o fixtures/quiniela_teams.json
python manage.py dumpdata --settings settings.settings --indent 2 quiniela.tournament -o fixtures/quiniela_tournaments.json
python manage.py dumpdata --settings settings.settings --indent 2 quiniela.quiniela -o fixtures/quiniela_quinielas.json