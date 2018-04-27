## Quiniela Migrations
python manage.py dumpdata --settings settings.settings --indent 2 quiniela.team -o fixtures/quiniela/teams.json
python manage.py dumpdata --settings settings.settings --indent 2 quiniela.game -o fixtures/quiniela/games.json
python manage.py dumpdata --settings settings.settings --indent 2 quiniela.gameresult -o fixtures/quiniela/gamesresults.json
python manage.py dumpdata --settings settings.settings --indent 2 quiniela.group -o fixtures/quiniela/group.json
python manage.py dumpdata --settings settings.settings --indent 2 quiniela.groupteam -o fixtures/quiniela/groupteam.json
python manage.py dumpdata --settings settings.settings --indent 2 quiniela.memberfixture -o fixtures/quiniela/membersfixtures.json
python manage.py dumpdata --settings settings.settings --indent 2 quiniela.tournament -o fixtures/quiniela/tournaments.json
python manage.py dumpdata --settings settings.settings --indent 2 quiniela.quiniela -o fixtures/quiniela/quinielas.json