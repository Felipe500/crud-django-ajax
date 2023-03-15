from django.utils.translation import gettext_lazy as _
from django.db import models
from .managers import ClientManager
from app.common.models import Base


class Client(Base):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30, null=True, blank=True)
    date_birth = models.DateField(blank=True, null=True)
    cell_phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(verbose_name=_('Ativo?'), default=True)

    objects = ClientManager()

    class Meta:
        verbose_name = _('Cliente')
        verbose_name_plural = _('Clientes')
        ordering = ['name']

    def __str__(self):
        if self.surname:
            return self.name + ' ' + self.surname
        return self.name + ' '

    @property
    def full_name(self):
        if self.surname:
            return self.name + ' ' + self.surname
        return self.name + ' '




