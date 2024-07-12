import discord
import random
import asyncio
from datetime import datetime, timedelta

# قائمة الأكواد العشوائية
codes = [
    "BLAZE-6H-N6Z0-R7PA",
    "BLAZE-6H-MXSX-4MYZ",
    "BLAZE-6H-GBEY-8R65",
    "BLAZE-6H-RQ7H-57U9",
    "BLAZE-6H-MXYR-PYA7",
    "BLAZE-6H-PF56-GJZ8",
    "BLAZE-6H-8FB4-XWCA",
    "BLAZE-6H-KP5C-KTU5",
    "BLAZE-6H-EGNP-DZ6Y",
    "BLAZE-6H-IZYV-LIWG",
    "BLAZE-6H-PJQ9-JAFU",
    "BLAZE-6H-9Z6A-LV3Q",
    "BLAZE-6H-KM3F-MHGF",
    "BLAZE-6H-1OZJ-V99A",
    "BLAZE-6H-YPJY-WUNN",
    "BLAZE-6H-DHEK-5GMQ",
    "BLAZE-6H-FXHR-SOLN",
    "BLAZE-6H-LR1Y-EA78",
    "BLAZE-6H-DDCQ-SUYZ",
    "BLAZE-6H-SHJC-VPX6",
    "BLAZE-6H-H3HG-C8N6",
    "BLAZE-6H-RPZ1-NGGG",
    "BLAZE-6H-QOLQ-EQ2S",
    "BLAZE-6H-OWBD-V5JM",
    "BLAZE-6H-5WWK-CCMO",
    "BLAZE-6H-4AHV-Q90C",
    "BLAZE-6H-LEBD-3BHB",
    "BLAZE-6H-67CF-GHQD",
    "BLAZE-6H-BJ2E-CX6C",
    "BLAZE-6H-KQXH-BM67"
]


# قائمة لتخزين الأكواد المستخدمة
used_codes = []

# قائمة لتخزين الأكواد المرسلة مع الوقت الذي تم فيه الإرسال
sent_codes = []

# مهلة بين كل كود (6 ساعات)
cooldown_time = timedelta(hours=6)

# إعداد نوايا البوت
intents = discord.Intents.default()
intents.message_content = True

# تعريف البوت
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!key'):
        if len(used_codes) == len(codes):
            await message.channel.send('ALL KEYS STOCK IS FINISHED WAIT FOR REFILL')
        else:
            user = message.author

            # التحقق مما إذا كان الكود قد تم إرساله مؤخراً
            now = datetime.now()
            recent_codes = [code_info for code_info in sent_codes if (now - code_info[1]) < cooldown_time]

            if any(code[0] == user.id for code in recent_codes):
                await message.channel.send('Please Wait  6 Hours Before Get New Key')
            else:
                available_codes = [code for code in codes if code not in used_codes]
                code = random.choice(available_codes)
                used_codes.append(code)
                sent_codes.append((user.id, datetime.now()))
                await user.send(f'Your code is: {code}')
                await message.channel.send(f'Key was sent to you, check your DM.')

client.run('MTI2MTI3ODY0MzY0MDk5MTc3NA.GDjGNy.EFsBHW_KXAHC7Xi6HZ_FaYUctjNCTlu7TDq100')
