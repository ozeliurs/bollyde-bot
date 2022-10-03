import json
import random

import discord
from collections import Counter

from pathlib import Path

with open(f"{__file__.split('/main.py')[0]}/.discord", "r", encoding="utf8") as secret:
    TOKEN = secret.read()

client = discord.Client(intents=discord.Intents.all())


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
        "proba": "https://cdn.discordapp.com/attachments/755446976631406725/958326585847586836/st.cowJup56qXJR.mp4",
        "cringe": "https://giphy.com/gifs/the-office-smile-9oF7EAvaFUOEU",
        "incomodo": "https://cdn.discordapp.com/attachments/755446976631406725/957972945819541554/Pardon_je_sais_qui_Leto..._-_Morbius.mp4",
        "feur": "https://cdn.discordapp.com/attachments/759864445760962601/959070908553785364/unknown.png",
        "culot": "https://cdn.discordapp.com/attachments/768477390283210812/959111419578708008/unknown.png", 
        "debout": "https://www.youtube.com/shorts/WRzkMKbMYgk",
        "spooktober": "https://i.ytimg.com/vi/jG7yLhdCM64/maxresdefault.jpg"
    }

    comm = message.content.strip().split(" ")[0]

    if comm in [prefix+m for m in messages]:
        await message.channel.send(messages[comm.strip("!")])
        await message.delete()

    if str(message.author) == "antøskins#8106":
        if random.randint(0, 100) <= 5:
            msgs = [
                "https://youtu.be/zHUylGEOhNg",
                "https://youtu.be/U0Rizfz_4uM",
                "https://youtu.be/yuSReKk0-co",
                "https://youtu.be/VzeOnBRzDik"
            ]
            await message.channel.send(random.choice(msgs))
    
    if str(message.author) == "Hovercraft#9079":
        if random.randint(0, 100) <= 5:
            await message.channel.send("https://www.youtube.com/watch?v=xmwGkwO6lOg&")

    if str(message.author) == "Musaraigne anonyme#1908":
        if random.randint(0, 100) <= 0:
            await message.channel.send("La GAUUUUUUUUUUUUUUUUUUUCHE")

    if message.content.startswith(f"{prefix}shifoumi"):
        if len( message.content.strip().split(" ") ) != 3:
            await message.channel.send(prefix+"shifoumi <J1> <J2>")
            return
        else:
            els = ["pierre", "papier", "ciseaux"]
            p1 = message.content.strip().split(" ")[1]
            j1 = random.choice(els)
            p2 = message.content.strip().split(" ")[2]
            j2 = random.choice(els)

            await message.channel.send(f"{p1}: {j1} - {j2} :{p2}")

            if j1 == j2:
                winner = "égalité"
            elif (j1 == "pierre" and j2 == "ciseaux") or (j1 == "ciseaux" and j2 == "feuille") or (j1 == "feuille" and j2 == "pierre"):
                winner = f"{p1} à gagné"
            else:
                winner = f"{p2} à gagné"

            await message.channel.send(f"Résultat: {winner}")

    if message.content.startswith(f"{prefix}ghostping"):
        with open("/data/ghostping", "a", encoding="utf8") as log:
            log.write(f"{message.author}\n")
        await message.delete()

    if message.content.startswith(f"{prefix}ghosted"):
        if str(message.author) in [".Happy.#8314", "Kioko#2772"]:
            await message.channel.send("Petit curieux va ...")
            return

        with open("/data/ghostping", "r", encoding="utf8") as log:
            contents = log.read().split("\n")[:-1]
        count = Counter(contents)

        out = "Ghostping Users:\n"

        for ind in count:
            out += str(ind) + ": " + str(count[ind]) + "\n"

        await message.delete()
        await message.channel.send(out)

    if message.content.startswith(f"{prefix}help"):
        help = "".join([f" - {prefix}{x} -> Image meme." + "\n" for x, y in messages.items()])

        help += f" - {prefix}shifoumi <a> <b> -> détermine le vainqueur entre a et b. (maintenant sans bug !!)\n"
        help += f" - {prefix}ghostping <a> -> supprimme immédiatement le message d'origine. (attention vous êtes enregistrés !)\n"
        help += f" - {prefix}ghosted -> Liste les utilisateurs de ghostping.\n"
        help += f" - {prefix}music theme <theme> -> Choisir le theme pour le perdant du cycle précédent.\n"
        help += f" - {prefix}music vote <score> <vote> -> Voter pour une musique.\n"
        help += f" - {prefix}music end -> Arreter la session, afficher les résultats et choisir le perdant pour le prochain theme.\n"

        await message.channel.send(help)

    if message.content.startswith(f"{prefix}music vote"):
        config = json.loads(Path("/data/music.json").read_text())

        score, vote = message.content.split(f"{prefix}music vote")[1].split(" ")[0:2]
        config["player"][message.author][vote] = score

        Path("/data/music.json").write_text(json.dumps(config, indent=4))
        await message.channel.send(f"{score} attribués à {vote}.")

    if message.content.startswith(f"{prefix}music end"):
        results = {}
        cfile = Path("/data/music.json")

        if not cfile.exists():
            config = {"theme": None, "players":{}}
        else:
            config = json.loads(cfile.read_text())

        for player in config["players"]:
            for target, score in player.items():
                if target in results:
                    results[target] += int(score)
                else:
                    results[target] = int(score)

        mini = 1000000000
        loser = None

        msg = f"Voisi les scores pour le thème: {config['theme']}\n"

        for player, score in results.items():
            msg += f" - {player}: {score}\n"

            if score < mini:
                mini = score
                loser = player

        msg += f"\nA {loser} de choisir le thème. ({prefix}help pour l'aide)"

        config = {"loser": loser}

        await message.channel.send(str(msg))

        cfile.write_text(json.dumps(config, indent=4))

    if message.content.startswith(f"{prefix}music debug"):
        await message.channel.send(Path("/data/music.json").read_text())

    if message.content.startswith(f"{prefix}music theme"):
        config = json.loads(Path("/data/music.json").read_text())

        if config["loser"] != message.author:
            await message.channel.send("Vous n'etes pas le perdant du round précédent.")

        if config["theme"] is None:
            msg = "Le nouveau theme est la @everyone: "
        else:
            msg = "Le thème à changé @everyone: "

        theme = message.content.split(f"{prefix}music theme")[1]
        config["theme"] = theme
        msg += theme

        Path("/data/music.json").write_text(json.dumps(config, indent=4))

        await message.channel.send(msg)


def main():
    client.run(TOKEN)


if __name__ == "__main__":
    main()
