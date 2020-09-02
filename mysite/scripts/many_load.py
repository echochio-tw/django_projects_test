import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import States, Region, Category, Iso, Site

def run():
    fhand = open('unesco/load.csv')
    reader = csv.reader(fhand)
    next(reader) # Advance past the header

    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    for row in reader:

        print(row)

        c, created = Category.objects.get_or_create(name=row[7])
        s, created = States.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])

        try:
            y = int(row[3])
        except:
            y = None

        try:
            la = float(row[4])
        except:
            la = None

        try:
            lo = float(row[5])
        except:
            lo = None

        try:
            ar = float(row[6])
        except:
            ar = None



        site = Site(name=row[0], description=row[1], justification=row[2], year=y, latitude=la, longitude=lo, area_hectares=ar, category=c, states=s, region=r, iso=i)
        site.save()

