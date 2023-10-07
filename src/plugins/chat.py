# -*- coding: utf-8 -*-
import nonebot
from nonebot import on_keyword, get_driver, on_command
import random
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me, keyword
from .timer import qinghualist
import os
from nonebot.adapters.onebot.v11 import MessageSegment

basePath = os.path.abspath(__file__).replace('\\', '/').split("plugins/")[0] + "data/"


hug = on_keyword({"抱抱", "想抱"", 抱"}, rule=to_me(), priority=6)


@hug.handle()
async def _(bot: Bot, event: Event):
    await hug.finish(random.choice(["抱抱，最喜欢你了", "笨蛋", "抱", "抱抱，小猪", "啵啵", "给你个大熊抱", "给你个公主抱"]))


kiss = on_keyword({"亲", "啵啵", "想亲"}, rule=to_me(), priority=6)


@kiss.handle()
async def _(bot: Bot, event: Event):
    await kiss.finish(random.choice(["啵啵，小笨猪", "啵啵，最喜欢你了", "啵啵，小笨蛋", "啵", "啵啵，臭猪", "啵啵", "亲亲", "亲亲我的小笨蛋"]))


papa = on_keyword(
    {"不戴套", "不带套", "内射", "想和你啪", "想和你doi", "doi", "想上", "想霍", "想嚯", "想啪", "想和你做", "啪啪啪", "想操", "操我", "上我"},
    rule=to_me(),
    priority=5)


@papa.handle()
async def _(bot: Bot, event: Event):
    await papa.finish(random.choice(["我好想把你按在床上狠狠艹一顿", "我也好想上你", "可以不戴套吗？", "你想被艹哭吗？", "1小时20块，包夜50，打钱吧", "哼，小色狼"]))


miss = on_keyword({"想你"}, rule=to_me(), priority=6)


@miss.handle()
async def _(bot: Bot, event: Event):
    await miss.finish(random.choice(["啵啵，小猪", "我也好想你", "小猪，我也想你", "哼，我也想你啊", "笨蛋"]))


baby = on_keyword({"宝", "崽", "小猪", "亲爱的", "老公", "臭猪"}, rule=to_me(), priority=7)


@baby.handle()
async def _(bot: Bot, event: Event):
    await baby.finish(random.choice(["啵啵", "嘎哈", "臭猪", "小猪", "笨蛋", "老婆"]))


doWhat = on_keyword({"干嘛呢", "嘎哈呢", "干啥呢", "干什么", "做什么", "忙什么", "搞什么"}, rule=to_me(), priority=6)


@doWhat.handle()
async def _(bot: Bot, event: Event):
    await doWhat.finish(random.choice(["小猪，我在写大作业呢", "我在写论文", "我在收拾东西", "我在吃饭", "我正准备去洗澡呢"]))


look = on_keyword({"给我看看你", "照片"}, rule=to_me(), priority=6)


@look.handle()
async def _(bot: Bot, event: Event):
    await look.finish(random.choice(["哼，我有什么好处？", "不给看", "我有什么好处？"]))


haochu = on_keyword({"要好处", "怎么就想要好处", "怎么就知道要好处"}, rule=to_me(), priority=6)


@haochu.handle()
async def _(bot: Bot, event: Event):
    await haochu.finish(random.choice(["一分付出，一份回报，臭猪"]))


zaima = on_keyword({"在不", "在吗", "?", "？"}, rule=to_me(), priority=6)


@zaima.handle()
async def _(bot: Bot, event: Event):
    await zaima.finish(random.choice(["臭猪", "嘎哈？"]))


love = on_keyword({"爱你"}, rule=to_me(), priority=6)


@love.handle()
async def _(bot: Bot, event: Event):
    await love.finish(random.choice(["我也最爱你", "小猪，我也爱你", "我也爱你，笨蛋", "小笨蛋，我世界第一爱你"]))


like = on_keyword({"喜欢你"}, rule=to_me(), priority=6)


@like.handle()
async def _(bot: Bot, event: Event):
    await like.finish(random.choice(["我也最喜欢你", "小猪，我也喜欢你", "我也喜欢你，笨蛋"]))


