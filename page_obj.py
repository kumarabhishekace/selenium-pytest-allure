
class makemytrip_obj():
    def __init__(self):
        self.url = 'https://www.makemytrip.com/'
    
    def flight_page(self):
        self.from_city = "//*[@id='fromCity']"
        self.to_city = "//*[@id='toCity']"
        self.date = ""
