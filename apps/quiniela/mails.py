import os
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

users = User.objects.all()[1:]
subject = 'Get ready to Russia 2018 World Cup!'
from_email = 'admin@memberit.com'
for user in users:
  ctx = {'user': user}
  message = render_to_string(os.path.abspath('.')+'/apps/users/templates/quiniela_reminder.html', ctx)
  mail = EmailMultiAlternatives(subject, 'Error sending message.', from_email, [user.email])
  mail.attach_alternative(message, "text/html")
  mail.send()