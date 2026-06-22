import requests

query = input("Enter a topic to search for news: ")
api = "b489a0c15c0d4630904a0db31bf3edce"

url = f"https://newsapi.org/v2/everything?q={query}&from=2026-05-19&sortBy=publishedAt&apiKey={api}"
print(url)

response = requests.get(url)
data = response.json()
articles = data['articles']

for i, article in enumerate(articles):
    print(f"Article {i+1}:")
    print(f"Title: {article['title']}")
    print(f"Description: {article['description']}")
    print(f"URL: {article['url']}")
    print(f"Published At: {article['publishedAt']}")
    print("-" * 80)
    


    #request  should be installed , if it is not installed then run the command "pip install requests" in the terminal
    #go to newsapi.org and create an account to get your own api key and replace the api variable with your own api key
    #modfy the url , url is extracted from the news api
    #when you run code till print(url) it will print the url in the terminal and you can copy paste it in the browser to see the response from the news api
    #but the response will be in json format and it will be difficult to read 
    #then add json formatter 
    #use for loop to print the title , description , url and published at of the articles in a readable format
    