import time
from hashlib import md5
from nonebot.plugin import on_keyword
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11 import MessageSegment
import re

a = '向晚, 晚晚, 幽默钻头, 兄弟, 我兄弟, 晚比, 晚'
b = '贝拉, 拉姐, 拉'
c = '珈乐, 小狼王, 乐'
d = '嘉然, 然然, 粉色小矮子, 粉色小恶魔, 小羽毛球, 粉色小猪猪, 然比, 然'
e = '乃琳, n0, 白色香顶边, 坏女人, 琳'
ab = '师徒组, 师徒, 憨次方'
ac = '萤火虫'
ad = '嘉晚饭'
ae = '果丹皮'
bc = '贝贝珈'
bd = '超级嘉贝'
be = '乃贝, 奶贝'
cd = 'c++, c嘉珈, c珈嘉'
ce = '珈特琳'
de = '母女组'
cao = '阿草, 羊驼, 臭羊驼'
shark = '七海, 海子姐, nanami'

names = [a, b, c, d, e, ab, ac, ad, ae, bc, bd, be, cd, ce, de, cao, shark]

renpin = on_keyword(['人品', '运势'], rule=to_me(), priority=5)


@renpin.handle()
async def return_rp(bot: Bot, event: Event, state: T_State):
    usrqq = event.get_user_id()
    t = time.localtime(time.time())
    rand = t.tm_year + t.tm_yday
    raw = str(rand) + usrqq
    raw = str(raw)
    md5_con = md5(raw.encode('utf8')).hexdigest()
    s = [i for i in md5_con if i.isnumeric()]
    rp = str(int("".join(s)) % 101)
    rely = [MessageSegment.at(usrqq), MessageSegment.text("\n你今天的运势为：" + rp)]
    await renpin.finish(rely)



chouqian = on_keyword({"抽签"}, priority=5)


@chouqian.handle()
async def _(bot: Bot, event: Event):
    usrqq = event.get_user_id()
    t = time.localtime(time.time())
    rand = t.tm_year + t.tm_yday
    raw = str(rand) + usrqq
    raw = str(raw)
    md5_con = md5(raw.encode('utf8')).hexdigest()
    s = [i for i in md5_con if i.isnumeric()]
    rp = str(int("".join(s)) % 101)
    myList = ["大吉签"]*3 + ["上上签"]*8 + ["上吉签"]*18 + ["中吉签"]*27 + ["中平签"]*24 + ["中下签"] + ["下下签"]*20
    myList.reverse()
    await chouqian.send("请虔诚祈祷...")
    await chouqian.send("抽签中...")
    rely = [MessageSegment.at(usrqq), MessageSegment.text("\n你今天的签是：[" + str(myList[int(rp)]) + "]")]
    await chouqian.finish(rely)



