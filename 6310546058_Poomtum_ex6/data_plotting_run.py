import data_processing as dp
import matplotlib.pyplot as plt

# Scatter plot of cities showing latitudes versus temperatures
x = []
y = []
for city in dp.cities_data:
    x.append(float(city['latitude']))
    y.append(float(city['temperature']))
plt.xlabel('latitude')
plt.ylabel('temperature')
plt.scatter(x, y,c=x)
plt.show()

# Bar chart showing average temperatures of all cities in each country
bars = [] # list of countries
temperature = [] # average temperature of each country
dict = dp.average_country_temp(dp.cities_data)
for key, value in dict.items():
    bars.append(key)
    temperature.append(value)

numbars = len(bars)
width = .75
plt.bar(range(numbars), temperature, width, align='center')
plt.xlabel('country')
plt.ylabel('temperature')
plt.xticks(range(numbars), bars, rotation='vertical')
print(bars)
print(temperature)
plt.show()

# Pie chart showing number of EU countries versus non-EU countries
numEU = 0
numNotEU = 0
for country in dp.countries_data:
    if country['EU'] == 'yes':
        numEU += 1
    else:
        numNotEU +=1
plt.pie([numEU, numNotEU], labels=['EU','not EU'], autopct='%1.1f%%')
plt.show()

# Bar chart showing population of countries that are in EU but do not have coastline

# your code here
info = dp.population_countries_no_coastline_in_EU(dp.countries_data)
country = [] ; popu = []
for i, v in info.items():
    country.append(i)
    popu.append(v)
numbars = len(country)
width = .75
plt.bar(range(numbars), popu, width, align='center')
plt.xlabel('country')
plt.ylabel('population')
plt.xticks(range(numbars), country, rotation='vertical')
print(country)
print(popu)
plt.show()
# Pie chart showing number of EU cities versus non-EU cities

# your code here
numEU = 0
for country in dp.countries_data:
    if country['EU'] == 'yes':
        numEU += 1
plt.pie([numEU, len(dp.countries_data) - numEU], labels=['EU','not EU'], autopct='%1.1f%%')
plt.show()
# Scatter plot of players showing minutes played versus passes made;
# color each player based on their position (goalkeeper, defender, midfielder, forward)

# your code here
goalkeeper = [(int(dp.players_data[i]['minutes']),int(dp.players_data[i]['passes'])) for i in range(len(dp.players_data)) if dp.players_data[i]['position'] == 'goalkeeper']
defender = [(int(dp.players_data[i]['minutes']),int(dp.players_data[i]['passes'])) for i in range(len(dp.players_data)) if dp.players_data[i]['position'] == 'defender']
midfielder = [(int(dp.players_data[i]['minutes']),int(dp.players_data[i]['passes'])) for i in range(len(dp.players_data)) if dp.players_data[i]['position'] == 'midfielder']
forward = [(int(dp.players_data[i]['minutes']),int(dp.players_data[i]['passes'])) for i in range(len(dp.players_data)) if dp.players_data[i]['position'] == 'forward']
plt.xlabel('Minutes')
plt.ylabel('Passes')
color = ['red', 'green', 'blue', 'pink']
position = [goalkeeper,defender,midfielder,forward]
positionname = ['goalkeeper','defender','midfielder','forward']
for i in range(len(color)):
    plt.scatter(*zip(*position[i]), c=color[i], label= positionname[i])
plt.legend()
plt.show()
# Bar chart showing average number of passes made by each player postion (defender, midfielder, forward, goalkeeper)

# your code here
position = ['defender','midfielder','forward','goalkeeper']
passes = dp.average_passes(dp.players_data)
numbars = len(position)
width = .75
plt.bar(range(numbars), passes, width, align='center')
plt.xlabel('position')
plt.ylabel('passes')
plt.xticks(range(numbars), position, rotation='vertical')
print(position)
print(passes)
plt.show()

# Bar chart showing the survival rate in each passenger class; the three bars should be labeled 'first', 'second', 'third'

# your code here
classes = [1,2,3]
rate = [dp.class_survival_rate(classes[i],dp.titanic_data) for i in range(len(classes))]
numbars = len(classes)
width = .75
plt.bar(range(numbars), rate, width, align='center')
plt.xlabel('classes')
plt.ylabel('survival rate (%)')
plt.xticks(range(numbars), ['first','second','third'], rotation='vertical')
print(classes)
print(rate)
plt.show()
# Pie chart showing the number of male survivors versus female survivors

# your code here
gender = ['M', 'F']
num = [dp.gender_survival_number(i,dp.titanic_data) for i in gender]
plt.pie([num[0], num[1]], labels=['M','F'], autopct='%1.1f%%')
plt.show()