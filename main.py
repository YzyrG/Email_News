"""
Request news by  use api
"""
# coding=utf-8

import requests
import send_emails
import os

api_key = os.getenv("NEWS_API")
category = "guoji"
url = "http://v.juhe.cn/toutiao/index?" \
      f"type={category}&" \
      "page=1&" \
      "page_size=20&" \
      "is_filter=1&" \
      "key=f780d600201b82df140b910357a7db9c"


# 请求
request = requests.get(url)
# 获取dictionary data, request.text是string，requeston.json才是dictionary
content = request.json()
# print(content)

# 生成news
news = ""
for article in content['result']['data']:
    if article["title"] is not None:
        title = article['title']
        author = article['author_name']
        url = article['url']
        news += f"Title: {title}\n Author: {author}\n {url}\n\n"

# 构造邮件
message = str(send_emails.create_email("头条", news))
# 发送邮件
send_emails.send_email(message)
