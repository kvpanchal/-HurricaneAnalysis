# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# Update Recorded Damages

conversion = {"M": 1000000,
              "B": 1000000000}
updated_damages = []
def update_damages(damages):
  
      
  for damage in damages:
    if damage == "Damages not recorded":
      updated_damages.append(damage)
          
    if damage[-1] == "M":
      updated_damages.append(float(damage[0:damage.find("M")]) * conversion["M"])
    if damage[-1] == "B":
      updated_damages.append(float(damage[0:damage.find("B")]) * conversion["B"])
  return updated_damages
# test function by updating damages
print(update_damages(damages))


# Create and view the hurricanes dictionary

hurricanes = dict()

def hurricate_dic(names, months, years, max_sustained_winds,areas_affected, updated_damages, deaths):
    
    numbers_hurricanes = len(names)
    
    for i in range(numbers_hurricanes):
        hurricanes[names[i]] = {"Name": names[i],
        "Month": months[i],
        "Year": years[i],
        "Max Sustained Wind": max_sustained_winds[i],
        "Areas Affected": areas_affected[i],
        "Damage": updated_damages[i],
        "Deaths": deaths[i]}
    return hurricanes
  
print(hurricate_dic(names, months, years, max_sustained_winds,areas_affected, updated_damages, deaths))


# Organizing by Year

def hurricanes_by_year(hurricanes):
    dic_year = dict()
    
    for val in hurricanes:
        current_year = hurricanes[val]["Year"]
        current_hcane = hurricanes[val]
        
        if current_year not in dic_year:
            dic_year[current_year] = current_hcane
        else:
            dic_year[current_year].update(current_hcane)
    return dic_year


# create a new dictionary of hurricanes with year and key

print(hurricanes_by_year(hurricanes))


# find most frequently affected area and the number of hurricanes involved in

def count_affected_areas(hurricanes):
    affected_areas_count = dict()
    for cane in hurricanes:
        for area in hurricanes[cane]['Areas Affected']:
            if area not in affected_areas_count:
                affected_areas_count[area] = 1
            else:
                affected_areas_count[area] += 1
    return affected_areas_count

areas_affected = count_affected_areas(hurricanes)


# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths

def  most_affected_area(areas_affected):
  max_area = 'Central America'
  max_area_count = 0
  for area in areas_affected:
    if areas_affected[area] > max_area_count:
      max_area = area
      max_area_count = areas_affected[area]
  return max_area, max_area_count
    
print(most_affected_area(areas_affected))


# Rating Hurricanes by Mortality

def number_of_mortality(hurricanes):
  max_mortality = 0
  for cane in hurricanes.values():
    if cane["Deaths"] > max_mortality:
      max_mortality = cane["Deaths"]
  return max_mortality
  
print(number_of_mortality(hurricanes))

# categorize hurricanes in new dictionary with mortality severity as key

# find highest damage inducing hurricane and its total cost

def mortality_scale(hurricanes):
  mortality_scale = {0: [ ],
                   1: [ ],
                   2: [ ],
                   3: [ ],
                   4: [ ],
                   5: [ ]}
  for key, cane in hurricanes.items():
    if cane["Deaths"] > 10000:
      mortality_scale[5].append(cane)
    elif cane["Deaths"] > 1000 and cane["Deaths"] <= 10000:
      mortality_scale[4].append(cane)
    elif cane["Deaths"] > 500 and cane["Deaths"] <= 1000:
      mortality_scale[3].append(cane)
    elif cane["Deaths"] > 100 and cane["Deaths"] <= 500:
      mortality_scale[2].append(cane)
    elif cane["Deaths"] > 0 and cane["Deaths"] <= 100:
      mortality_scale[1].append(cane)
    else:
      mortality_scale[0].append(cane)
            
  return mortality_scale

print(mortality_scale(hurricanes))
# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def highest_damage(hurricanes):
  high_damage = 0
  high_damage_cane = "Cuba I"
  for key, cane in hurricanes.items():
    if cane["Damage"] == "Damages not recorded":
      continue
    elif cane["Damage"] > high_damage:
      high_damage = cane["Damage"]
      high_damage_cane = key
  return high_damage_cane, high_damage
  
print(highest_damage(hurricanes))
  
# categorize hurricanes in new dictionary with damage severity as key

def damage_scale(hurricanes):
  damage_scale_dic = {0: [ ],
                   1: [ ],
                   2: [ ],
                   3: [ ],
                   4: [ ],
                   5: [ ]}
  for key, cane in hurricanes.items():
    if cane["Damage"] == "Damages not recorded":
      continue
    elif cane["Damage"] > 50000000000:
      damage_scale_dic[5].append(cane)
    elif cane["Damage"] > 10000000000 and cane["Damage"] <= 50000000000:
      damage_scale_dic[4].append(cane)
    elif cane["Damage"] > 1000000000 and cane["Damage"] <= 10000000000:
      damage_scale_dic[3].append(cane)
    elif cane["Damage"] > 100000000 and cane["Damage"] <= 1000000000:
      damage_scale_dic[2].append(cane)
    elif cane["Damage"] > 0 and cane["Damage"] <= 100000000:
      damage_scale_dic[1].append(cane)
    else:
      damage_scale_dic[0].append(cane)
            
  return damage_scale_dic

print(damage_scale(hurricanes))
