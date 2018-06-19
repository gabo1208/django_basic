## Users an Oauth App Migration
python manage.py dumpdata --settings settings.settings --indent 2 users -o fixtures/users.json
python manage.py dumpdata --settings settings.settings --indent 2 oauth2_provider.application -o fixtures/applications.json

# Memberits Migration
python manage.py dumpdata --settings settings.settings --indent 2 memberits -o fixtures/memberits.json
