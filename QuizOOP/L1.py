import time


def current_time():
    return time.time()


class BusDatabase:
    def __init__(self):
        self.__route = []

    @property
    def route(self):
        return self.__route

    def add_route(self):
        route = input("Enter route name : ")
        self.__route.append([route])

    def choose_route(self):
        select_route = int(input("Enter a route number: "))
        select_route -= 1
        return self.__route[select_route]

    def add_bus(self, bus, route):
        bus.bus_code = input("Bus Code: ")
        route.append(bus)

    def __str__(self):
        return "\n".join(["Route {0} : {1}".format(self.__route.index(i) + 1, "".join(i[0])) for i in self.__route])


class Bus:
    def __init__(self):
        self.__start = 0
        self.__total_time = 0
        self.__present_time = 0
        self.__bus_code = ""
        self.__bus_status = "Stop"

    @property
    def bus_status(self):
        return self.__bus_status

    @property
    def present_time(self):
        return self.__present_time

    @present_time.setter
    def present_time(self, value):
        self.__present_time = value

    @bus_status.setter
    def bus_status(self, value):
        self.__bus_status = value

    @property
    def total_time(self):
        return self.__total_time

    @total_time.setter
    def total_time(self, value):
        self.__total_time = value

    def start(self):
        self.__start = current_time()

    def elapse_time(self):
        self.__present_time = int(current_time() - self.__start)

    def final_time(self):
        self.__total_time = int(current_time() - self.__start)

    @property
    def bus_code(self):
        return self.__bus_code

    @bus_code.setter
    def bus_code(self, value):
        self.__bus_code = value

    def __str__(self):
        return ("{0} is {1} (Current {2} secs / All {3} secs)").format(self.__bus_code, self.__bus_status,
                                                                       self.__present_time, self.__total_time)


class Application:
    def __init__(self):
        self.database = BusDatabase()

    def bus_menu(self, select_route):
        while True:
            menu = input("(a)dd bus, (p)rint, (r)un/stop, (m)ain menu: ")
            if menu == "a":
                self.database.add_bus(Bus(), select_route)
            elif menu == "p":
                print(f"Route {self.database.route.index(select_route) + 1} : {select_route[0]}")
                for i in range(1, len(self.database.route[self.database.route.index(select_route)])):
                    self.database.route[self.database.route.index(select_route)][i].present_time = \
                    self.database.route[self.database.route.index(select_route)][i].elapse_time()
                    print(f"{i}.{self.database.route[self.database.route.index(select_route)][i].__str__()}")
            elif menu == "r":
                bus_num = int(input("Bus Number? : "))
                if self.database.route[self.database.route.index(select_route)][bus_num].bus_status == "Stop":
                    self.database.route[self.database.route.index(select_route)][bus_num].start()
                    self.database.route[self.database.route.index(select_route)][bus_num].bus_status = "Running"
                else:
                    self.database.route[self.database.route.index(select_route)][bus_num].present_time = 0
                    self.database.route[self.database.route.index(select_route)][bus_num].total_time += \
                    self.database.route[self.database.route.index(select_route)][bus_num].final_time()
                    self.database.route[self.database.route.index(select_route)][bus_num].bus_status = "Stop"
            elif menu == "m":
                break

    def main_menu(self):
        while True:
            menu = input("(n)ew Route , (s)how, (c)hoose, (q)uit: ")
            if menu == "n":
                self.database.add_route()
                print(self.database)
            elif menu == "s":
                print(self.database)
            elif menu == "c":
                a = self.database.choose_route()
                self.bus_menu(a)
            elif menu == "q":
                break


app = Application()
app.main_menu()
