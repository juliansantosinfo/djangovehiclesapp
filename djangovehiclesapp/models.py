""" docstring """


from django.db import models
from django.db.models.deletion import CASCADE
from django.urls.base import reverse


class VehicleManufacturer(models.Model):
    """ docstring """

    class Meta:
        verbose_name = "Fabricante"
        verbose_name_plural = "Fabricantes"

    name = models.CharField(
        verbose_name="Nome",
        max_length=254,
    )

    def __str__(self) -> str:
        return self.name


class VehicleModel(models.Model):
    """ docstring """

    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"

    manufacturer = models.ForeignKey(
        VehicleManufacturer,
        verbose_name="Fabricante",
        on_delete=CASCADE
    )

    name = models.CharField(
        verbose_name="Nome",
        max_length=254,
    )

    year = models.CharField(
        verbose_name="Ano",
        max_length=4,
    )

    def __str__(self) -> str:
        return self.name


class VehicleVersion(models.Model):
    """ docstring """

    class Meta:
        verbose_name = "Versão"
        verbose_name_plural = "Versões"

    model = models.ForeignKey(
        VehicleModel,
        verbose_name="Modelo",
        on_delete=CASCADE
    )

    name = models.CharField(
        verbose_name="Nome",
        max_length=254,
    )

    def __str__(self) -> str:
        return self.name


class Vehicle(models.Model):
    """ docstring """

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"

    manufacturer = models.ForeignKey(
        VehicleManufacturer,
        verbose_name="Fabricante",
        on_delete=CASCADE
    )

    model = models.CharField(
        VehicleModel,
        verbose_name="Modelo",
        on_delete=CASCADE
    )

    version = models.ForeignKey(
        VehicleVersion,
        verbose_name="Versão",
        on_delete=CASCADE
    )
    

    def __str__(self):
        return self.manufacturer + " | " + self.model + " | " + self.model.year + " | " + self.version
