# WebPy is a text based browser

import requests
import html2text


def getRequest(url):

        reqGet = requests.get(url)
        content = reqGet.content
        content = content.decode("utf-8", 'ignore')

        if len(content) == 0:
            if reqGet.status_code == 200:
                print(html2text.html2text(content))
            elif reqGet.status_code == 404:
                print("Error 404: Not Found")
            elif reqGet.status_code == 500:
                print("Error 500: Internal Server Error")
            else:
                print(html2text.html2text(content))

        # For non-empty case, print message
        else:
            print(html2text.html2text(content))

def main():
    print("Type 'quit' to close")
    print("WebPy is a text based web reader")

    while True:
        data = input("Website Address/URL:(e.g. http://www.google.com)\n>>>")
        print("Type 'quit' to close")

        if data == "quit":
            break
        else:
            pass

        getRequest(data)

main()
