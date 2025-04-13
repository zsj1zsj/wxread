# config.py 自定义配置,包括阅读次数、推送token的填写
import os
import re

"""
可修改区域
默认使用本地值如果不存在从环境变量中获取值
"""

# 阅读次数 默认40次/20分钟
READ_NUM = int(os.getenv('READ_NUM') or 40)
# 需要推送时可选，可选pushplus、wxpusher、telegram
PUSH_METHOD = "" or os.getenv('PUSH_METHOD')
# pushplus推送时需填
PUSHPLUS_TOKEN = "" or os.getenv("PUSHPLUS_TOKEN")
# telegram推送时需填
TELEGRAM_BOT_TOKEN = "" or os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = "" or os.getenv("TELEGRAM_CHAT_ID")
# wxpusher推送时需填
WXPUSHER_SPT = "" or os.getenv("WXPUSHER_SPT")
# read接口的bash命令，本地部署时可对应替换headers、cookies
curl_str = os.getenv('WXREAD_CURL_BASH')

# headers、cookies是一个省略模版，本地或者docker部署时对应替换
cookies = {
    'ptcz': '57e7c8f8f07f13b06fadc94f5e63f7a92514e2c843c53b0d74dda81151386786',
    'uin': 'o44611321',
    '_qimei_h38': '06048ac6bdc110eb625d25f10300000cd1811d',
    'pac_uid': '0_CmXWxBF52P5xw',
    'suid': 'user_0_CmXWxBF52P5xw',
    '_qimei_fingerprint': '98e2866c8389ef7e8e6dd4ddf011d2ae',
    'RK': 'RJHwWF+feX',
    'wr_gid': '278483624',
    'wr_fp': '2637993037',
    'wr_vid': '327488677',
    'wr_pf': '0',
    'wr_rt': 'web%40ROH4NSFPNrNXe2gAo_N_AL',
    'wr_localvid': '68c321108138514a568cb53',
    'wr_name': 'Lynn',
    'wr_gender': '1',
    '_qimei_uuid42': '1940b01292e100002d2ca1980fdbf4f063c8b13850',
    'wr_avatar': 'https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FDYAIOgq83erM7bxmkPTPIxIcNZzvYqZrLf3y3PYcBAIHuzIEichTYdZG6jBHSOia4tqkibvVgTaPCsYgz2NIicI7AA%2F132',
    'wr_skey': '08Uv45bs',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en,zh;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,ja;q=0.6',
    'baggage': 'sentry-environment=production,sentry-release=dev-1744355656859,sentry-public_key=ed67ed71f7804a038e898ba54bd66e44,sentry-trace_id=b1cc66429e2d44e58ed1cd6461dd66fe',
    'content-type': 'application/json;charset=UTF-8',
    'dnt': '1',
    'origin': 'https://weread.qq.com',
    'priority': 'u=1, i',
    'referer': 'https://weread.qq.com/web/reader/f1e328e072710bfaf1e87e9k033320e02c30336dcbab9a8',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': 'b1cc66429e2d44e58ed1cd6461dd66fe-88e81f284baf197c',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    # 'cookie': 'ptcz=57e7c8f8f07f13b06fadc94f5e63f7a92514e2c843c53b0d74dda81151386786; uin=o44611321; _qimei_h38=06048ac6bdc110eb625d25f10300000cd1811d; pac_uid=0_CmXWxBF52P5xw; suid=user_0_CmXWxBF52P5xw; _qimei_fingerprint=98e2866c8389ef7e8e6dd4ddf011d2ae; RK=RJHwWF+feX; wr_gid=278483624; wr_fp=2637993037; wr_vid=327488677; wr_pf=0; wr_rt=web%40ROH4NSFPNrNXe2gAo_N_AL; wr_localvid=68c321108138514a568cb53; wr_name=Lynn; wr_gender=1; _qimei_uuid42=1940b01292e100002d2ca1980fdbf4f063c8b13850; wr_avatar=https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FDYAIOgq83erM7bxmkPTPIxIcNZzvYqZrLf3y3PYcBAIHuzIEichTYdZG6jBHSOia4tqkibvVgTaPCsYgz2NIicI7AA%2F132; wr_skey=08Uv45bs',
}


# 书籍
book = [
    "36d322f07186022636daa5e","6f932ec05dd9eb6f96f14b9","43f3229071984b9343f04a4","d7732ea0813ab7d58g0184b8",
    "3d03298058a9443d052d409","4fc328a0729350754fc56d4","a743220058a92aa746632c0","140329d0716ce81f140468e",
    "1d9321c0718ff5e11d9afe8","ff132750727dc0f6ff1f7b5","e8532a40719c4eb7e851cbe","9b13257072562b5c9b1c8d6"
]

# 章节
chapter = [
    "ecc32f3013eccbc87e4b62e","a87322c014a87ff679a21ea","e4d32d5015e4da3b7fbb1fa","16732dc0161679091c5aeb1",
    "8f132430178f14e45fce0f7","c9f326d018c9f0f895fb5e4","45c322601945c48cce2e120","d3d322001ad3d9446802347",
    "65132ca01b6512bd43d90e3","c20321001cc20ad4d76f5ae","c51323901dc51ce410c121b","aab325601eaab3238922e53",
    "9bf32f301f9bf31c7ff0a60","c7432af0210c74d97b01b1c","70e32fb021170efdf2eca12","6f4322302126f4922f45dec"
]

"""
建议保留区域|默认读三体，其它书籍自行测试时间是否增加
"""
data = {
    'appId': 'wb115321887466h1205141645',
    'b': 'f1e328e072710bfaf1e87e9',
    'c': '033320e02c30336dcbab9a8',
    'ci': 6,
    'co': 385,
    'sm': '竿头添彩，后出转精——图文版《明朝那些事',
    'pr': 0,
    'rt': 15,
    'ts': 1744536065606,
    'rn': 202,
    'sg': '49e84affe82a70ee108768f98f3d091b00559a16ae919e333806a6439462f181',
    'ct': 1744536065,
    'ps': '46032d707a65f364g017062',
    'pc': 'fcc32a507a65f364g019c0b',
    's': '46159d82',
}


def convert(curl_command):
    """提取bash接口中的headers与cookies
    支持 -H 'Cookie: xxx' 和 -b 'xxx' 两种方式的cookie提取
    """
    # 提取 headers
    headers_temp = {}
    for match in re.findall(r"-H '([^:]+): ([^']+)'", curl_command):
        headers_temp[match[0]] = match[1]

    # 提取 cookies
    cookies = {}
    
    # 从 -H 'Cookie: xxx' 提取
    cookie_header = next((v for k, v in headers_temp.items() 
                         if k.lower() == 'cookie'), '')
    
    # 从 -b 'xxx' 提取
    cookie_b = re.search(r"-b '([^']+)'", curl_command)
    cookie_string = cookie_b.group(1) if cookie_b else cookie_header
    
    # 解析 cookie 字符串
    if cookie_string:
        for cookie in cookie_string.split('; '):
            if '=' in cookie:
                key, value = cookie.split('=', 1)
                cookies[key.strip()] = value.strip()
    
    # 移除 headers 中的 Cookie/cookie
    headers = {k: v for k, v in headers_temp.items() 
              if k.lower() != 'cookie'}

    return headers, cookies


headers, cookies = convert(curl_str) if curl_str else (headers, cookies)
