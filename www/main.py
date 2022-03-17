import discord

with open(".discord", "r", encoding="utf8") as secret:
    TOKEN = secret.read()

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


def main():
    client.run(TOKEN)


if __name__ == "__main__":
    main()