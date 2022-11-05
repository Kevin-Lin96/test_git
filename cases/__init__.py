import requests


def test_get_areatypes(self):
    # 发送get请求
    url = "http://www.67934.cn:30702/superlink/api/areatypes?includeContainedAreaTypes=false&page=1&pageSize=100"
    data = {
        "includeContainedAreaTypes":"true",
        "page":"1",
        "pageSize":"100"
    }
    rep= requests.get(url=url)
    print(rep.json())