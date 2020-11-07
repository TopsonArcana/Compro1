import csv

# open Cities.csv file with csv.DictReader and read its content into a list of dictionary, cities_data
cities_data = []
with open('Cities.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities_data.append(r)
# open Countries.csv file with csv.DictReader and read its content into a list of dictionary, countries_data
countries_data = []
with open('Countries.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries_data.append(r)


def min_max_temp(cities_data):
    """Returns a list whose first and second elements are the min and the max temperatures of all the
    cities in cities_data.
    """
    temps = []
    for r in cities_data:
        temps.append(float(r['temperature']))
    return [min(temps), max(temps)]


def country_list(cities_data):
    """Returns a list of all the countries represented in cities_data.
    """
    countries = []
    for r in cities_data:
        if r['country'] not in countries:
            countries.append(r['country'])
    return countries


def average_country_temp(cities_data):
    """
    Return a dictionary whose key:value pair is country name:its average temp. The size of the
    returned dictionary must equal the number of countries represented.
    """
    d = dict()
    for country in country_list(cities_data):
        t = [float(r['temperature'])
             for r in cities_data if r['country'] == country]
        d[country] = sum(t)/len(t)
    return d


def country_max_diff_temperature(cities_data):
    """Returns a tuple with information about a country whose minimum and maximum city temperatures differ the most in the following format: (the country whose minimum and maximum city temperatures differ the most, min temperature, max temperature, max temperature - min temperature)
    """
    l = []
    l2 = []
    for country in country_list(cities_data):
        t = [float(r['temperature'])
             for r in cities_data if r['country'] == country]
        l.append(max(t) - min(t))
        l2.append([min(t), max(t)])
    return (country_list(cities_data)[l.index(max(l))], l2[l.index(max(l))][0], l2[l.index(max(l))][1], max(l))


def northern_sounthern_most_cities(cities_data):
    """Returns a list of tuples with information about the northernmost and southernmost cities together with their associated countries in the following format: [(northernmost city, its country), (southernmost city, its country)]
    """
    ns = []
    for r in cities_data:
        ns.append(r['latitude'])
    return [(cities_data[ns.index(max(ns))]['city'], cities_data[ns.index(max(ns))]['country']), (cities_data[ns.index(min(ns))]['city'], cities_data[ns.index(min(ns))]['city'])]


def population_countries_no_coastline_in_EU(countries_data):
    """Returns a dictionary whose keys are countries in EU but do not have coastline; the value associated with each key is the population of that country
    """
    d = dict()
    for r in countries_data:
        if (r['EU'] == 'yes') and (r['coastline'] == 'no'):
            d[r['country']] = float(r['population'])
    return d


def cities_in_EU(cities_data, countries_data):
    """Returns a dictionary whose key:value pair is "name of city":"EU membership", e.g., "Graz":"yes" or 'Aalborg':'no'; the size of the dictionary must equal the number of cities represented in cities_data
    """
    # Hint:
    # Use nested for in loops to generate the dictionary:
    #
    # for city in cities_data:
    #    for country in countries_data:
    d = dict()
    for city in cities_data:
        for country in countries_data:
            if city['country'] == country['country']:
                d[city['city']] = country['EU']
    return d


def average_EU_city_temperature(cities_data, countries_data):
    """Returns a tuple with two elements: (the average temperature of all the cities in EU countries, the average temperature of all the cities not in EU countries)
    """
    avginEU = []
    avgnotinEU = []
    citiesEU = cities_in_EU(cities_data, countries_data)
    for index, city in enumerate(citiesEU):
        if citiesEU.get(city) == 'yes':
            avginEU.append(float(cities_data[index]['temperature']))
        else:
            avgnotinEU.append(float(cities_data[index]['temperature']))
    return (sum(avginEU) / len(avginEU), sum(avgnotinEU) / len(avgnotinEU))


# open Players.csv file with csv.DictReader and read its content into a list of dictionary, players_data
players_data = []
with open('Players.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        players_data.append(r)

# open Teams.csv file with csv.DictReader and read its content into a list of dictionary, teams_data
teams_data = []
with open('Teams.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        teams_data.append(r)


def average_passes(players_data):
    """Returns a tuple with four elements; the first, second, third, and fourth elements show the average number of passes made by defenders, midfielders, forwards, and goalkeepers, respectively
    """
    l = []
    for role in ['defender', 'midfielder', 'forward', 'goalkeeper']:
        temp = 0
        for player in players_data:
            if role == player['position']:
                temp += int(player['passes'])
        l.append(temp)
    return (l[0], l[1], l[2], l[3])


def max_GF_GA_ratio(teams_data):
    """Returns the string name of a team with highest ratio of goalsFor to goalsAgainst
    """
    ratio = []
    for team in teams_data:
        ratio.append(int(team['goalsFor']) / int(team['goalsAgainst']))
    return teams_data[ratio.index(max(ratio))]['team']


def whose_player_list(players_data, teams_data):
    """Returns a list of tuples; each tuple has information about a player who is on a team ranked in the top 20, plays less than 200 minutes and makes more than 100 passes; the format for each tuple is (player's surname, team played for, team ranking, minutes played, number of passes)
    """
    team20 = []
    wantplayer = []
    for i in teams_data:
        if int(i['ranking']) > 20:
            break
        team20.append(i['team'])
    for player in players_data:
        if (player['team'] in team20) and (int(player['minutes']) < 200) and (int(player['passes']) > 100):
            wantplayer.append((player['surname'], player['team'], int(teams_data[team20.index(
                player['team'])]['ranking']), int(player['minutes']), int(player['passes'])))
    return wantplayer
    # Reminder: Convert minutes and passes to integers before comparing to values


def team_list_passes_per_minute(players_data, teams_data):
    """Returns a list of tuples; each tuple has information about a team and its passes per minute value generated by its players
    """
    l = []
    for team in teams_data:
        passes = 0
        minutes = 0
        for player in players_data:
            if team['team'] == player['team']:
                passes += int(player['passes'])
                minutes += int(player['minutes'])
        l.append((team['team'], passes / minutes))
    return l


# open Titanic.csv file with csv.DictReader and read its content into a list of dictionary, titanic_data
titanic_data = []
with open('Titanic.csv') as f:
    rows = csv.DictReader(f)
    for r in rows:
        titanic_data.append(r)


def number_married_women_embarked(place_embarked, age_threshold, titanic_data):
    """Returns the number of married women over age_threshold embarked at place_embarked

    Your test code must include at least five test cases with different combinations of place_embarked and age_threshold
    >>> number_married_women_embarked('Southampton', 20, titanic_data)
    80
    >>> number_married_women_embarked('Cherbourg', 15, titanic_data)
    20
    >>> number_married_women_embarked('Queenstown', 30, titanic_data)
    2
    >>> number_married_women_embarked('Southampton', 40, titanic_data)
    27
    >>> number_married_women_embarked('Cherbourg', 50, titanic_data)
    4
    """
    num = 0
    for marriedwoman in titanic_data:
        if ('Mrs.' in marriedwoman['first'] and marriedwoman['age'] != ''
        and int(marriedwoman['age']) > age_threshold and marriedwoman['embarked'] == place_embarked):
            num += 1
    return num


def class_survival_rate(passenger_class, titanic_data):
    """Returns the survival rate of a given passenger_class

    Your test case must test all the three passenger classes
    >>> class_survival_rate(1, titanic_data)
    15.26374859708193
    >>> class_survival_rate(2, titanic_data)
    9.764309764309765
    >>> class_survival_rate(3, titanic_data)
    13.35578002244669
    """
    sur = 0
    for passenger in titanic_data:
        if int(passenger['class']) == passenger_class:
            if passenger['survived'] == 'yes':
                sur += 1
    return (sur / len(titanic_data)) * 100


def gender_survival_number(passenger_gender, titanic_data):
    """Returns the number of survivors for a given gender, M (male) or F (female)

    Your test case must test both genders
    >>> gender_survival_number('M',titanic_data)
    109
    >>> gender_survival_number('F',titanic_data)
    233
    """
    num = 0
    for passenger in titanic_data:
        if passenger['gender'] == passenger_gender:
            if passenger['survived'] == 'yes':
                num += 1
    return num


def twin_list(titanic_data):
    """Returns a list of tuples of pairs of passengers who are likely to be twin children, i.e., same last name, same age, same place of embarkment, and age is under 18; each tuple has the following format: (person1's "last name" + "first name", person2's "last name" + "first name")
    """
    listtwin = []
    for i in range(len(titanic_data)):
        if i < (len(titanic_data) - 1):
            if (titanic_data[i]['last'] == titanic_data[i+1]['last']) and titanic_data[i]['age'] == titanic_data[i + 1]['age'] and titanic_data[i]['embarked'] == titanic_data[i + 1]['embarked'] and titanic_data[i]['age'] != '':
                if float(titanic_data[i]['age']) < 18:
                    listtwin.append((titanic_data[i]['first'][:titanic_data[i]['first'].find(".") + 1] + titanic_data[i]['last'] + " " + titanic_data[i]['first'][titanic_data[i]['first'].find('.') + 1:],
                    titanic_data[i+1]['first'][:titanic_data[i+1]['first'].find(".")+1]+titanic_data[i+1]['last']+" "+titanic_data[i+1]['first'][titanic_data[i+1]['first'].find('.')+1:]))
    return listtwin
