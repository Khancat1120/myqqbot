import json
import random
import time
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot import on_command, on_keyword
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me
import requests
import base64
import os

basePath = os.path.abspath(__file__).replace('\\', '/').split("plugins/")[0] + "data/"
img = on_keyword({'色图', '涩图'}, rule=to_me(), priority=7)

user_agent_list = [
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/20100101 Firefox/17.0.6',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36']

url_list = [
    "https://api.lolicon.app/setu/v2?size=original&size=regular&r18=0",
    "https://api.lolicon.app/setu/v2?size=original&size=regular&r18=1"
]


def getUrl(type):
    UserAgent = random.choice(user_agent_list)
    headers = {'user-agent': UserAgent}
    r = requests.get(url_list[type], headers=headers, verify=False)
    c = r.json()
    c = c['data'][0]['urls']['original']
    return c.replace(".cat/", ".re/")
    # return c


miao = on_command("来个猫猫", rule=to_me(), priority=5)


@miao.handle()
async def _(bot:Bot, ev:Event):
    im = requests.get("http://edgecats.net/")
    await miao.finish(message=MessageSegment.image(im.content))



img = on_command("色图", rule=to_me(), priority=5)


@img.handle()
async def _(bot: Bot, event: Event):
    im = getUrl(0)
    rely = MessageSegment.image(im)
    await img.finish(message=rely)


wuneigui = on_command("不够色", rule=to_me(), priority=5)


@wuneigui.handle()
async def _(bot: Bot, event: Event):
    im = getUrl(1)
    rely = MessageSegment.image(im)
    await wuneigui.finish(message=rely)


ceshi = on_keyword({'测试'}, rule=to_me(), priority=5)


@ceshi.handle()
async def _(bot: Bot, event: Event):
    path = basePath + "test"
    # 返回path下所有文件构成的一个list列表
    fileList = os.listdir(path)
    # 遍历输出每一个文件的名字和类型
    url = random.choice(fileList)
    rely = MessageSegment.image("file:///" + path + "/" + url)
    await ceshi.finish(message=rely)


boom = on_command('色图六连', rule=to_me(), priority=5)

@boom.handle()
async def _(bot: Bot, event: Event):
    path = basePath + "setu"
    await boom.send("雷之呼吸 - 壹之型 - 色图一闪 - 六连")
    for i in range(6):
        fileList = os.listdir(path)
        # 遍历输出每一个文件的名字和类型
        # im = getUrl()
        url = random.choice(fileList)
        print(url)
        rely = MessageSegment.image("file:///" + path + "/" + url)
        await boom.send(message=rely)


balian = on_command('色图八连', rule=to_me(), priority=5)


@balian.handle()
async def _(bot: Bot, event: Event):
    path = basePath + "setu"
    await balian.send("集中一点，登峰造极！")
    await balian.send("全集中 - 雷之呼吸 - 壹之型 - 色图一闪 - 神速 - 八连")
    for i in range(8):
        fileList = os.listdir(path)
        # 遍历输出每一个文件的名字和类型
        # im = getUrl()
        url = random.choice(fileList)
        print(url)
        rely = MessageSegment.image("file:///" + path + "/" + url)
        await balian.send(message=rely)


shilian = on_command('色图十连', rule=to_me(), priority=5)


@shilian.handle()
async def _(bot: Bot, event: Event):
    path = basePath + "setu"
    await boom.send("纵使形神俱灭，定将色图从P站上搬运殆尽")
    shuihu = ["水之呼吸·壹之型 水面斩击", "水之呼吸·贰之型 水车", "水之呼吸·叁之型 流流舞动", "水之呼吸·肆之型 击打潮",
              "水之呼吸·伍之型 乾天的慈雨", "水之呼吸·陆之型 扭转漩涡", "水之呼吸·柒之型 雫波纹击刺", "水之呼吸·捌之型 泷壶",
              "水之呼吸·玖之型 水流飞沫", "水之呼吸·拾之型 生生流转", "水之呼吸·拾壹之型 凪"]
    for i in range(11):
        fileList = os.listdir(path)
        # 遍历输出每一个文件的名字和类型
        # im = getUrl()
        url = random.choice(fileList)
        print(shuihu[i] + "-" + url)
        rely = [
            MessageSegment.text(shuihu[i] + "\n"),
            MessageSegment.image("file:///" + path + "/" + url)
        ]
        await shilian.send(message=rely)


jiulian = on_command('色图九连', rule=to_me(), priority=5)


