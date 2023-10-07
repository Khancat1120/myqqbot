# -*- coding: utf-8 -*-
from nonebot import *
from nonebot.plugin import on_keyword, on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

help = on_keyword({'help', '功能', '你会干什么', "你会做什么", "你会什么", "菜单"}, rule=to_me())


@help.handle()
async def handle_help(bot: Bot, event: Event, state: T_State):
    ret_help = await get_help()
    await help.finish(ret_help)


async def get_help():
    return f"欢迎使用雅琪专属QQ机器人\n使用方法：@bot 输入指令，如果bot没有反应看看是不是复制了别人的命令或者格式不对？需要自己手动艾特bot哦。\n\
            已实现功能：\n\
            -输入关键词 “帮助/help/功能” 获取帮助菜单\n\
            -对话功能   “对话内容自行探索”\n\
            -输入指令   “歌单” 获取歌单\n\
            -输入指令   “冷笑话/笑话” 获取随机冷笑话\n\
            -输入指令   “天气 城市” 获取城市天气\n\
            -输入指令   “新闻” 获取每日新闻速报\n\
            -输入指令   “疫情 城市” 获取疫情速报\n\
            -输入指令   “情话” 获取随机情话\n\
            -输入指令   “骚话” 获取随机骚话\n\
            -输入指令   “度娘 关键字” 获取百度百科，此功能有冷却时间\n\
            -输入指令   “mc” 获取menhera酱表情包\n\
            -输入指令   “降水” 获取降水图\n\
            -输入指令   “漫画” 获取随机漫画\n\
            -输入指令   “抽签” 进行今日抽签\n\
            -输入关键词 “运势+空格/逗号+版本强势CP名/人物” 获取该人物/cp今日运势\n\
            -输入关键词 “日程表” 获取本周A-soul日程表\n\
            -输入关键词 “粉丝数” 获取A-soul实时粉丝数\n\
            -输入指令   “人品/运势” 获取你今日的运势\n\
            -输入指令   “remake/重开” 获取重开结果\n\
            -输入关键词 “吃什么”等 获取该吃什么\n\
            -输入指令   “小作文” 获取随机小作文\n\
            -输入指令   “狗屁不通 主题 生成一段狗屁不通的文章\n\
            -输入指令   “概率 事件 获取某事发生的概率\n\
            -输入指令   “绝绝子 事件 生成绝绝子小短文\n\
            -输入指令   “吃瓜 获取微博热搜\n\
            -输入指令   “点歌+歌名 网易云点歌\n\
            -输入指令   “切片” 获取A-Soul随机切片"


waibi = on_keyword({"阿巴阿巴"}, rule=to_me())


@waibi.handle()
async def handle_waibi(bot: Bot, event: Event, state: T_State):
    ret_help = await get_waibi()
    await waibi.finish(ret_help)


