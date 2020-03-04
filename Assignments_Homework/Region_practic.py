import csv

region_unit = {}
regions_revenue = {}
regions = []

current_region = " "
current_units = 0
current_revenue = 0

f = open ("Region_file.csv", 'rt')


reader = csv.reader(f)
# this is the header, we disregard it.
next(reader)


# Read the input file
for row in reader:
 #   print (row)

    current_region = row[0]
    current_units  = row[1]
    current_revenue = row[2]

    # check to see if the key exists
    if not current_region in region_unit:
        region_unit[current_region] = current_units
    else:
        region_unit[current_region] = \
            int(region_unit[current_region]) \
            + int(current_units)

regions = list(region_unit.keys())

print("All the regions found are: ", end="")
print(regions)

for r in regions:
    print(r, end=", ")


print ("Totals per region")
for r in regions:
    print(r)
    print("total units ofr region: " + str(region_unit[r]))