@jiulian.handle()
async def _(bot: Bot, event: Event):
    path = basePath + "setu"
    await boom.send("纵使形神俱灭，定将色图从P站上搬运殆尽")
    fenghu = ["风之呼吸·壹之型 尘旋风·削斩", "风之呼吸·贰之型 爪爪·科户风", "风之呼吸·叁之型 晴岚风树", "风之呼吸·肆之型 升上沙尘岚",
              "风之呼吸·伍之型 寒秋落山风", "风之呼吸·陆之型 黑风烟岚", "风之呼吸·柒之型 劲风·天狗风", "风之呼吸·捌之型 初烈风斩",
              "风之呼吸·玖之型 韦驮天台风"]
    for i in range(9):
        fileList = os.listdir(path)
        # 遍历输出每一个文件的名字和类型
        # im = getUrl()
        url = random.choice(fileList)
        print(fenghu[i] + "-" + url)
        rely = [
            MessageSegment.text(fenghu[i] + "\n"),
            MessageSegment.image("file:///" + path + "/" + url)
        ]
        await jiulian.send(message=rely)


qilian = on_command('色图七连', rule=to_me(), priority=5)


@qilian.handle()
async def _(bot: Bot, event: Event):
    path = basePath + "setu"
    await boom.send("纵使形神俱灭，定将色图从P站上搬运殆尽")
    xiahu = ["霞之呼吸·壹之型 垂天远霞", "霞之呼吸·贰之型 八重霞", "霞之呼吸·叁之型 霞散的飞沫", "霞之呼吸·肆之型 平流斩",
             "霞之呼吸·伍之型 霞云之海", "霞之呼吸·陆之型 月之霞消", "霞之呼吸·柒之型 胧"]
    for i in range(7):
        fileList = os.listdir(path)
        # 遍历输出每一个文件的名字和类型
        # im = getUrl()
        url = random.choice(fileList)
        print(xiahu[i] + "-" + url)
        rely = [
            MessageSegment.text(xiahu[i] + "\n"),
            MessageSegment.image("file:///" + path + "/" + url)
        ]
        await qilian.send(message=rely)


manga = on_command('漫画', rule=to_me(), priority=5)


@manga.handle()
async def _(bot: Bot, event: Event):
    UserAgent = random.choice(user_agent_list)
    headers = {'user-agent': UserAgent}
    r = requests.get("https://api.iyk0.com/bili_chart", headers=headers, verify=False)
    c = r.json()
    c = c['img']
    rely = MessageSegment.image(c)
    await manga.finish(message=rely)


saohua = on_command('骚话', rule=to_me(), priority=5)


@saohua.handle()
async def _(bot: Bot, event: Event):
    UserAgent = random.choice(user_agent_list)
    headers = {'user-agent': UserAgent}
    r = requests.get("https://api.iyk0.com/sao", headers=headers, verify=False)
    c = r.text
    await saohua.finish(c)


kuawo = on_command('夸我', rule=to_me(), priority=5)


@kuawo.handle()
async def _(bot: Bot, event: Event):
    url = "https://api.iyk0.com/chp/"
    UserAgent = random.choice(user_agent_list)
    headers = {'user-agent': UserAgent}
    r = requests.get(url, headers=headers, verify=False)
    c = r.json()
    sentence = c['txt']
    await kuawo.finish(sentence)


maijiaxiu = on_command('买家秀', rule=to_me(), priority=5)


@maijiaxiu.handle()
async def _(bot: Bot, event: Event):
    UserAgent = random.choice(user_agent_list)
    headers = {'user-agent': UserAgent}
    r = requests.get("https://api.iyk0.com/mjx/", headers=headers, verify=False, allow_redirects=False)
    res = dict(r.headers)['Location']
    print(res)
    rely = MessageSegment.image(res)
    await maijiaxiu.finish(message=rely)


cos = on_command('coser', rule=to_me(), priority=5)


@cos.handle()
async def _(bot: Bot, event: Event):
    UserAgent = random.choice(user_agent_list)
    headers = {'user-agent': UserAgent}
    r = requests.get("https://api.iyk0.com/cos/", headers=headers, verify=False, allow_redirects=False)
    res = dict(r.headers)
    rely = MessageSegment.image(res['Location'])
    await cos.finish(message=rely)


menhera = on_command('来张色色', rule=to_me(), priority=5)


