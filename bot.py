import discord.app_commands
import os
import dotenv
# This example requires the 'message_content' intent.

import discord
import random
dotenv.load_dotenv()


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)
@tree.command(
    name="kondate",
    description="適当に献立を決めてくれます。"
)
async def hoge(ctx:discord.Interaction):
    kondatelist = ["デミグラスソースハンバーグ","カレイの煮つけ","肉じゃが","トンカツ","カツオのたたき","生姜焼き","エビグラタン","麻婆豆腐","あじの塩焼き","唐揚げ","ピーマンの肉詰め","ポークソテー","鳥の照り焼き","エビチリ","豚丼","カレイの煮つけ","肉じゃが","トンカツ","カツオのたたき","生姜焼き","エビグラタン","麻婆豆腐","あじの塩焼き","唐揚げ","ピーマンの肉詰め","ポークソテー","鳥の照り焼き","エビチリ","豚丼"]
    await ctx.response.send_message(random.choice(kondatelist))
@client.event
async def on_ready():
    await tree.sync()
client.run(os.getenv("BOT_TOKEN"))




