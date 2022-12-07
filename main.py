
import os
# インストールした discord.py を読み込む
import discord
import asyncio
from discord.ext import tasks
from datetime import datetime 


youtube_url = 'https://www.youtube.com/watch?v=FIw-HUP7XK0' # youtubeのURLを指定

voice = None
player = None
TOKEN = os.environ['TOKEN']

# 接続に必要なオブジェクトを生成
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
     
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    print('エラーなし')
@client.event
async def on_message(message):
  
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '!起動':
        print("起動されました")
        await message.channel.send('東大医学部は頭悪くないか')
        await client.change_presence(activity=discord.Game(name="東大医学部は頭悪くないか"))
        await asyncio.sleep(2)
        await message.channel.send('______うるさい')
        await message.channel.send('本当だからだ')
        await client.change_presence(activity=discord.Game(name="本当だからだ"))
        await message.channel.send('______馬鹿野郎うっせーぞこの野郎')
        await message.channel.send('本当のことを言って何が悪いんだこの馬鹿コラ')
        await client.change_presence(activity=discord.Game(name="本当のことを言って何が悪いんだこの馬鹿コラ"))
        await message.channel.send('______電車の中では静かにしてください')
        await message.channel.send('そういうことだぁぁ')
        await client.change_presence(activity=discord.Game(name="そういうことだぁ"))
        await message.channel.send('わかったかぁ')
        await client.change_presence(activity=discord.Game(name="わかったかぁ"))
        await asyncio.sleep(1)
        await message.channel.send('______知らねーよ')
        await message.channel.send('知らねぇじゃねぇ')
        await client.change_presence(activity=discord.Game(name="知らねぇじゃねぇ"))
        await message.channel.send('なんでお前が正しいんだ')
        await client.change_presence(activity=discord.Game(name="なんでお前が正しいんだ"))
        await asyncio.sleep(3)
        await message.channel.send('正しいコンギョを言え')
        await client.change_presence(activity=discord.Game(name="*正しいコンギョを言え*"))
    if message.content == 'できた':
        print("『できた』のコマンドが実行されました")
        await message.channel.send('できたじゃねぇこれからが未完成だ(?)')
    if message.content == 'つかれた':
        print("『つかれた』のコマンドが実行されました")
        await message.channel.send('つかれた？つかれた後が本領発揮だろ')
    if message.content == 'w':
        print("『w』のコマンドが実行されました")
        await message.channel.send('その心笑ってるねぇ')
    if message.content == 'おはよう':
        print("『おはよう』のコマンドが実行されました")
        await message.channel.send('おはよう今日も頑張ろう')
    if message.content == 'あーね':
        print("『あーね』のコマンドが実行されました")
        await message.channel.send('あーねって要はわからなくてどう返事すればいいかわかんない時も使うんだおw')
    if message.content == 'うざ':
        print("『うざ』のコマンドが実行されました")
        await message.channel.send('うざくても我慢しよう')
    if message.content == 'わからん':
        print("『わからん』のコマンドが実行されました")
        await message.channel.send('じゃぁ調べろggrks')
    if message.content == 'おはよう':
        print("『おはよう』のコマンドが実行されました")
        await message.channel.send('おはよう今日も頑張ろう')
    if message.content == 'めんどい':
        print("『めんどい』のコマンドが実行されました")
        await message.channel.send('がんばれ')
    if message.content == "!help":
        embed = discord.Embed(title="help?",description="これは伊吹chがつくった高機能botです\nコマンド\n!起動=コンギョを言えおじさん\n!help=今開いてるこれ\nそのた会話に応じてチャットします",color=0xff0000)
        await message.channel.send(embed=embed)
    if message.content == "!D":
        embed = discord.Embed(title="デトロッパー",description="デトロッパーツール\n開発OS\n 1.mac 2.windows\n開発ソフト\nvisualstudiochord2019",color=0xff0000)
        await message.channel.send(embed=embed)
    

    
client.run(TOKEN)