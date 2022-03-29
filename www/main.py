import discord
import time
from collections import Counter

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

    prefix = "!"

    messages = {
        "evite": "https://media.discordapp.net/attachments/856154341106647090/953608358127091732/unknown.png",
        "nekfeu": "https://cdn.discordapp.com/attachments/953590491637768202/956903404259672084/ErmxaTxXYAEqmXo.png",
        "noodle": "https://www.youtube.com/watch?v=iOQz2r6ZtR4",
        "espuma": "<@!692684431370223647> https://youtu.be/k3xxquu-pmQ",
        "bonsens": "https://cdn.discordapp.com/attachments/755446976631406725/958326468956520508/videoplayback.mp4",
        "prob": "https://cdn.discordapp.com/attachments/755446976631406725/958326585847586836/st.cowJup56qXJR.mp4",
        "cringe": "https://giphy.com/gifs/the-office-smile-9oF7EAvaFUOEU",
        "incomodo": "https://cdn.discordapp.com/attachments/755446976631406725/957972945819541554/Pardon_je_sais_qui_Leto..._-_Morbius.mp4"
    }

    if message.content.strip(prefix).strip() in messages:
        await message.channel.send(messages[message.content.strip(prefix).strip()])
        await message.delete()

    if message.content.startswith("!ghostping"):
        with open("/data/ghostping", "a", encoding="utf8") as log:
            log.write(f"{message.author}\n")
        await message.delete()

    if message.content.startswith("!ghosted"):
        with open("/data/ghostping", "r", encoding="utf8") as log:
            contents = log.read().split("\n")[:-1]
        count = Counter(contents)

        out = "Ghostping Users:\n"

        for ind in count:
            out += str(ind) + ": " + str(count[ind]) + "\n"

        await message.delete()
        await message.channel.send(out)


def main():
    client.run(TOKEN)


if __name__ == "__main__":
    main()
