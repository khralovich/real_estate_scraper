class Website:
    def define(self, domain, webpage_filter):
        self.domain = domain
        self.webpage_filter = webpage_filter


morizon = Website()
morizon.define("https://www.morizon.pl", "https://www.morizon.pl/mieszkania/warszawa/?ps%5Bbuild_year_from%5D=1970&ps%5Bliving_area_from%5D=39&ps%5Bmarket_type%5D=2&ps%5Bnumber_of_rooms_from%5D=2&ps%5Bnumber_of_rooms_to%5D=3&ps%5Bprice_from%5D=380000&ps%5Bprice_to%5D=460000&ps%5Bwith_photo%5D=1")

otodom = Website()
otodom.define("https://www.otodom.pl", "https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie,rynek-wtorny/warszawa?distanceRadius=0&page=1&limit=36&priceMax=450000&areaMin=39&ownerTypeSingleSelect=ALL&buildYearMin=1970&roomsNumber=%5BTWO%2CTHREE%5D&locations=%5Bcities_6-26%5D&by=DEFAULT&direction=DESC&viewType=listing")

nieruchomosci_pl = Website()
nieruchomosci_pl.define("https://warszawa.nieruchomosci-online.pl",
                        "https://warszawa.nieruchomosci-online.pl/szukaj.html?3,mieszkanie,sprzedaz,,Warszawa:20571,,,,-450000,39,,,,,,2,,,,,,,,,,,,,,,,,,,,,,,1")


"""
class Player:
    MAX_POSITION = 10
    def __init__(self):
        self.position = 0

    # Add a move() method with steps parameter
    def move(self, steps):
        self.steps = steps
        if self.position + self.steps < Player.MAX_POSITION:
            self.position = self.position + self.steps
        else:
            self.position = Player.MAX_POSITION
        return self.position

    # This method provides a rudimentary visualization in the console
    def draw(self):
        drawing = "-" * self.position + "|" +"-"*(Player.MAX_POSITION - self.position)
        print(drawing)

p = Player(); p.draw()
p.move(4); p.draw()
p.move(5); p.draw()
p.move(3); p.draw()
"""
