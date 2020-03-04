import csv

# Define dictionary
region_unit = {}
regions_revenue = {}
regions = []                                 # list

# Variables
current_region = " "
current_units = 0
current_revenue = 0

#current_ave_per_unit = 0


f = open ("500000 Sales Records.csv","rt")   # open file
reader = csv.reader(f)                       # read input file
next(reader)                                 # disregard header

# Loop into the input file
for row in reader:

    current_region = row[0]                  # Get the first row which is #Region
    current_units  = row[8]                  # Get the eighth row which is #unit
    current_revenue = row[11]                # Get the twelves row with is #revenu

  # check to see if the key exists
    if not current_region in region_unit:
        region_unit[current_region] = current_units
    else:
        region_unit[current_region] = \
            region_unit[current_region] \
           + str(current_units)

regions= list(region_unit.keys())

if not current_region in regions_revenue:
    regions_revenue[current_revenue] = current_revenue
else:
    regions_revenue[current_region] = \
    regions_revenue[current_revenue] + str(current_revenue)



# Display the header
print("All the regions found are: ", end="")


for r in regions:
  print (r)



print("\nTOTALS UNITS PER REGION\n")

for a in regions:
    print(a)
    print("total units of region:" + str(region_unit[a]))

print("\nTotal Revenue per region\n")

for t in regions:
    print (t)
    print("Total revenue of region " + str(regions_revenue[t]))
    print()
