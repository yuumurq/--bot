import os
import dotenv
# This example requires the 'message_content' intent.

import discord
import random
dotenv.load_dotenv()
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        kondatelist = ["デミグラスソースハンバーグ","カレイの煮つけ","肉じゃが","トンカツ","カツオのたたき","生姜焼き","エビグラタン","麻婆豆腐","あじの塩焼き","唐揚げ","ピーマンの肉詰め","ポークソテー","鳥の照り焼き","エビチリ","豚丼","カレイの煮つけ","肉じゃが","トンカツ","カツオのたたき","生姜焼き","エビグラタン","麻婆豆腐","あじの塩焼き","唐揚げ","ピーマンの肉詰め","ポークソテー","鳥の照り焼き","エビチリ","豚丼"]

        if message.content == '/kondate':
            await message.channel.send(random.choice(kondatelist))
        print(f'Message from {message.author}: {message.content}')
    

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv("BOT_TOKEN"))



