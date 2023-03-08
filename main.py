import requests

api_key = "3a87d35100f44f459716ca23be0ddab7"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-02-08&" \
      "sortBy=publishedAt&apiKey=3a87d35100f44f459716ca23be0ddab7"

# 请求
request = requests.get(url)
# 获取dictionary data, request.text是string，requeston.json才是dictionary
content = request.json()

# 拿到文章title和description
for article in content['articles']:
    print(article['title'])
    print(article['description'])
