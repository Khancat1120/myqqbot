import json
import random
from nonebot import on_command, on_keyword
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.rule import to_me
import os

nonereply = on_command("", rule=to_me(), priority=20)

basePath = os.path.abspath(__file__).replace('\\', '/').split("plugins/")[0] + "data/"


@nonereply.handle()
async def _(bot: Bot, event: Event):
    path = basePath + "myImage"
    # 返回path下所有文件构成的一个list列表
    fileList = os.listdir(path)
    # 遍历输出每一个文件的名字和类型
    rely = MessageSegment.image("file:///" + path + "/" + random.choice(fileList))
    await nonereply.finish(rely)


yaqiyuwo = on_keyword({"雅琪与可涵"}, rule=to_me(), priority=5)


@yaqiyuwo.handle()
async def _(bot: Bot, event: Event):
    path = basePath + "yaqiyuwo"
    # 返回path下所有文件构成的一个list列表
    fileList = os.listdir(path)
    # 遍历输出每一个文件的名字和类型
    rely = MessageSegment.image("file:///" + path + "/" + random.choice(fileList))
    await yaqiyuwo.send("注：左边的橘猫是可涵，右边的白猫是雅琪")
    await yaqiyuwo.finish(message=rely)
