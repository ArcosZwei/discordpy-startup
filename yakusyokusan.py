# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NzY4NzA5MDQxNjI2OTM5NDIy.X5EaFQ.pX2Oi08tgL-gwOgYUi3g0pQTzf0'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)

ID_CHANNEL_README = 192278756553916416 # 該当のチャンネルのID
ID_ROLE_WELCOME = 768709394321244160 # 付けたい役職のID

@client.event
async def on_raw_reaction_add(payload):
    # channel_id から Channel オブジェクトを取得
    channel = client.get_channel(payload.channel_id)

    # 該当のチャンネル以外はスルー
    if channel.id != ID_CHANNEL_README:
        return

    # guild_id から Guild オブジェクトを取得
    guild = client.get_guild(payload.guild_id)

    # user_id から Member オブジェクトを取得
    member = guild.get_member(payload.user_id)

    # 用意した役職IDから Role オブジェクトを取得
    role = guild.get_role(ID_ROLE_WELCOME)

    # リアクションを付けたメンバーに役職を付与
    await member.add_roles(role)

    # 分かりやすいように歓迎のメッセージを送る
    await channel.send('いらっしゃいませ！')
