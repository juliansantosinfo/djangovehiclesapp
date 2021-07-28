""" docstring """


import os, csv
from pathlib import Path
from django.db.models import Q
from django.core.management.base import BaseCommand, CommandError
from ...models import VehicleManufacturer, VehicleModel, VehicleVersion, Vehicle


class Command(BaseCommand):
    """ docstring """

    help = 'Generate default database.'

    def handle(self, *args, **options):

        file = os.path.join(Path(__file__).resolve().parent, 'assets', 'deafult_database.csv')
        
        with open(file, 'r', newline='', encoding="utf8") as csvfile:

            firstline = True
            csv_reader = csv.reader(csvfile, delimiter=';')

            for line in csv_reader:
                
                if firstline:
                    firstline = False
                    continue

                if len(line) != 4:
                    continue

                # Manufacturer
                manufacturer = VehicleManufacturer.objects.filter(name=line[0]).first()
                if not manufacturer:
                    manufacturer = VehicleManufacturer()
                    manufacturer.name = line[0]
                    manufacturer.save()

                # Model
                model = VehicleModel.objects.filter( Q(name=line[1]) & Q(year=line[2]) ).first()
                if not model:
                    model = VehicleModel()
                    model.manufacturer = manufacturer
                    model.name = line[1]
                    model.year = line[2]
                    model.save()

                versions = line[3].split("|")

                for version_name in versions:

                    v = VehicleVersion.objects.filter(Q(model=model) & Q(name=version_name)).first()
                    if not v:
                        version = VehicleVersion()
                        version.model = model
                        version.name = version_name
                        version.save()
                        
                        self.stdout.write(self.style.NOTICE('Added vehicle ' + str(version.model) + ' | ' + version_name))

        self.stdout.write(self.style.SUCCESS('Standard database started successfully.'))
