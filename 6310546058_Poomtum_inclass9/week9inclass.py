import csv     
import matplotlib.pyplot as plt
cities_data = []
with open('cities.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities_data.append(r)
# Question 2
print('Question 2')
city_temp_tuple = []
for i in range(len(cities_data)):
    city_temp_tuple.append((cities_data[i]['city'], float(cities_data[i]['temperature'])))
print(city_temp_tuple)
#Question 3
print('Question 3')
def list_countries(cities):
    listcountries = []
    for i in range(len(cities)):
        if cities[i]['country'] not in listcountries:
            listcountries.append(cities[i]['country'])
    
    return listcountries
countries = list_countries(cities_data)
print(len(countries))
print(countries)
#Question 4
print('Question 4')
def compute_ave_country_temp(countries):
    countriesdic = {}
    countryavg = []
    for name in countries:
        avgpercountry = 0
        countcities = 0
        for i in range(len(cities_data)):
            if cities_data[i]['country'] == name:
                avgpercountry += float(cities_data[i]['temperature'])
                countcities += 1
        countryavg.append(avgpercountry/countcities)
    for i in range(len(countries)):
        countriesdic[countries[i]] = countryavg[i]
    
    return countriesdic
print(len(compute_ave_country_temp(countries)))        
print(compute_ave_country_temp(countries))
#Question 5
def read_file(filename):
    cities_data = []
    with open(filename,'r') as f:
        rows = csv.DictReader(f)
        for r in rows:
            cities_data.append(r)
    return cities_data

def extract_to_list(cities_data, value):
    extractedlist = [float(cities_data[i][value]) for i in range(len(cities_data))]
    return extractedlist

cities_data = read_file('cities.csv')
lat = extract_to_list(cities_data,'latitude')
long = extract_to_list(cities_data,'longitude')
temps = extract_to_list(cities_data,'temperature')
high = extract_to_list(cities_data,'highest')
# Plot scatter plot using x = latitude,
# y = temperature,
# color=longitude
plt.scatter(lat,temps,c=long)
# Add x-axis label
plt.xlabel('Latitude')
# Add y-axis label
plt.ylabel('Temperatures')
# Add label for color bar
plt.colorbar().ax.set_title('Longtitude')
# Save plot as image file
plt.savefig('lat_temps_long.png')
# Show plot
plt.show()
plt.scatter(long,temps,c=lat)
plt.xlabel('Longitude')
plt.ylabel('Temperatures')
plt.colorbar().ax.set_title('Latitude')
# Set colormap to the selected one
# See more colormap selection in the reference at the end of
plt.set_cmap('RdBu')
plt.savefig('long_temps_lat.png')
plt.show()
#Question 6
def count_region_freq(cities):
    regionfrequency = []
    region = []
    for i in range(len(cities)):
        if cities[i]['region'] not in region:
            region.append(cities[i]['region'])
    regionlist = [cities_data[i]['region'] for i in range(len(cities))]
    for i in region:
        eachregionfreq = 0
        for j in range(len(regionlist)):
            if i == regionlist[j]:
                eachregionfreq += 1
        regionfrequency.append(eachregionfreq)
    return region, regionfrequency

region_list, region_freq_list = count_region_freq(cities_data)
# Set up bar colors in bar graph
# See more color names in the reference at the end of Exercise 6
my_colors = ['red','blue','green','orange']
# Plot bar graph using x = unique region list
# y = region frequency
# Bar graph color is set to my_colors list
plt.bar(region_list, region_freq_list, color=my_colors)
plt.xlabel('Region')
plt.ylabel('Frequency')
plt.savefig('region_freq.png')
plt.show()
#Question 7
print('Question 7')
def find_lowest_highest_avg_city_temp(cities):
    country = list_countries(cities)
    avgtemp = compute_ave_country_temp(country)
    countriesunique = []
    tempunique = []
    for i in avgtemp:
        countriesunique.append(i)
        tempunique.append(avgtemp.get(i))
    result = []
    result.append(countriesunique[tempunique.index(min(tempunique))])
    result.append(countriesunique[tempunique.index(max(tempunique))])
    return result
print(find_lowest_highest_avg_city_temp(cities_data[:11]))
print(find_lowest_highest_avg_city_temp(cities_data[-10:]))
print(find_lowest_highest_avg_city_temp(cities_data))
#Question 8
def compute_ave_region_highest(cities):
    region = []
    ave_highest_list = []
    for i in range(len(cities)):
        if cities[i]['region'] not in region:
            region.append(cities[i]['region'])
    regionlist = [cities_data[i]['region'] for i in range(len(cities))]
    highest = extract_to_list(cities, 'highest')
    for i in region:
        regionsum = []
        for j in range(len(regionlist)):
            if i == regionlist[j]:
                regionsum.append(int(highest[j]))
        ave_highest_list.append(sum(regionsum) / len(regionsum))
    return region, ave_highest_list

region_list, ave_highest_list = compute_ave_region_highest(cities_data) 
# Set up bar colors in bar graph
# See more color names in the reference at the end of Exercise 6
my_colors = ['brown','purple','pink','black']
# Plot bar graph using x = unique region list
# y = region frequency
# Bar graph color is set to my_colors list
plt.bar(region_list, ave_highest_list, color=my_colors)
plt.xlabel('Region')
plt.ylabel('Average Highest')
plt.savefig('region_freq2.png')
plt.show()