@menhera.handle()
async def _(bot: Bot, event: Event):
    UserAgent = random.choice(user_agent_list)
    headers = {'user-agent': UserAgent}
    r = requests.get("https://iw233.cn/api.php?sort=random", headers=headers, verify=False, allow_redirects=False)
    print(r)
    res = dict(r.headers)['Location']
    rely = MessageSegment.image(res)
    await menhera.finish(message=rely)


# w = on_command('天气', rule=to_me(), priority=5)


# @w.handle()
# async def _(bot: Bot, event: Event):
#     msg = str(event.get_message()).split(' ')[-1]
#     UserAgent = random.choice(user_agent_list)
#     headers = {'user-agent': UserAgent}
#     r = requests.get("https://api.iyk0.com/tq/?city={}&type=".format(msg), headers=headers, verify=False,
#                      allow_redirects=False)
#     print("https://api.iyk0.com/tq/?city={}&type=".format(msg))
#     d = dict(r.json())
#     await w.finish(
#         "城市：" + d['city'] + "\n" +
#         "更新时间；" + d['update_time'] + "\n" +
#         "天气：" + d['wea'] + "\n" +
#         "当前气温：" + d['tem'] + "摄氏度" + "\n" +
#         "最低气温：" + d['tem_night'] + "摄氏度" + "\n" +
#         "最高气温：" + d['tem_day'] + "摄氏度" + "\n" +
#         "风向：" + d['win'] + "\n" +
#         "风级：" + d['win_speed'] + "\n" +
#         "风速：" + d['win_meter'] + "\n" +
#         "空气质量：" + d['air'] + "\n" +
#         "日期：" + d['time'] + "\n"
#     )
    


diange = on_command('点歌', rule=to_me(), priority=5)


@diange.handle()
async def _(bot: Bot, event: Event):
    msg = str(event.get_message()).split(' ')[1:]
    s = ""
    for i in msg:
      s += i
    msg = s
    UserAgent = random.choice(user_agent_list)
    headers = {'user-agent': UserAgent}
    r = requests.get("https://api.iyk0.com/wymusic/?msg={}&n=1".format(msg))
    d = dict(r.json())
    rely = [MessageSegment.text('歌名：' + d['song'] + '\n' + '歌手：' + d['singer'] + '\n' + d['url']), MessageSegment.image(d['img'])]
    await diange.send(message=rely)
    
    
    
weibo = on_command('吃瓜', rule=to_me(), priority=5)


@weibo.handle()
async def _(bot: Bot, event: Event):
    msg = str(event.get_message()).split(' ')[-1]
    UserAgent = random.choice(user_agent_list)
    headers = {'user-agent': UserAgent}
    r = requests.get("https://api.iyk0.com/wbr/")
    d = r.text
    s = ""
    mylist = d.split("}")
    for i in range(20):
        d = mylist[i] + "}"
        d = json.loads(d)
        temp = str(i + 1) + "：#" + d['title'] + "#" + '\n'
        s += temp
    s += "信息来源：https://s.weibo.com/top/summary/"
    await weibo.send(message=MessageSegment.text(s))



water = on_command('降水', aliases={'降雨'}, rule=to_me(), priority=5)

@water.handle()
async def _(bot: Bot, event: Event):
    UserAgent = random.choice(user_agent_list)
    headers = {'user-agent': UserAgent}
    r = requests.get("https://api.iyk0.com/jyu/", headers=headers, verify=False,
                     allow_redirects=False)
    d = dict(r.json())
    print(d)
    rely = MessageSegment.image(d['img'])
    await water.finish(message=rely)


jiojio = on_command('jk', aliases={'JK'}, rule=to_me(), priority=5)


@jiojio.handle()
async def _(bot: Bot, event: Event):
    UserAgent = random.choice(user_agent_list)
    headers = {'user-agent': UserAgent}
    r = requests.get("https://api.iyk0.com/mtt/", headers=headers, verify=False, allow_redirects=False)
    res = dict(r.headers)['Location']
    print(res)
    rely = MessageSegment.image(res)
    await jiojio.finish(message=rely)


manghe = on_command('盲盒', aliases={'开盲盒'}, rule=to_me(), priority=5)


@manghe.handle()
async def _(bot: Bot, event: Event):
    UserAgent = random.choice(user_agent_list)
    headers = {'user-agent': UserAgent}
    r = requests.get("https://api.iyk0.com/mtyh/", headers=headers, verify=False, allow_redirects=False)
    res = dict(r.headers)['Location']
    print(res)
    rely = MessageSegment.image(res)
    await manghe.finish(message=rely)


baidu = on_command('百度', aliases={'度娘', '百度百科'}, rule=to_me(), priority=5)


