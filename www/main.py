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

    if message.content == "$sutom":
        with open("/data/sutom.csv", "r", encoding="utf8") as sutom:
            data = [x.split(",") for x in sutom.read().split("\n")]

        players = {}
        playe = {}

        for play in data:
            if play[1].split("#") not in players:
                players[play[1].split("#")] = 0
                playe[play[1].split("#")] = play[1]
            if int(players[play[2]]) - 5 > 0:
                players[play[1].split("#")] += int(players[play[2]]) - 5

        out = "Résultats :\n"

        for player in players:
            out += f"{playe[player]} - {players[player]} points\n"

        message.channel.send(out)

    if message.content.startswith("SUTOM #"):
        meta = message.content.split("\n")[0]
        _, day, score = meta.split(" ")

        with open("/data/sutom.csv", "a", encoding="utf8") as sutom:
            sutom.write(f"\n{day.strip('#')},{message.author},{score.split('/')[1]}")


def main():
    client.run(TOKEN)


if __name__ == "__main__":
    main()