zao = on_keyword({"早"}, rule=to_me(), priority=6)


@zao.handle()
async def _(bot: Bot, event: Event):
    await zao.finish(random.choice(["早安", "小猪，早", "早，好困啊"]))


noon = on_keyword({"午睡，午觉"}, rule=to_me(), priority=6)


@noon.handle()
async def _(bot: Bot, event: Event):
    await noon.finish(random.choice(["好困，想睡一小会儿", "困困，刚刚吃的太饱了", "好困啊"]))


night = on_keyword({"晚安"}, rule=to_me(), priority=6)


@night.handle()
async def _(bot: Bot, event: Event):
    await night.finish(random.choice(["晚安，好梦，爱你", "啵啵，晚安，要梦到我哦", "爱你，晚安，zzz"]))


hungry = on_keyword({"饿"}, rule=to_me(), priority=6)


@hungry.handle()
async def _(bot: Bot, event: Event):
    await hungry.finish(random.choice(["我也好饿", "小猪，想吃什么", "小猪，想吃米线还是麻辣拌，我给你点外卖"]))


fight = on_keyword({"雷之呼吸"}, rule=to_me(), priority=6)


@fight.handle()
async def _(bot: Bot, event: Event):
    await fight.finish(random.choice(["雷之呼吸·壹之型 霹雳一闪", "雷之呼吸·柒之型 火雷神"]))


water = on_keyword({"水之呼吸"}, rule=to_me(), priority=6)


@water.handle()
async def _(bot: Bot, event: Event):
    await water.finish(random.choice(["水之呼吸·壹之型 水面斩击", "水之呼吸·贰之型 水车", "水之呼吸·叁之型 流流舞动", "水之呼吸·肆之型 击打潮",
                                      "水之呼吸·伍之型 乾天的慈雨", "水之呼吸·陆之型 扭转漩涡", "水之呼吸·柒之型 雫波纹击刺", "水之呼吸·捌之型 泷壶",
                                      "水之呼吸·玖之型 水流飞沫", "水之呼吸·拾之型 生生流转"]))


xiahu = on_keyword({"霞之呼吸"}, rule=to_me(), priority=6)


@xiahu.handle()
async def _(bot: Bot, event: Event):
    await xiahu.finish(random.choice(["霞之呼吸·壹之型 垂天远霞", "霞之呼吸·贰之型 八重霞", "霞之呼吸·叁之型 霞散的飞沫", "霞之呼吸·肆之型 平流斩",
                                      "霞之呼吸·伍之型 霞云之海", "霞之呼吸·陆之型 月之霞消", "霞之呼吸·柒之型 胧"]))


bisha = on_keyword({"大招", "开大", "必杀"}, rule=to_me(), priority=6)


@bisha.handle()
async def _(bot: Bot, event: Event):
    await bisha.finish(random.choice(["全集中·水之呼吸·拾壹之型 凪", "炎之呼吸·奥义·第玖之型 炼狱"]))


rihu = on_keyword({"日之呼吸", "火之神神乐"}, rule=to_me(), priority=6)


@rihu.handle()
async def _(bot: Bot, event: Event):
    await rihu.finish(random.choice(["火之神神乐·壹之型 圆舞", "火之神神乐·贰之型 碧罗天", "火之神神乐·叁之型 烈日红镜", "火之神神乐·肆之型 幻日虹",
                                     "火之神神乐·伍之型 火车", "火之神神乐·陆之型 灼骨炎阳", "火之神神乐·柒之型 阳华突", "火之神神乐·捌之型 飞轮阳炎",
                                     "火之神神乐·玖之型 斜阳转身", "火之神神乐 拾之型 辉辉恩光", "火之神神乐·拾壹之型 日晕之龙·头舞", "火之神神乐·拾贰之型 炎舞"]))


yanhu = on_keyword({"炎之呼吸"}, rule=to_me(), priority=6)


