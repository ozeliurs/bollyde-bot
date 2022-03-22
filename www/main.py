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

    if message.content.startswith("SUTOM #"):
        meta = message.content.split("\n")[0]
        _, day, score = meta.split(" ")

        with open("/data/sutom.csv", "a", encoding="utf8") as sutom:
            sutom.write(f"\n{day.strip('#')}, {message.author}, {score.split('/')}")


def main():
    client.run(TOKEN)


if __name__ == "__main__":
    main()