@baidu.handle()
async def _(bot: Bot, event: Event):
    msg = str(event.get_message()).split(' ')[-1]
    url = 'http://tool.mkblog.cn/lmbtfy/?q=' + str(base64.b64encode(msg.encode('utf-8')))[2:-1]
    rely = MessageSegment.share(url, "你刚才问的问题的答案")
    await baidu.finish(rely)


covid = on_command('疫情', rule=to_me(), priority=5)


@covid.handle()
async def _(bot: Bot, event: Event):
    msg = str(event.get_message()).split(' ')[-1]
    UserAgent = random.choice(user_agent_list)
    headers = {'user-agent': UserAgent}
    r = requests.get("https://api.iyk0.com/yq/?msg={}&type=".format(msg), headers=headers, verify=False,
                     allow_redirects=False)
    print("https://api.iyk0.com/yq/?msg={}&type=".format(msg))
    d = dict(r.json())
    print(d)
    await covid.finish(
        "查询地区：" + d['查询地区'] + "\n" +
        "累计确诊；" + d['目前确诊'] + "\n" +
        "死亡人数：" + d['死亡人数'] + "\n" +
        "治愈人数：" + d['治愈人数'] + "\n" +
        "新增确诊：" + d['新增确诊'] + "\n" +
        "现存确诊：" + d['现存确诊'] + "\n" +
        "现存无症状：" + d['现存无症状'] + "\n" +
        "上次统计时间：" + d['time'] + "\n"
    )


xiezhen = on_keyword({'福利姬', "写真"}, rule=to_me(), priority=5)


@xiezhen.handle()
async def _(bot: Bot, event: Event):
    path = basePath + "xiezhen"
    # 返回path下所有文件构成的一个list列表
    fileList = os.listdir(path)
    # 遍历输出每一个文件的名字和类型
    url = random.choice(fileList)
    print(url)
    rely = MessageSegment.image("file:///" + path + "/" + url)
    rely = "精虫上脑的给爷爬"
    await xiezhen.finish(message=rely)


nonereply = on_command("", rule=to_me(), priority=20)


@nonereply.handle()
async def _(bot: Bot, event: Event):
    msg = str(event.get_message())
    if "你是" in msg and ("嘛" in msg or "吗" in msg):
        await nonereply.finish("我不是，我没有，别瞎说")
    UserAgent = random.choice(user_agent_list)
    headers = {'user-agent': UserAgent}
    r = requests.get("http://api.qingyunke.com/api.php?key=free&appid=0&msg={}".format(msg), headers=headers,
                     verify=False,
                     allow_redirects=False)
    d = dict(r.json())
    await nonereply.finish(
        d['content'].replace("菲菲", "小七").replace("晨晨", "雅琪").replace("妈咪你", "雅琪").replace("无名", "高雅君"))


news = on_command('新闻', rule=to_me(), priority=5)


@news.handle()
async def _(bot: Bot, event: Event):
    UserAgent = random.choice(user_agent_list)
    headers = {'user-agent': UserAgent}
    r = requests.get("https://api.iyk0.com/60s", headers=headers, verify=False)
    c = dict(r.json())
    print(c)
    c = c['imageUrl']
    rely = MessageSegment.image(c)
    await news.finish(message=rely)
    



setuzhongji = on_command('色图神乐', rule=to_me(), priority=5)


@setuzhongji.handle()
async def _(bot: Bot, event: Event):
    path = basePath + "setu"
    rihu = ["火之神神乐 圆舞", "火之神神乐 碧罗天", "火之神神乐 烈日红镜", "火之神神乐 幻日虹",
            "火之神神乐 火车", "火之神神乐 灼骨炎阳", "火之神神乐 阳华突", "火之神神乐 飞轮阳炎",
            "火之神神乐 斜阳转身", "火之神神乐 辉辉恩光", "火之神神乐 日晕之龙·头舞", "火之神神乐 炎舞"]
    await setuzhongji.send("我等色图Bot永垂不朽……")
    await setuzhongji.send("直至满足此世上所有人的XP")
    for i in range(24):
        fileList = os.listdir(path)
        # 遍历输出每一个文件的名字和类型
        # im = getUrl()
        url = random.choice(fileList)
        print(rihu[i % 12] + "-" + url)
        rely = [
            MessageSegment.text(rihu[i % 12] + "\n"),
            MessageSegment.image("file:///" + path + "/" + url)
        ]
        await setuzhongji.send(message=rely)
