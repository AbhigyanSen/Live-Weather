from requests_html import HTMLSession

Session = HTMLSession()
# Query = 'London'
Query = input("Enter Place: ")
Query = Query[0].upper() + Query[1:]

URL = f'https://www.google.com/search?q=weather+{Query}'
Request = Session.get(URL, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'})

Temperature = Request.html.find('span#wob_tm', first=True).text
Degree = Request.html.find('div.vk_bk.wob-unit', first=True).find('span.wob_t', first=True).text
Description = Request.html.find('span#wob_dc', first=True).text

print(Query, Temperature, Degree, Description)