@yanhu.handle()
async def _(bot: Bot, event: Event):
    print(nonebot.get_bots())
    await yanhu.finish(random.choice(["炎之呼吸·壹之型 不知火", "炎之呼吸·贰之型 上升炎天", "炎之呼吸·叁之型 气炎万象", "炎之呼吸·肆之型 盛炎的蜿蜒",
                                      "炎之呼吸·伍之型 炎虎", "炎之呼吸·奥义·玖之型 炼狱"]))


fenghu = on_keyword({"风之呼吸"}, rule=to_me(), priority=6)


@fenghu.handle()
async def _(bot: Bot, event: Event):
    print(nonebot.get_bots())
    await fenghu.finish(random.choice(["风之呼吸·壹之型 尘旋风·削斩", "风之呼吸·贰之型 爪爪·科户风", "风之呼吸·叁之型 晴岚风树", "风之呼吸·肆之型 升上沙尘岚",
                                       "风之呼吸·伍之型 寒秋落山风", "风之呼吸·陆之型 黑风烟岚", "风之呼吸·柒之型 劲风·天狗风", "风之呼吸·捌之型 初烈风斩",
                                       "风之呼吸·玖之型 韦驮天台风"]))


guangjie = on_keyword({"陪我", "一起玩游戏吗？"}, rule=to_me(), priority=6)


@guangjie.handle()
async def _(bot: Bot, event: Event):
    await guangjie.finish(random.choice(["好的，什么时候？", "什么时候开始呀？", "现在吗？还是什么时候？"]))


hh = on_keyword({"嘿", "哈", "嘻"}, rule=to_me(), priority=6)


@hh.handle()
async def _(bot: Bot, event: Event):
    await hh.finish(random.choice(["笨蛋，傻笑什么？", "小猪，什么事这么开心？", "笨猪"]))


nihao = on_keyword({"你真好", "你最好", "你真棒", "你怎么这么可爱", "你真可爱", "这么可爱", "你好可爱"}, rule=to_me(), priority=6)


@nihao.handle()
async def _(bot: Bot, event: Event):
    await nihao.finish(random.choice(["那当然，我可是要成为水柱的男人", "笨蛋，我不好谁好？", "你是小笨猪吗？"]))


aiwo = on_keyword({"你爱我吗", "你喜欢我吗", "永远爱", "一直爱", "一辈子爱"}, rule=to_me(), priority=6)


@aiwo.handle()
async def _(bot: Bot, event: Event):
    await aiwo.finish(random.choice(["那当然", "笨蛋，我永远世界第一爱你", "你是小笨猪吗？总问这些傻傻的问题", "当然啦，没有安全感的小笨蛋"]))


today = on_keyword({"今天你有多爱我", "今天你有多喜欢我", "你有多喜欢我", "你多喜欢我", "你有多爱我", "你有多爱我"}, rule=to_me(), priority=6)


@today.handle()
async def _(bot: Bot, event: Event):
    await today.finish(random.choice(["比昨天多一点，比明天少一点"]))


notice = on_keyword({"你注意到", "你看到"}, rule=to_me(), priority=6)


@notice.handle()
async def _(bot: Bot, event: Event):
    await notice.finish(random.choice(["怎么了？"]))


beautiful = on_keyword({"很美"}, rule=to_me(), priority=6)


@beautiful.handle()
async def _(bot: Bot, event: Event):
    await beautiful.finish(random.choice(["不如你美"]))


lucky = on_keyword({"有你在三生有幸", "有你在真幸运"}, rule=to_me(), priority=6)


@lucky.handle()
async def _(bot: Bot, event: Event):
    await lucky.finish(random.choice(["不，我才幸运"]))


missme = on_keyword({"你在想我吗", "你想我了吗", "想我"}, rule=to_me(), priority=6)


@missme.handle()
async def _(bot: Bot, event: Event):
    await missme.finish(random.choice(["当然，每时每刻都在想你", "当然，我一直都在想你哦", "想你，小猪"]))


keyima = on_keyword({"行吗", "可以吗", "可以嘛", "行不", "行嘛"}, rule=to_me(), priority=6)


