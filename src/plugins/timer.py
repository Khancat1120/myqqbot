import random
import os
from nonebot import require
import nonebot
import requests

scheduler = require('nonebot_plugin_apscheduler').scheduler

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

group_id = 902230120
yaqi_id = 807573173
bot_id = '454427917'
qinghualist = [
    "做梦也想不到我会把信写在五线谱上吧。五线谱是偶然来的，你也是偶然来的。不过我给你的信值得写在五线谱里呢。但愿我和你，是一支唱不完的歌。我和你就好像两个小孩子，围着一个神秘的果酱罐，一点一点尝它，看看里面有多少甜。",
    "还有我。我是爱你的，看见就爱上了。我爱你爱到不自私的地步。就像一个人手里一只鸽子飞走了，他从心里祝福那鸽子的飞翔。你也飞吧。我会难过，也会高兴，到底会怎么样我也不知道。",
    "我真不知怎么才能和你亲近起来，你好像是一个可望而不可及的目标，我琢磨不透，追也追不上，就坐下哭了起来。",
    "你想知道我对你的爱情是什么吗？就是从心底里喜欢你，觉得你的一举一动都很亲切，不高兴你比喜欢我更喜欢别人。你要是喜欢了别人我会哭，但是还是喜欢你。你肯用这样的爱情回报我吗？就是你高兴我也高兴，你难过时我来安慰你，还有别爱别人！",
    "我把我整个的灵魂都给你，连同它的怪癖，耍小脾气，忽明忽暗， 一千八百种坏毛病。它真讨厌，只有一点好，爱你。",
    "你是非常可爱的人，真应该遇到最好的人，我也真希望我就是。",
    "自从我认识了你，我觉得所有的人都黯然失色，再也没有谁比你更好了。",
    "男孩子们都喜欢女孩子，可是谁也没有我喜欢你这么厉害。",
    "你真好，我真爱你。可惜我不是诗人，说不出再动人一点的话了",
    "不管我本人多么平庸，我总觉得对你的爱很美。",
    "我和你分别以后才明白，原来我对你爱恋的过程全是在分别中完成的，就是说，每一次见面之后，你给我的印象都使我，在余下的日子里用我这愚笨的头脑里可能想到的一切称呼，来呼唤你。",
    "你要是愿意，我就永远爱你，你要是不愿意，我就永远相思。",
    "我永远不会想把别人的灵魂据为己有。我只希望我们的灵魂可以互通，像一个两倍大的共同体。"
    "你知道吗，孤独的灵魂多么寂寞啊，人又有多少弱点啊。\
    一个像你这样的灵魂可以给人多么大的助力，给人多少温暖啊！你把你灵魂的大门开开，让我进去吧！本着这些信念，我很希望你绝对自由，我希望你的灵魂高飞。当然，你将来爱上别人，不就说明我的灵魂暗淡了吗。",
    "静下来想你，觉得一切都美好得不可思议。以前我不知道爱情这么美好，爱到深处这么美好。真不想让任何人来管我们。谁也管不着，和谁都无关。告诉你，一想到你，我这张丑脸上就泛起微笑。 ",
    "只希望你和我好，互不猜忌，也互不称誉，安如平日，你和我说话就像对自己说话一样，我和你说话也像对自己说话一样。你说，和我好么？ ",
    "说真的，我喜欢你的热情，你可以温暖我。我很讨厌我自己不温不凉的思虑过度，也许我是个坏人。不过我只要你吻我一下就会变好呢。",
    "只要我们真正相爱，哪怕只有一天，一个小时，我们就不应该再有一刀两断的日子。\
    也许你会在将来不爱我，也许你要离开我，但是我永远对你负有责任，就是你的一切苦难就永远是我的。我觉得我爱了你了，从此以后，不管什么时候我都不能对你无动于衷。我可不能赞成爱里面一点责任没有。我当然反对它成为一种枷锁，我也不能同意它是一场宴会。我以为它该是终身不能忘却的。比如说，将来你不爱我了，那你就离开我，可是别忘了它。这是不该忘记的东西。",
    "碰上了，然后就爱了，然后一点办法也没有。",
    "请你不要吃我，我给你唱一支好听的歌。",
    "我会不爱你吗？不爱你？不会。爱你就像爱生命。",
    "我好想把自己变小，这样你就能把我放到口袋里，我想你了就自己钻出来看看你",
    "我想作诗，写雨，写夜的相思，写你，写不出。",
    "不要愁老之将至，你老了一定很可爱。而且，假如你老了十岁，我当然也同样老了十岁，世界也老了十岁，太阳也老了十岁，月亮也老了十岁，一切都是一样的。",
    "我是，我是高雅琪至上主义者。",
    "要是世上只有我们两个人多么好，我一定要把你欺负得哭不出来。",
    "我渴望和你打架，也渴望抱抱你。",
    "我爱你也许并不为什么理由，虽然可以有理由，例如你聪明，你纯洁，你可爱，你是好人等，但主要的原因大概是你全然适合我的趣味。因此你仍知道我是自私的，故不用感激我。",
    "我想要在茅亭里看雨、假山边看蚂蚁，看蝴蝶恋爱，看蜘蛛结网，看水，看船，看云，看瀑布，看宋清如甜甜地睡觉。",
    "以前我最大的野心，便是成为你的好朋友；现在我的野心，便是希望这样的友谊能持续到死时。谢谢你给我一个等待。",
    "一见到你我就容易被罚款，因为，我心里乱撞的小鹿超速了，说的我自己都脸红",
    "我生在北方，活在北方，栽在你手里，总算是去过不一样的地方",
    "我想吃碗面,你的心里面",
    "我本来是要行走江湖的，但遇见你我觉得可以先停一停",
    "不敢正视你的眼睛，我怕我每个眼神都像在表白",
    "你可以帮我个忙么? 帮忙快点爱上我!",
    "我去买生蚝 回家的路上生蚝全都跳出袋子 钻到了泥土里 原来这就叫蚝喜欢泥",
    "你可以教我包饺子吗？我有点笨，做什么都容易露馅，喜欢你也是~",
    "宙斯，雅典娜，波塞冬，阿尔忒密斯，你猜我最喜欢哪个神？我最喜欢，你的眼神啊",
    "我可以称呼你为您吗?这样我就可以把你放在心上。",
    "我超级酷，但是如果你和我聊天的话，我可以不酷那么一小会儿",
    "你是超可爱的女孩子，我是超可爱",
    "不要抱怨，抱我",
    "我怀疑你的本质是一本书，不然为什么你让我越看越想睡？",
    "近朱者赤，近你者甜",
    "你为什么要害我？害我那么喜欢你",
    "面对你，我不仅善解人意，还善解人衣",
    "每天只想和你做四件事——一日三餐",
    "既然你把我的心已经弄乱了，那你打算什么时候来弄乱我的床？",
    "有些事不用在一晚内做完的，我们又不赶时间，可以每晚都做一做",
    "人生呐，最美好的两件事，就是睡你——睡觉，和你",
    "我发现昨天很喜欢你，今天也很喜欢你，而且有预感明天也会喜欢你",
    "我的身体24小时都营业，只等待你的进入",
    "你知道我最爱的是什么吗？现在看这句话第一个字就知道了",
    "你是甜筒吗？为什么我想舔遍你全身",
    "我想你一定很忙，所以只看前三个字就好啦",
    "你问我多喜欢你，我说不出来。但是我心里明白，我宁愿和你吵架，也不愿意去爱别人",
    "你最可爱了。我说的时候来不及思索，我仔细想过之后，还是会这么说",
    "想送你很多很多口红，让你每天还我一点点",
    "今天我想你想的，连续换了五条内裤",
    "我喜欢春天的花，夏天的雨，秋天的风，冬天的雪，和任何时候的你",
    "人总是会变的，从一开始的喜欢你，到后来的更喜欢你",
    "风止于秋水，落叶止于根，我止于你",
    "好好照顾自己，不行就让我来照顾你",
    "你今天干嘛打扮成这个样子，好看不说，偏偏是我喜欢的样子",
    "你今天可真讨厌。讨人喜欢和百看不厌",
    "眼里都是你，亿万星辰犹不及",
    "有趣的地方都想去掺和一下，比如你的世界",
    "今天不是你死就是我死，你可爱死了，我爱死你了",
    "你上辈子一定是碳酸饮料吧？我一看到你就开心得冒泡",
    "不辞青山，相随与共",
    "千里山水藏于心，你藏山水里",
    "我爱你甚于昨日，略匮明朝",
    "三更梦醒，你是檐上落下的星",
    "江南春不如你，横水秋也不如你",
    "万里河山如梦，不如你青丝如瀑",
    "此生棠棣开荼蘼，三遍荣华不如你",
    "菩提树下说执迷，云海涛生皆是你",
    "已是人海孤鸿，你似清晨朝暮",
    "乍见心欢，小别思恋，久处仍怦然",
    "你是天赐的礼物，我迟来的救赎",
    "你和我之间，不需要时间在场",
    "理解归理解，醋我还是要吃的",
    "你是生活扑面而来的善意",
    "想当你的小尾巴，屁颠颠的那种",
    "我喜欢你是从心底到眼里都藏不住的粉色",
    "所幸遇你，从此山河旖旎，都不及你",
    "我永远屈服于温柔，而你就是温柔本身",
    "对你的喜欢总是止不住的悸动",
    "我三观不正，很歪，全向着你",
    "你是个可爱又浪漫的麻烦",
    "你是落日弥漫的橘，天边透亮的星",
    "当下心动便是最珍贵",
    "月亮照回湖心，野鹤奔向闲云，我步入你",
    "世界需要讲讲道理，但我最偏心你",
    "我想和你一屋两人，门外奔波，门内亲吻",
    "晚是世界的晚，安是给你的安",
    "我对全世界说晚安，独独对你说喜欢",
    "你真可爱，我说时来不及思索，而思索之后，还是这样说",
    "希望我能成为你的小众喜好，藏着时欣喜不已，炫耀时格外骄傲",
    "这个世界上的美丽多半大同小异，就好比我觉得好看的人，都像你",
    "从前，我见山是大地峻冷的脊背，见水是星象的眼泪，见雪是世纪的白象，直到见了你，我踏过土地，捧起泉水，接过下落的雪花，万物都于我有了生灵，你无需开口，就让我从虚空下坠，落地开花",
    "爱你就像爱生命",
    "喜你成疾，药石无医",
    "有什么不懂的尽管吻我",
    "我想到你的房间去看月亮",
    "喜欢你，春夏秋冬的喜欢",
    "所有的日记都知道我喜欢你",
    "你是书吗，怎么越看越想睡",
    "春眠不觉晓，处…处对象可好",
    "风一不小心就把你吹进我眼里",
    "我和你除了恋爱没什么好谈的",
    "你是年少的欢喜，倒过来念也是",
    "被你点赞过的朋友圈，叫甜甜圈",
    "我是九你是三，我除了你还是你",
    "幸得识君桃花面，从此阡陌多暖春",
    "麻烦你笑一下，我的咖啡忘加糖了",
    "子曰三思而后行，1.2.3，我喜欢你",
    "你若携风来叩，我必以满屋芬芳相迎",
    "我心中有一幅山水，落款的你的名字",
    "我想要两颗西柚，I want to see you",
    "一支圆珠笔，可以写5693个你的名字",
    "你胖了真好，喜欢你的地方又多了一圈",
    "不管我本人多么平庸，我总觉得对你的爱很美",
    "真想当个医生啊，这样就能听听你的心里话了",
    "哪来这么多情话，我看你的每一个眼神都是表白",
    "“医生说我有低血糖，需要你跟我说几句甜蜜的话",
    "”等你心里的树结果了，能不能邀请我去当一次牛顿呢",
    "我喜欢你,在所有时候,也喜欢有些人,在他们偶尔像你的时候”",
    "如果你前女友和现女友同时掉到水里，我可以做你女朋友吗？我身上的每一斤肉都很想你，它们和思念一样，都是沉甸甸的",
    "我有两个可爱之处你知道吗 ？一个是我可爱，另一个是我可爱你了",
    "小猪佩奇你配我",
    "我办事十拿九稳，唯独少你一吻。",
    "“我今天不吃肉，吃素”，“为什么啊!” “因为你是我的菜啊!”",
    "我觉得你今天有点怪，哪里怪了，怪可爱的。",
    "“你怎么这么宅?”“没有啊”，“有啊，你在我心里都没动过!”",
    "你知道我最喜欢吃什么水果吗?你这个开心果。",
    "“你为什么要害我”，“我怎么害你了?”“害我这么喜欢你!”",
    "走在路上被泥溅了一身，回去一查才知道这泥叫做我好想泥。",
    "你知道昨天是什么日子吗?是我爱了你一天的日子。",
    "你是喜欢苹果汁，还是桃子汁，还是我这个小傻汁。",
    "世界上有五种辣：微辣，中辣，麻辣，变态辣，我想你辣!",
    "我要露出点小马脚来，好让你知道我喜欢你",
    "我不喜欢夏天，但我喜欢有你的夏天",
    "遇见你的机率，很小，可还是遇见了，真好",
    "你知道我最近为什么吃素吗，因为你是我的菜",
    "千万别跟我客气，早晚都是一个户口本上的人",
    "喜欢不是一件浪漫的事，喜欢你才是",
    "你愿不愿你带我回家当你的生活必须品",
    "我这个做事拖拖拉拉，唯一高效的一次，是初次见面就喜欢你",
    "没学过礼尚往来吗，我喜欢你，你也得喜欢我",
    "你愿不愿你带我回家当你的生活必须品"
]


