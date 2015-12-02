from django.db import models
from django.contrib.auth.models import User

classes = models.CharField(max_length=32)
classes.contribute_to_class(User, 'classes')