@keyima.handle()
async def _(bot: Bot, event: Event):
    await keyima.finish(random.choice(["小猪，等下我看看能不能腾出时间", "我问问组里那时候有没有事儿", "等我先看看哦，小笨蛋"]))


bukeyi = on_keyword({"不行"}, rule=to_me(), priority=6)


@bukeyi.handle()
async def _(bot: Bot, event: Event):
    await bukeyi.finish(random.choice(["臭猪，小气", "哼", "哼，小气鬼"]))


qinghua = on_keyword({"情话"}, rule=to_me(), priority=6)


@qinghua.handle()
async def _(bot: Bot, event: Event):
    path = basePath + "myImage"
    # 返回path下所有文件构成的一个list列表
    fileList = os.listdir(path)
    # 遍历输出每一个文件的名字和类型
    rely = MessageSegment.image("file:///" + path + "/" + random.choice(fileList))
    await qinghua.send(rely)
    await qinghua.finish(random.choice(qinghualist))


meiyou = on_keyword({"我没感觉到", "冷漠", "不爱我", "不喜欢我"}, rule=to_me(), priority=6)


@meiyou.handle()
async def _(bot: Bot, event: Event):
    await meiyou.finish(random.choice(["啊呸！我最喜欢你了", "哼，才没有呢", "我呸，我最喜欢你了"]))


buli = on_keyword({"不理我", "不说话"}, rule=to_me(), priority=6)


@buli.handle()
async def _(bot: Bot, event: Event):
    await buli.finish(random.choice(["小猪，我在想你呢", "小猪，我忙着呢"]))


aiwo = on_keyword({"没有见面", "好久没见你了"}, rule=to_me(), priority=6)


@aiwo.handle()
async def _(bot: Bot, event: Event):
    await aiwo.finish(random.choice(["两情若是久长时，又岂在朝朝暮暮", "但愿人长久，千里共婵娟", "有情不管别离久，情在相逢终有", "好把音书凭过雁，东莱不似蓬莱远"]))


gaoyaqi = on_keyword(
    {"可涵的老婆", "你老婆是谁", "你对象是谁", "你女朋友是谁", "你的老婆是谁", "你的对象是谁", "你的女朋友是谁", "你的宝宝是谁", "你的宝贝儿是谁", "你的宝贝是谁"},
    rule=to_me(), priority=6)


@gaoyaqi.handle()
async def _(bot: Bot, event: Event):
    await gaoyaqi.finish("高雅琪")


gaoyajun = on_keyword({"你的小姨子是谁", "你小姨子是谁"}, rule=to_me(), priority=6)


@gaoyajun.handle()
async def _(bot: Bot, event: Event):
    await gaoyajun.finish("高雅君")


gaoyajunwho = on_keyword({"高雅君是谁"}, rule=to_me(), priority=6)


@gaoyajunwho.handle()
async def _(bot: Bot, event: Event):
    await gaoyajunwho.finish(random.choice(["是机灵鬼", "是聪明人", "是大佬"]))


gaoyaqiwho = on_keyword({"雅琪是谁"}, priority=6)


@gaoyaqiwho.handle()
async def _(bot: Bot, event: Event):
    await gaoyaqiwho.finish(random.choice(["是臭猪", "是小笨蛋", "是小垃圾"]))


hushuo = on_keyword({"胡说"}, priority=6)


@hushuo.handle()
async def _(bot: Bot, event: Event):
    await hushuo.finish(random.choice(["我从不胡说！", "我呸，我才没有"]))

# yiwozuo = on_keyword({"通透秒上三"}, priority=5)
#
#
# @yiwozuo.handle()
# async def _(bot: Bot, event: Event):
#     await yiwozuo.finish(random.choice(["又开始虚空加通透秒上三了？你敢不敢给猗窝座也加个通透和呼吸？"]))
#
#
# tongmo = on_keyword({"丑死的"}, priority=5)
#
#
# @tongmo.handle()
# async def _(bot: Bot, event: Event):
#     await tongmo.finish(random.choice(["经典言论：黑死牟被自己丑死"]))
