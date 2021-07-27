""" docstring """


from typing import NoReturn
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
        return self.manufacturer.name + " | " + self.name + " | " + self.year


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
        return str(self.model) + " | " + self.name


class Vehicle(models.Model):
    """ docstring """

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"

    model = models.ForeignKey(
        VehicleVersion,
        verbose_name="Modelo",
        on_delete=CASCADE
    )

    board = models.CharField(
        verbose_name="Placa",
        max_length=10
    )

    color = models.CharField(
        verbose_name="Cor",
        max_length=80,
        blank=True,
        null=True
    )

    type_fuel = models.CharField(
        verbose_name="Combustível",
        max_length=2,
        choices=(
            ("ET", "Etanol"),
            ("DS", "Diesel"),
            ("GS", "Gasolina"),
            ("GN", "Gás Natural"),
            ("FX", "Fléx"),
            ("FG", "Fléx/GNV"),
        ),
        blank=True,
        null=True
    )

    renavam = models.CharField(
        verbose_name="Renavam",
        max_length=254,
        blank=True,
        null=True,
    )

    chassi = models.CharField(
        verbose_name="Chassi",
        max_length=254,
        blank=True,
        null=True,
    )

    category = models.CharField(
        verbose_name="Categoria",
        max_length=254,
        blank=True,
        null=True,
    )

    capacity = models.CharField(
        verbose_name="Capacidade",
        max_length=254,
        blank=True,
        null=True,
    )

    power = models.CharField(
        verbose_name="Potência",
        max_length=254,
        blank=True,
        null=True,
    )

    displacement = models.CharField(
        verbose_name="Cilindrada",
        max_length=254,
        blank=True,
        null=True,
    )

    gross_weight = models.FloatField(
        verbose_name="Peso Bruto",
        blank=True,
        null=True,
    )

    engine = models.CharField(
        verbose_name="Motor",
        max_length=254,
        blank=True,
        null=True,
    )

    axles = models.PositiveIntegerField(
        verbose_name="Eixos",
        blank=True,
        null=True,
    )

    capacity = models.CharField(
        verbose_name="Capacidade",
        max_length=254,
        blank=True,
        null=True,
    )

    obs = models.TextField(
        verbose_name="Observações",
        blank=True,
        null=True
    )

    photo = models.ImageField(
        verbose_name="Foto",
        upload_to="",
    )
    
    def __str__(self):
        return str(self.model)