def getRandombqb():
    path = os.path.abspath(__file__).replace('\\', '/').split("plugins/")[0] + "data/myImage"
    # 返回path下所有文件构成的一个list列表
    fileList = os.listdir(path)
    # 遍历输出每一个文件的名字和类型
    rely = {
        "type": "image",
        "data": {
            "file": "file:///" + path + "/" + random.choice(fileList)
        }
    }
    return rely


@scheduler.scheduled_job('cron', hour=6, minute=00)
async def _():
    weatherStr = weather.get_city_weather("北京", "北京")
    bot = nonebot.get_bots()[bot_id]
    await bot.call_api('send_msg', **{
        'user_id': 807573173,
        'message': "现在是6点啦，雅琪宝宝，是不是要起床了？今天天气" + weatherStr + "起床后要注意更换合适的衣服哦，如果有下雨别忘了带上雨伞！"
    })


@scheduler.scheduled_job('cron', hour=8, minute=0)
async def _():
    bot = nonebot.get_bots()[bot_id]
    await bot.call_api('send_msg', **{
        'user_id': 807573173,
        'message': "现在是8点啦，雅琪宝宝，可涵初号机也马上要上线咯，有没有一点清醒了？精神精神准备迎接新的一天吧~爱你哦"
    })


@scheduler.scheduled_job('cron', hour=9, minute=0)
async def _():
    bot = nonebot.get_bots()[bot_id]
    await bot.call_api('send_msg', **{
        'user_id': 807573173,
        'message': "已经9点啦，雅琪小猪，快去泡点热茶喝，喝茶有助于缓解压力，清肝明目哦~"
    })