async def get_waibi():
    return f"欢迎使用色图QQ机器人\n\
            使用方法：@bot 输入指令，如果bot没有反应看看是不是复制了别人的命令或者格式不对？需要自己手动艾特bot哦。\n\
            已实现功能：\n\
            -输入关键词 “帮助/help/功能” 获取帮助菜单\n\
            -对话功能   “对话内容自行探索”\n\
            -色图功能   “色图/不够色/色图六连/色图十连”\n\
            -买家秀功能   “输入买家秀 获得淘宝福利买家秀”\n\
            -coser功能   “输入coser 获得coser图片”\n\
            -福利姬功能   “输入福利姬/写真 获取随机女菩萨图片”\n\
            -盲盒功能   “完全随机获取图片”\n\
            -JK功能   “获取黑丝/白丝JK”\n\
            -输入指令   “冷笑话/笑话” 获取随机冷笑话\n\
            -输入指令   “天气 城市” 获取城市天气\n\
            -输入指令   “疫情 城市” 获取疫情速报\n\
            -输入指令   “情话” 获取随机情话\n\
            -输入指令   “骚话” 获取随机骚话\n\
            -输入指令   “度娘 关键字” 获取百度百科，此功能有冷却时间\n\
            -输入指令   “mc” 获取menhera酱表情包\n\
            -输入指令   “降水” 获取降水图\n\
            -输入指令   “漫画” 获取随机漫画\n\
            -输入指令   “抽签” 进行今日抽签\n\
            -输入关键词 “运势+空格/逗号+版本强势CP名/人物” 获取该人物/cp今日运势\n\
            -输入关键词 “日程表” 获取本周A-soul日程表\n\
            -输入关键词 “粉丝数” 获取A-soul实时粉丝数\n\
            -输入指令   “人品/运势” 获取你今日的运势\n\
            -输入指令   “remake/重开” 获取重开结果\n\
            -输入关键词 “吃什么”等 获取该吃什么\n\
            -输入指令   “小作文” 获取随机小作文\n\
            -输入指令   “狗屁不通 主题 生成一段狗屁不通的文章\n\
            -输入指令   “概率 事件 获取某事发生的概率\n\
            -输入指令   “绝绝子 事件 生成绝绝子小短文\n\
            -输入指令   “匹配 匹配对象 测试你和ta的匹配程度吧\n\
            -输入指令   “来个猫猫 获取随机猫猫图片\n\
            -输入指令   “骂我/我要色色 获取色色语音\n\
            -输入指令   “图片搜索” 搜取图片出处\n\
            -输入指令   “P站排行榜及关键字搜图使用帮助：\n\
                        可选参数：类型：\n\
                          1. 日排行\n\
                          2. 周排行\n\
                          3. 月排行\n\
                          4. 原创排行\n\
                          5. 新人排行\n\
                          6. R18日排行\n\
                          7. R18周排行\n\
                          8. R18受男性欢迎排行\n\
                          9. R18重口排行【慎重！】\n\
                        【使用时选择参数序号即可，R18仅可私聊】\n\
                         p站排行榜 [参数] [数量](可选) [日期](可选)\n\
                         示例：\n\
                            p站排行榜   （无参数默认为日榜）\n\
                            p站排行榜 1\n\
                            p站排行榜 1 5\n\
                            p站排行榜 1 5 2018-4-25\n\
                        【注意空格！！】【在线搜索会较慢】片\n\n\
                        P站搜图帮助：\n\
                        可选参数：\n\
                            1.热度排序\n\
                            2.时间排序\n\
                        【使用时选择参数序号即可，R18仅可私聊】 \n\
                        搜图 [关键词] [数量](可选) [排序方式](可选) [r18](可选)\n\
                        示例：\n\
                            搜图 樱岛麻衣\n\
                            搜图 樱岛麻衣 5 1\n\
                            搜图 樱岛麻衣 5 2 r18\n\
                        【默认为 热度排序】\n\
                        【注意空格！！】【在线搜索会较慢】【数量可能不符】\n\
            -输入指令   “切片” 获取A-Soul随机切片"


gedan = on_command("歌单", rule=to_me())


@gedan.handle()
async def handle_gedan(bot: Bot, event: Event, state: T_State):
    ret_help = await get_gedan()
    await gedan.finish(ret_help)


async def get_gedan():
    return f"让我来为雅琪唱一首歌吧！\n\
            使用方法：给雅琪唱首歌+空格+歌曲名+片段id\n\
            示例：给雅琪唱首歌 孤勇者0\n\
            歌单：\n\
            -孤勇者[1~5]\n\
            -勾指起誓[1~5]\n\
            -你的猫咪[1~7]\n\
            -鹊引桥[1~4]\n\
            -达拉崩吧[1~7]\n\
            -化身孤岛的鲸[1~6]\n\
            -起风了[1~5]\n\
            -吃醋[1~3]\n\
            -亲爱的旅人[1~6]"