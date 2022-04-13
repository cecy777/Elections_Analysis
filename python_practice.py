counties = ["Arapahoe","Denver","Jefferson"]
if counties[1]=='Denver':
    print(counties[1])

if counties[3]!='Jefferson':
    print(counties[2])

    
    counties = ["Arapahoe","Denver","Jefferson"]
if "El paso" in counties:
    print("El paso is in the list of counties.")
else:
    print("El paso is not the list of counties.")

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.") 