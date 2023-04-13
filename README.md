# python-tiktok
python脚本监听抖音用户作品以及粉丝变动然后推送
### 使用教程

1. 安装依赖

```
pip install requests time random bs4

```

2. 先去抖音官网https://www.douyin.com =>查找你要监控的用户节界面 =>然后看到用户名再次点进去 
3. 复制user/后面的编码地址然后拼接?showTab=post

```
https://www.douyin.com/user/复制链接到此出'+'?showTab=post
```
示例
```
https://www.douyin.com/user/MS4wLjABAAAAqdZaxHszgw-AwIKTj5lbYi4ehlYD4GDWcnX41t1GzCw?showTab=post
```

4. 替换2处为你的信息，headers信息F12自己获取

```python
url = '上面的user用户拼接链接'
```

```
headers = {
        'User-Agent': '你的User-Agent',
        'cookie': '你的cookie'
    }
```

5. 替换为你的key，推送平台：https://www.pushdeer.com 下载app即可获取提送key

```
push_key = "your key"
```

6.需要自定义随机睡眠时间，请修改此处（默认岁进30分钟-1小时）

```
 sleep_time = random.randint(1800,3600)
```

7. run