@scheduler.scheduled_job('cron', hour=10, minute=00)
async def _():
    bot = nonebot.get_bots()[bot_id]
    await bot.call_api('send_msg', **{
        'user_id': 807573173,
        'message': "现在是10点00分啦，雅琪小猪，有没有在想我？"
    })


@scheduler.scheduled_job('cron', hour=11, minute=00)
async def _():
    bot = nonebot.get_bots()[bot_id]
    await bot.call_api('send_msg', **{
        'user_id': 807573173,
        'message': "现在是11点啦，雅琪宝宝，别总在办公桌前坐着，起来走一走吧~顺便想想午饭该吃什么"
    })


@scheduler.scheduled_job('cron', hour=12, minute=00)
async def _():
    bot = nonebot.get_bots()[bot_id]
    await bot.call_api('send_msg', **{
        'user_id': 807573173,
        'message': "现在是12点啦，雅琪小猪，中午要多吃点哦，记得要吃快点，还能多午休一会儿"
    })


@scheduler.scheduled_job('cron', hour=13, minute=00)
async def _():
    bot = nonebot.get_bots()[bot_id]
    await bot.call_api('send_msg', **{
        'user_id': 807573173,
        'message': "现在是13点啦，雅琪小猪，不要一直看手机啦，趴着休息一会儿吧"
    })


