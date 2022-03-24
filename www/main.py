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

    if message.content.startswith("!incomodo"):
        link = message.content.split("!incomodo ")[1].split("/")
        await message.delete()
        server = client.get_guild(int(link[4]))
        channel = server.get_channel(int(link[5]))
        message = await channel.fetch_message(int(link[6]))

        reactions = [":regional_indicator_i:", ":regional_indicator_n:", ":regional_indicator_c:", ":regional_indicator_o:", ":regional_indicator_m:", ":o2:", ":regional_indicator_d:", ":o:"]
        for emoji in reactions:
            await message.add_reaction(emoji)


    if message.content == "$sutom":
        with open("/data/sutom.csv", "r", encoding="utf8") as sutom:
            sutom = sutom.read().split("\n")
            data = []
            print(sutom)
            for su in sutom:
                print(su)
                if su != "":
                    data.append(su.split(","))

        print(data)

        table = buildIdTable(data)
        players = {}

        for play in data:
            if play[1] not in players:
                players[play[1]] = 0
            if 7 - int(play[3]) > 0:
                players[play[1]] += 7 - int(play[3])

        out = "Résultats :\n"

        for player in players:
            out += f"{table[player]} - {players[player]} points\n"

        await message.channel.send(out)


    if message.content.startswith("SUTOM #"):
        meta = message.content.split("\n")[0]
        _, day, score = meta.split(" ")

        with open("/data/sutom.csv", "a", encoding="utf8") as sutom:
            sutom.write(f"\n{day.strip('#')},{message.author.id},{message.author},{score.split('/')[0]}")


def main():
    client.run(TOKEN)


if __name__ == "__main__":
    main()
