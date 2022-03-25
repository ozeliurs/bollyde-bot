import discord

with open(f"{__file__.split('/main.py')[0]}/.discord", "r", encoding="utf8") as secret:
    TOKEN = secret.read()

client = discord.Client()


def buildIdTable(csv):
    dic = {}
    for line in csv:
        if line[1] not in dic:
            dic[line[1]] = line[2]
    return dic


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

    if message.content.startswith("!evite"):
        await message.channel.send("https://media.discordapp.net/attachments/856154341106647090/953608358127091732/unknown.png")
        await message.delete()

    if message.content.startswith("!nekfeu"):
        await message.channel.send("https://cdn.discordapp.com/attachments/953590491637768202/956903404259672084/ErmxaTxXYAEqmXo.png")
        await message.delete()

    if message.content.startswith("!noodle"):
        await message.channel.send("https://www.youtube.com/watch?v=iOQz2r6ZtR4")
        await message.delete()

    if message.content.startswith("!espuma"):
        await message.channel.send("<@!692684431370223647> https://youtu.be/k3xxquu-pmQ")
        await message.delete()

    if message.content.startswith("!incomodo"):
        link = message.content.split("!incomodo ")[1]
        if link.strip() == "":
            await message.reply("https://youtu.be/0AJfiIHg4fU")
            return
        link = link.split("/")
        await message.delete()
        server = client.get_guild(int(link[4]))
        channel = server.get_channel(int(link[5]))
        message = await channel.fetch_message(int(link[6]))

        reactions = ["<:regional_indicator_i:>", "<:regional_indicator_n:>", "<:regional_indicator_c:>", "<:regional_indicator_o:>", "<:regional_indicator_m:>", "<:o2:>", "<:regional_indicator_d:>", "<:o:>"]

        for emoji in reactions:
            await message.add_reaction(emoji)

        await message.reply("<:hot_face:>")


def main():
    client.run(TOKEN)


if __name__ == "__main__":
    main()
