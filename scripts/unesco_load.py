import csv


from unesco.models import Site,Category,Region,Iso,States

def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    # print(next(reader))
    next(reader)  # skip head section
    
    # delete existing entries
    Site.objects.all().delete()
    States.objects.all().delete()
    Category.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()

    for row in reader:
        print(row)
        cat,created = Category.objects.get_or_create(name=row[7])
        stat,created = States.objects.get_or_create(name=row[8])
        reg,created = Region.objects.get_or_create(name=row[9])
        iso,created = Iso.objects.get_or_create(name=row[10])
        try:
            lt = int(row[4])
        except:
            lt= None
        
        try:
            alt = int(row[5])
        except:
            alt= None
        
        try:
            ah = int(row[6])
        except:
            ah= None
        site= Site(name=row[0],year=row[3],
            description=row[1], justification=row[2],longitude=lt,
            latitude=alt, area_hectares=ah, category=cat,
            state=stat,region=reg,iso=iso)
        site.save()