import discord

with open(f"{__file__.split('/main.py')[0]}/.discord", "r", encoding="utf8") as secret:
    TOKEN = secret.read()

client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\n'
        )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if str(message.author) == "Maxime BILLY#9875":
        pass

    if str(message.author) == "antøskins#8106":
        await message.channel.send("https://cdn.discordapp.com/attachments/755446976631406725/953788321253949510/unknown.png")


def main():
    client.run(TOKEN)


if __name__ == "__main__":
    main()