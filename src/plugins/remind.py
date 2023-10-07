import random
import os
from nonebot import require
import nonebot
import requests

scheduler = require('nonebot_plugin_apscheduler').scheduler
group_id = 902230120
yaqi_id = 807573173
bot_id = '454427917'

basePath = os.path.abspath(__file__).replace('\\', '/').split("plugins/")[0] + "data/test/"


@scheduler.scheduled_job('cron', day_of_week="wed,sun", hour=20, minute=00)
async def _():
    bot = nonebot.get_bots()[bot_id]
    rely = [
        {
            "type": "at",
            "data": {
                "qq": "all",
                "name": ""
            }
        },
        {
            "type": "text",
            "data": {
                "text": "\n大家好，我是本群机器人，请停下手中的工作，让我来给你讲个恐怖故事：\n今晚深渊结算"
            }
        },
        {
            "type": "image",
            "data": {
                "file": "file:///" + basePath + "shenyuan.png"
            }
        }
    ]
    await bot.send_group_msg(group_id=929242692, message=rely)


@scheduler.scheduled_job('cron', hour=21, minute=00)
async def _():
    bot = nonebot.get_bots()[bot_id]
    rely = [
        {
            "type": "at",
            "data": {
                "qq": "all",
                "name": ""
            }
        },
        {
            "type": "text",
            "data": {
                "text": "\n大家好，我是本群的提醒摆烂小助手，如果各位不打游戏的话也不摆烂的话请滚去睡觉，谢谢"
            }
        },
        {
            "type": "image",
            "data": {
                "file": "file:///" + basePath + "bai.gif"
            }
        }
    ]
    await bot.send_group_msg(group_id=929242692, message=rely)