@scheduler.scheduled_job('cron', hour=14, minute=00)
async def _():
    bot = nonebot.get_bots()[bot_id]
    await bot.call_api('send_msg', **{
        'user_id': 807573173,
        'message': "下午2点咯，雅琪小猪，是在睡觉做着美梦还是在努力工作啊？啵啵"
    })


@scheduler.scheduled_job('cron', hour=15, minute=00)
async def _():
    bot = nonebot.get_bots()[bot_id]
    await bot.call_api('send_msg', **{
        'user_id': 807573173,
        'message': "现在是15点00分啦，雅琪小猪，清醒清醒，别继续睡了，不然晚上就要睡不着咯，抓紧开始工作吧"
    })


@scheduler.scheduled_job('cron', hour=16, minute=00)
async def _():
    bot = nonebot.get_bots()[bot_id]
    await bot.call_api('send_msg', **{
        'user_id': 807573173,
        'message': "小猪，4点咯，该去泡下午喝的热茶了！要精神地面对下午的工作哦"
    })


@scheduler.scheduled_job('cron', hour=17, minute=00)
async def _():
    bot = nonebot.get_bots()[bot_id]
    await bot.call_api('send_msg', **{
        'user_id': 807573173,
        'message': "雅琪小猪，已经5点了，别一直坐着，快起来活动活动身体，晚上打算在点外卖还是在食堂吃呀"
    })


