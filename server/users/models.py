from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def novels_count(self):
        """ count novels of the user """
        return self.novels.count()

    novels_count.short_description = "Novels Count"