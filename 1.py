import requests
import time
import random
from bs4 import BeautifulSoup

# 定义爬虫函数
def spider():
    # URL为抖音用户主页URL链接
    url = 'your url'
    headers = {
        'User-Agent': 'your User-Agent',
        'cookie': 'your cookie'
    }
    response = requests.get(url, headers=headers)
    bs4 = BeautifulSoup(response.text, 'html.parser')
    # 在页面中找到粉丝元素并获取粉丝数量
    fans_element = bs4.find_all('div', {'class': 'AULCPX_8 LEaniV4W', 'data-e2e': 'user-info-fans'})
    if not fans_element:
        return ''
    fans = int(fans_element[0].find_all('div', {'class': 'TxoC9G6_'})[0].text)
    works_element = bs4.find_all('div', {'class': 'qYqKgR2A GTnzp897', 'data-e2e': 'user-work-tab'})
    works = works_element[0].find_all('span', {'class': 'J6IbfgzH'})[0].text
    user_element = bs4.find_all('h1', {'class': 'xpjM3LEg'})
    user_name = user_element[0].find_all('span')[5].text

    dt = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print("{} {} 作品数:{} 粉丝数:{}".format(dt, user_name, works, fans))

    push_url = "https://api2.pushdeer.com/message/push"
    push_key = "your key"
    if hasattr(spider, 'fans') and hasattr(spider, 'works'):
        if fans != spider.fans:
            # 发送粉丝变化通知
            message = "{} {} 粉丝量有变化".format(dt, user_name)
            params = {"pushkey": push_key, "text": message}
            requests.get(push_url, params=params)
        if works != spider.works:
            # 发送作品更新通知
            message = "{} {} 更新或删除了一个作品".format(dt, user_name)
            params = {"pushkey": push_key, "text": message}
            requests.get(push_url, params=params)

    spider.fans = fans
    spider.works = works

def main():
    while True:
        spider()
        sleep_time = random.randint(1800,3600)
        time.sleep(sleep_time)


# 测试一次爬虫，检查是否正常运行
print('start')
main()
