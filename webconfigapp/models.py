from django.db import models

IOS_TYPE = [
    ('IOSXE', 'IOSXE'),
    ('IOSXR', 'IOSXR'),
]

class Routers(models.Model):
    hostname = models.CharField(max_length=200, help_text="Host name", blank=False)
    hostip = models.GenericIPAddressField(protocol="both", unpack_ipv4=False)
    ios = models.CharField(max_length=100, choices=IOS_TYPE, default='IOSXE')

    def __str__(self):
        return self.hostip

    class Meta:
        verbose_name = "Routers"
        verbose_name_plural = "Router List"
        db_table = "routers"
