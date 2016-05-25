from urllib import request

url = 'http://real-chart.finance.yahoo.com/table.csv?s=%5EBSESN&d=3&e=24&f=2016&g=d&a=6&b=1&c=1997&ignore=.csv'


def download_file(downloadable_url):
    response = request.urlopen(downloadable_url)
    csv = response.read()
    string = str(csv)
    lines = string.split("\\n")
    destination = r'stock.csv'
    file = open(destination, 'w')
    for line in lines:
        file.write(line + "\n")

    file.close()
    readfile = open('stock.csv', 'r')
    text = readfile.read()
    print(text)


download_file(url)
