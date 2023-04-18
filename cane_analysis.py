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

# write your update damages function here:
def update_damages(lst):
  updated_damages = []
  for damage in lst:
    if damage == 'Damages not recorded':
      updated_damages.append(damage)
    elif 'B' in damage:
      updated_damages.append(float(damage.replace('B','')) * 1000000000)
    elif 'M' in damage:
      updated_damages.append(float(damage.replace('M','')) * 1000000)
  return updated_damages


# write your construct hurricane dictionary function here:
def construct_hurricane_dict(lst_name, lst_mo, lst_yr, lst_wind, lst_area, lst_dam, lst_deaths):
  hurricane_dict = {}
  up_dams = update_damages(lst_dam)
  for i in range(len(lst_name)):
    hurricane_dict[lst_name[i]] = {"Name": lst_name[i], "Month": lst_mo[i], "Year": lst_yr[i], "Max Sustained Wind": lst_wind[i], "Areas Affected": lst_area[i], "Damage": up_dams[i], "Deaths": lst_deaths[i]}
  return hurricane_dict
    
hurricanes_dict = construct_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)


# write your construct hurricane by year dictionary function here:
def hurricanes_by_year(cane_lst):
  yr_dict = {}
  for i in range(len(cane_lst)):
    keys = list(cane_lst.keys())
    current_cane = cane_lst[keys[i]]
    current_year = cane_lst[keys[i]]['Year']
    if current_year not in yr_dict:
      yr_dict[current_year] = [current_cane]
    elif current_year in yr_dict:
      yr_dict[current_year].append(current_cane)
  return yr_dict


# write your count affected areas function here:
def area_count(area_dict):
  area_counts = {}
  for lst in area_dict:
    for area in lst:
      if area not in area_counts:
        area_counts[area] = 1
      if area in area_counts:
        area_counts[area] += 1
  return area_counts


# write your find most affected area function here:
def most_affected_area(area_dict):
  area_counts = area_count(area_dict)
  most_aff_area = ''
  most_num = 0
  for area in area_counts:
    if area_counts[area] > most_num:
      most_aff_area = area
      most_num = area_counts[area]
  return most_aff_area, most_num


# write your greatest number of deaths function here:
def greatest_deaths(canes_list):
  cane_name = ''
  cane_deaths = 0
  for cane in canes_list:
    if canes_list[cane]['Deaths'] > cane_deaths:
      cane_name = cane
      cane_deaths = canes_list[cane]['Deaths']
  return cane_name, cane_deaths


# write your catgeorize by mortality function here:
def mortality_ratings(canes_dict):
  mortality_dict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for cane in canes_dict:
    if canes_dict[cane]['Deaths'] > 10000:
      mortality_dict[5].append(cane)
    elif 1000 < canes_dict[cane]['Deaths'] <= 10000:
      mortality_dict[4].append(cane)
    elif 500 < canes_dict[cane]['Deaths'] <= 1000:
      mortality_dict[3].append(cane)
    elif 100 < canes_dict[cane]['Deaths'] <= 500:
      mortality_dict[2].append(cane)
    elif 0 < canes_dict[cane]['Deaths'] <= 100:
      mortality_dict[1].append(cane)
    else:
      mortality_dict[0].append(cane)
  return mortality_dict


# write your greatest damage function here:
def greatest_damage(canes):
  cane_name = ''
  cane_dam = 0
  for cane in canes:
    if canes[cane]['Damage'] == 'Damages not recorded':
      continue    
    elif int(canes[cane]['Damage']) > cane_dam:
      cane_name = cane
      cane_dam = canes[cane]['Damage']
  return cane_name, cane_dam

print(greatest_damage(hurricanes_dict))


# write your catgeorize by damage function here:
def damage_ratings(canes_dict):
  damage_dict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for cane in canes_dict:
    if canes_dict[cane]['Damage'] == 'Damages not recorded':
      damage_dict[0]
    elif canes_dict[cane]['Damage'] > 50000000000:
      damage_dict[5].append(cane)
    elif 10000000000 < canes_dict[cane]['Deaths'] <= 50000000000:
      damage_dict[4].append(cane)
    elif 1000000000 < canes_dict[cane]['Deaths'] <= 10000000000:
      damage_dict[3].append(cane)
    elif 100000000 < canes_dict[cane]['Deaths'] <= 1000000000:
      damage_dict[2].append(cane)
    elif 0 < canes_dict[cane]['Deaths'] <= 100000000:
      damage_dict[1].append(cane)
    else:
      damage_dict[0].append(cane)
  return damage_dict

print(damage_ratings(hurricanes_dict))
