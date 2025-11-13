import webbrowser

def validator(func):
    def wrapper(url):
        if "." in url:
            func(url)
        else:
            print("Invalid URL")
    return wrapper

@validator
def openUrl(url):
    webbrowser.open(url)

openUrl("http://google.com")
# class MainBuilding:
#     year = None
#     city = None
#     def __init__(self, year, city):
#         self.year = year
#         self.city = city
#     def build_info(self):
#         print("Year:",self.year, ". City:", self.city)
#
# class SchoolBuilding(MainBuilding):
#
#     pupils = 10000
#
#     def __init__(self, pupils, year, city):
#         super(SchoolBuilding, self).__init__(year, city)
#         self.pupils = pupils
#         print("Pupils:", self.pupils, ". Year:", self.year, ". City:", self.city)
# building = MainBuilding(2015, "Astana")
# building.build_info()
# school = SchoolBuilding(10000, 2020, "Astana")
# school.build_info()