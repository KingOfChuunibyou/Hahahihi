# https://pypi.org/project/python-dotenv/
# https://discordpy.readthedocs.io/en/stable/
# https://pypi.org/project/discord.py/
# https://discordpy.readthedocs.io/en/stable/faq.html#how-do-i-send-a-message-to-a-specific-channel
# https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html

import dotenv
import os
from discord import Client, Intents
from discord.ext import commands
from backend.genshin_wish import WishState, init_preparation
import discord

BANNER_TXT_FILE = "data/banner.txt"
STANDARD_TXT_FILE = "data/standard.txt"
in_wish_simulator = False


def main():
    # Initialize Genshin Variables

    event_banners, standard_banners = init_preparation(
        BANNER_TXT_FILE, STANDARD_TXT_FILE
    )
    wish_state = WishState()

    # User Loop input
    inside_commands = [
        "wish1",
        "wish10",
        "show pity counter",
        "show next probability",
        "show obtained",
    ]

    dotenv.load_dotenv()
    print(os.getenv("ARCHEL_BOT"))

    intents = Intents.default()
    intents.message_content = True
    # client = MyClient(intents=intents)
    # client.run(os.getenv("ARCHEL_BOT"))

    bot = commands.Bot(command_prefix="!", intents=intents)

    async def check_inside(ctx):
        global in_wish_simulator
        if not in_wish_simulator:
            await ctx.send("You are not in the wishing simulator.")

    @bot.command(name="reset")
    async def reset(ctx):
        global in_wish_simulator
        in_wish_simulator = False
        wish_state.reset()
        await ctx.send("You have exited the wishing simulator and reset it.")

    @bot.command(name="wish1")
    async def wish1(ctx):
        global in_wish_simulator
        check_inside(ctx)
        try:
            dict_char = wish_state.wish_1_time()
            await ctx.send("You CHOOSE to WISH ONCE")
            await ctx.send(f"Obtained: {dict_char['rarity']} - {dict_char['name']}")
            await ctx.send(f"Primogem left: {wish_state.num_primogem}")
        except ValueError:
            await ctx.send(
                f"You don't have enough primogems. Your primogem is {wish_state.num_primogem}"
            )

    @bot.command(name="show_probability")
    async def show_probability(ctx):
        global in_wish_simulator
        check_inside(ctx)
        next_probability = wish_state.show_next_probability()
        await ctx.send(
            f"NEXT 5* CHANCE: {next_probability['B5']} \n NEXT 4* CHANCE: {next_probability['B4']}"
        )

    @bot.command(name="show_obtained")
    async def show_obtained(ctx):
        global in_wish_simulator
        check_inside(ctx)
        obtained = wish_state.show_obtained()
        string_to_send = ""

        string_to_send += "Obtained Characters / Weapons\n"
        stars = [("B3", "3*"), ("B4", "4*"), ("B5", "5*")]

        for star, printed_star in stars:
            string_to_send += printed_star + "\n"
            if star in obtained:
                for name, count in obtained[star].items():
                    string_to_send += f"- {name}: {count}\n"
            else:
                string_to_send += "- None\n"
        await ctx.send(string_to_send)

    @bot.command(name="show_pity_counter")
    async def show_pity_counter(ctx):
        global in_wish_simulator
        check_inside(ctx)
        pity_counter = wish_state.show_pity_counter()
        await ctx.send(
            f"PITY COUNTER 5*: {pity_counter['B5']} \n PITY COUNTER 4*: {pity_counter['B4']}"
        )

    @bot.command(name="wish10")
    async def wish10(ctx):
        global in_wish_simulator
        check_inside(ctx)
        string_to_send = ""
        try:
            list_char = wish_state.wish_10_times()
            string_to_send += "You CHOOSE to WISH 10x \n"
            # Create a dictionary of obtained characters (contains nested dict)
            # first dict, key = rarity, value = dict
            # second dict, key = name, value = number of times obtained
            obtained_gacha = {}
            for char in list_char:
                obtained_gacha.setdefault(char["rarity"], {})
                obtained_gacha[char["rarity"]].setdefault(char["name"], 0)
                obtained_gacha[char["rarity"]][char["name"]] += 1
            # await ctx.send the obtained characters
            stars = [("B3", "3*"), ("B4", "4*"), ("B5", "5*")]
            for star, printed_star in stars:
                string_to_send += printed_star + "\n"
                if star in obtained_gacha:
                    for name, count in obtained_gacha[star].items():
                        string_to_send += f"- {name}: {count}\n"
                else:
                    string_to_send += "- None\n"
            string_to_send += f"Primogem left: {wish_state.num_primogem}"
        except ValueError:
            string_to_send += f"You don't have enough primogems. Your primogem is {wish_state.num_primogem}\n"

        await ctx.send(string_to_send)

    @bot.command(name="enter")
    async def enter(ctx, version: str):
        global in_wish_simulator
        if in_wish_simulator:
            await ctx.send("You are already in the wishing simulator.")
        elif version in event_banners:
            string_to_send = ""
            in_wish_simulator = True
            wish_state.set_characters(
                event_banners[version]["B5"],
                standard_banners["B5"],
                event_banners[version]["B4"],
                standard_banners["B4"],
            )
            string_to_send += f"You have entered version {version} banner.\n"
            string_to_send += (
                f"Featured 5* chars: **{wish_state.five_stars_event_chars[0]}**\n"
            )
            string_to_send += (
                f"Featured 4* chars: {' '.join(wish_state.four_stars_event_chars)}\n"
            )
            await ctx.send(string_to_send)
        else:
            await ctx.send(f"Version {version} not found.")

    @bot.command(name="test")
    async def test(ctx):
        await ctx.send("Test!")

    @bot.event
    async def on_message(message, pass_context=True):
        if message.author == bot.user:
            return
        await bot.process_commands(message)
        ctx = await bot.get_context(message)
        if ctx.command is None:
            print(f"Message from {message.author}: {message.content}")
            # channel = bot.get_channel(1114459976107303016)
            # send a message to the channel
            await ctx.send(f"Buacot koe {message.author}! Semprul!")
            await ctx.send(file=discord.File("backend/genshin_wish.py"))
            await ctx.send(file=discord.File("frontend/bot_archel.py"))
            # await message.author.send('Berani kamu sama saya!')

    bot.run(os.getenv("ARCHEL_BOT"))


if __name__ == "__main__":
    main()
