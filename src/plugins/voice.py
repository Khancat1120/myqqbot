from importlib.resources import path
from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, GroupMessageEvent, MessageSegment
from nonebot.rule import to_me
import random
import os

basePath = os.path.abspath(__file__).replace('\\', '/').split("plugins/")[0] + "data/"

dg_voice = on_command("骂我", rule=to_me(), priority=3)

@dg_voice.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    
    if len(str((event.get_message()))) > 1:
        allpath = basePath + "dinggong"
        voice = random.choice(os.listdir(allpath))
        fileName = "file:///" + allpath + "/" + voice
        result = MessageSegment.record(fileName)
        await dg_voice.send(result)
        await dg_voice.send(voice.split("_")[1])



kiss_voice = on_command("给雅琪个亲亲", rule=to_me(), priority=3)

@kiss_voice.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    if len(str((event.get_message()))) > 1:
        allpath = basePath + "kiss"
        voice = random.choice(os.listdir(allpath))
        fileName = "file:///" + allpath + "/" + voice
        result = MessageSegment.record(fileName)
        await kiss_voice.send(result)
        
        
sing_voice = on_command("给雅琪唱首歌", rule=to_me(), priority=3)

@sing_voice.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    usrname = event.get_user_id()
    if usrname not in ['2243581722', '807573173']:
        await sing_voice.send("只有雅琪和开发者可以使用此功能哦")
    else:
        usrmsg = str(event.get_message()).replace('给雅琪唱首歌', '').replace(' ', '')
        allpath = basePath + "songs/" + usrmsg
        fileName = "file:///" + allpath + ".mp3"
        result = MessageSegment.record(fileName)
        await sing_voice.send(result)
        
        
sese_voice = on_command("我要色色", rule=to_me(), priority=3)

@sese_voice.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    if len(str((event.get_message()))) > 1:
        allpath = basePath + "lly"
        voice = random.choice(os.listdir(allpath))
        fileName = "file:///" + allpath + "/" + voice
        result = MessageSegment.record(fileName)
        await sese_voice.send(result)