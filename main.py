"""
Request news by  use api
"""
# coding=utf-8

import requests
import send_emails

api_key = "3a87d35100f44f459716ca23be0ddab7"
topic = "war"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-02-08&" \
      "sortBy=publishedAt&" \
      "apiKey=3a87d35100f44f459716ca23be0ddab7"

# 请求
request = requests.get(url)
# 获取dictionary data, request.text是string，requeston.json才是dictionary
content = request.json()
# print(content)

# 生成news
news = ""
for article in content['articles'][:20]:
    if article["title"] is not None:
        title = article['title']
        description = article['description']
        url = article['url']
        news += f"Title: {title}\n Description: {description}\n {url}\n\n"

# 构造邮件
message = str(send_emails.create_email("Yahoo!", news))
# 发送邮件
send_emails.send_email(message)
