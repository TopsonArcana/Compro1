import urllib.request
import csv
import codecs

csv_url = "http://eduserv.ku.ac.th/EPL2020.csv"


class Football:
    def __init__(self, short_name ="", name = "", wins=0, draws=0, loses=0):
        self.__team_name = name
        self.__team_short = short_name
        self.__num_wins = wins
        self.__num_draws = draws
        self.__num_loses = loses

    @property
    def name_short(self):
        return self.__team_short

    @property
    def win(self):
        return self.__num_wins

    @win.setter
    def win(self, value):
        self.__num_wins = value

    @property
    def draw(self):
        return self.__num_draws

    @draw.setter
    def draw(self, value):
        self.__num_draws = value

    @property
    def lose(self):
        return self.__num_loses

    @lose.setter
    def lose(self, value):
        self.__num_loses = value

    def __str__(self):
        return f"{self.__team_short},{self.__team_name},{self.__num_wins},{self.__num_draws},{self.__num_loses}"

    def won(self, team):
        self.__num_wins += 1
        team.__num_loses += 1

    def drew(self, team):
        self.__num_draws += 1
        team.__num_draws += 1

    def losed(self, team):
        self.__num_loses += 1
        team.__num_wins += 1


class FileReadFromURL:
    def __init__(self):
        self.__data = []

    @property
    def file_data(self):
        return self.__data

    def read(self, url):
        data_byte = urllib.request.urlopen(url)
        data_str = csv.reader(codecs.iterdecode(data_byte, 'utf-8'))
        data = []
        for i in data_str:
            data.append(i)
        for i in range(1, len(data)):
            self.__data.append(Football(data[i][0], data[i][1], int(data[i][2]), int(data[i][3]), int(data[i][4])))

    def __str__(self):
        return "\n".join([str(i) for i in self.__data])

a = FileReadFromURL()
a.read(csv_url)
print(a)