@scheduler.scheduled_job('cron', hour=18, minute=00)
async def _():
    bot = nonebot.get_bots()[bot_id]
    await bot.call_api('send_msg', **{
        'user_id': 807573173,
        'message': "小猪，6点啦，快起来活动活动哦，一直在办公桌前坐着对身体不好！"
    })


@scheduler.scheduled_job('cron', hour=19, minute=00)
async def _():
    bot = nonebot.get_bots()[bot_id]
    await bot.call_api('send_msg', **{
        'user_id': 807573173,
        'message': "小猪，晚饭吃什么好吃的呢？"
    })


@scheduler.scheduled_job('cron', hour=20, minute=00)
async def _():
    bot = nonebot.get_bots()[bot_id]
    await bot.call_api('send_msg', **{
        'user_id': 807573173,
        'message': "小猪，8点了哦，在干嘛呀？有没有想我？"
    })


@scheduler.scheduled_job('cron', hour=21, minute=00)
async def _():
    bot = nonebot.get_bots()[bot_id]
    await bot.call_api('send_msg', **{
        'user_id': 807573173,
        'message': "雅琪宝宝，9点咯，不要一直打游戏哦，作业做完了吗？"
    })


@scheduler.scheduled_job('cron', hour=22, minute=30)
async def _():
    bot = nonebot.get_bots()[bot_id]
    await bot.call_api('send_msg', **{
        'user_id': 807573173,
        'message': "现在是22点30分啦，雅琪小猪，该睡觉啦，不然明天又要起不来了，笨蛋"
    })


@scheduler.scheduled_job('cron', hour=0, minute=0)
async def _():
    bot = nonebot.get_bots()[bot_id]
    await bot.call_api('send_msg', **{
        'user_id': 807573173,
        'message': "已经12点咯，小猪是不是在做着甜甜的梦呢？让我来做你梦中的守护神吧，如果有任何问题请给初号机打电话哦，晚安，做个甜甜的梦。"
    })


@scheduler.scheduled_job('cron', hour=2, minute=30)
async def _():
    bot = nonebot.get_bots()[bot_id]
    await bot.call_api('send_msg', **{
        'user_id': 807573173,
        'message': "已经2点半啦，雅琪小猪在梦里干什么呢？你不是一个人哦，有我陪着你呢~"
    })


@scheduler.scheduled_job('cron', hour="*", minute=15)
async def _():
    bot = nonebot.get_bots()[bot_id]
    url = ["https://api.iyk0.com/zhanan/", "https://api.iyk0.com/twqh"]
    UserAgent = random.choice(user_agent_list)
    headers = {'user-agent': UserAgent}
    r = requests.get(url[-1], headers=headers, verify=False)
    c = r.text

    await bot.call_api('send_msg', **{
        'user_id': 807573173,
        'message': random.choice(qinghualist)
    })
    await bot.call_api('send_msg', **{
        'user_id': 807573173,
        'message': getRandombqb()
    })


@scheduler.scheduled_job('cron', hour="*", minute=45)
async def _():
    bot = nonebot.get_bots()[bot_id]
    url = "https://api.iyk0.com/chp/"
    UserAgent = random.choice(user_agent_list)
    headers = {'user-agent': UserAgent}
    r = requests.get(url, headers=headers, verify=False)
    c = r.json()
    c = c['txt']

    await bot.call_api('send_msg', **{
        'user_id': 807573173,
        'message': random.choice(qinghualist)
    })
    await bot.call_api('send_msg', **{
        'user_id': 807573173,
        'message': getRandombqb()
    })


# @scheduler.scheduled_job('cron', hour="*", minute=0)
# async def _():
#     bot = nonebot.get_bots()[bot_id]
#     # sentence = random.choice(qinghualist)
#     url = "https://api.iyk0.com/chp/"
#     UserAgent = random.choice(user_agent_list)
#     headers = {'user-agent': UserAgent}
#     r = requests.get(url, headers=headers, verify=False)
#     c = r.json()
#     sentence = c['txt']
#     await bot.call_api('send_msg', **{
#         'user_id': 2251723362,
#         'message': sentence
#     })
#     await bot.call_api('send_msg', **{
#         'user_id': 2251723362,
#         'message': getRandombqb()
#     })
