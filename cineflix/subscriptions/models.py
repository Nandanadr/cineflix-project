from django.db import models

from multiselectfield import MultiSelectField

# Create your models here.

from movies.models import BaseClass

class DeviceChoices(models.TextChoices):

    PHONE = 'phone','phone'

    TABLET = 'tablet','tablet'

    TV = 'tv','tv'

    LAPTOP = 'laptop', 'laptop'

class QualityChoices(models.TextChoices):

    P480 = '480p','480p'

    P1000 = 'upto 1000','upto 1000'

    P4K = 'upto 4k','upto 4k'

class ScreenOrDrownloadDeviceChoices(models.IntegerChoices):

    ONE = 1,'1'

    TWO = 2,'2'

    FOUR = 4,'4'

class SubscriptionPlans(BaseClass):

    name = models.CharField(max_length=25)

    amount = models.FloatField()

    devices = MultiSelectField(choices=DeviceChoices.choices)

    quality = models.CharField(max_length=30,choices=QualityChoices.choices)

    no_of_screens = models.IntegerField(choices=ScreenOrDrownloadDeviceChoices.choices)

    download_devices = models.IntegerField(choices=ScreenOrDrownloadDeviceChoices.choices)

    class Meta:

        verbose_name = 'subscription plans'

        verbose_name_plural ='subscription plans'

    def __str__(self):

        return self.name

   



