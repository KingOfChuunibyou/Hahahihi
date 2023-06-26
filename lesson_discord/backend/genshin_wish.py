import random


BANNER_TXT_FILE = "data/banner.txt"
STANDARD_TXT_FILE = "data/standard.txt"


def init_preparation(
    banner_txt_file, standard_txt_file
) -> tuple[dict[str, dict[str, list[str]]], dict[str, list[str]]]:
    """
    Do your preparation here!

    Parameters
    ----------
    banner_txt_file : str
        The path to the banner text file.

    standard_txt_file : str
        The path to the standard text file.

    Returns
    -------
    tuple[dict[str, dict[str, list[str]]], dict[str, list[str]]]
        First tuple contains a dictionary containing the banner and standard characters.
        Keys are:
        - 'version name': the version name
           the value is a dictionary with keys:
            - 'B5': a list of strings containing the 5* banner characters
            - 'B4': a list of strings containing the 4* banner characters

        Second tuple contains dictionary containing the standard characters.
        Keys are:
        - 'B5': a list of strings containing the 5* standard characters
        - 'B4': a list of strings containing the 4* standard characters
        - 'B3': a list of strings containing '3-star weapon'
    """
    banner = {}

    with open(banner_txt_file, "r") as f:
        lines = f.readlines()
        versions = lines[0::4]
        b5s = lines[1::4]
        b4s = lines[2::4]

    b5standard = []

    # baca file standard.txt
    with open(standard_txt_file, "r") as p:
        for line in p:
            b5standard.append(line.strip())

    standard = {"B5": b5standard, "B4": []}

    for version, b5, b4 in zip(versions, b5s, b4s):
        # Case if there are two or MORE FIVE STARS (e.g.: Itto Alhaitham)
        b5_splitted = b5.strip().split()
        if len(b5_splitted) > 1:
            # The first one will be in "{version}-{1}". e.g.: 3.0-1-1
            # The second one will be in "{version}-{2}". e.g.: 3.0-1-2, and so
            # on
            for i in range(len(b5.strip().split())):
                banner[f"{version.strip()}-{i+1}"] = {
                    "B5": [b5_splitted[i]],
                    "B4": b4.strip().split(),
                }
        else:
            # Kodingan kamu archel :D
            banner[version.strip()] = {}
            banner[version.strip()]["B5"] = b5_splitted
            banner[version.strip()]["B4"] = b4.strip().split()

        # list: [a,b,c] -> list.extend([d,e,f]) -> [a,b,c,d,e,f] # 6 elemen
        # list: [a,b,c] -> list.append([d,e,f]) -> [a,b,c,[d,e,f]] # 4 elemen
        standard["B4"].extend(b4.strip().split())

    # MAKE B4 standard unique
    standard["B4"] = list(set(standard["B4"]))
    return banner, standard


class WishState:
    def __init__(self) -> None:
        self.five_stars_event_chars: list[str] = None
        self.four_stars_event_chars: list[str] = None
        self.five_stars_standard_chars: list[str] = None
        self.four_stars_standard_chars: list[str] = None
        self.three_star_weapon_string = "3-star weapon"
        self.num_primogem = 25_600

        # ADD ANY OTHER PROPERTIES THAT YOU NEED HERE. E.G: PITY COUNTER, CHARS OBTAINED, ETC.
        self.five_star_pity = 0
        self.four_star_pity = 0
        self.guaranteed_five_star_event = False
        self.guaranteed_four_star_event = False
        self.obtained_chars = []

    def reset(self):
        self.__init__()

    def show_next_probability(self) -> dict[str, float]:
        """
        Calculate the probability of the next wish.
        It will output a dictionary with keys:
        - 'B5': the probability of getting a 5* character
        - 'B4': the probability of getting a 4* character
        """
        # TODO: YOUR CODE HERE. CALCULATE THE PROBABILITY OF THE NEXT WISH
        # HINT: Make sure to check the pity counter for both five stars and four stars.

        # UPDATE THE RETURN! NTAR KUAPUS
        # print("5* event", self.five_stars_event_chars)
        # print("4* event", self.four_stars_event_chars)
        # print("5* std", self.five_stars_standard_chars)
        # print("4* std", self.four_stars_standard_chars)
        # print(self.three_star_weapon_string)

        five_star_probability = 0.006
        four_star_probability = 0.051

        # five stars calculation
        if self.five_star_pity == 90:
            five_star_probability = 1
        elif self.five_star_pity >= 74:
            # 0.6 + 6% * (pity - 73)
            five_star_probability = five_star_probability + 0.06 * (
                self.five_star_pity - 73
            )

        if self.four_star_pity == 10:
            four_star_probability = 1

        elif self.four_star_pity == 9:
            four_star_probability = 56.1 / 100

        return {
            "B5": five_star_probability,
            "B4": four_star_probability,
        }

    def wish_1_time(self) -> dict[str, str]:
        """
        Wish one time.
        """
        if self.num_primogem < 160:
            raise ValueError("Not enough primogem.")
        self.num_primogem -= 160
        # TODO: YOUR CODE HERE. WISH ONE TIME
        # HINT: Use the show_next_probability() function to determine the
        # probability of the next wish.
        # DO NOT FORGET TO UPDATE THE PITY COUNTER AND THE CHARS OBTAINED.
        self.five_star_pity += 1
        self.four_star_pity += 1

        probability: dict[str, float] = self.show_next_probability()
        # contoh {"B5": 0.006, "B4": 0.051}
        # cek bintang 5 duluan (masuk ke gachanya) -> 50 / 50 standard / event -> klo standard pasti event
        # cek bintang 4 abis itu (masuk ga ke gachanya) -> 50 / 50 standard / event -> klo standard pasti event
        # bintang 3

        # random.random()
        # BINTANG 5 YAH
        if probability["B5"] >= random.random():
            self.five_star_pity = 0
            if self.guaranteed_five_star_event or random.random() <= 0.5:
                self.guaranteed_five_star_event = False
                obtained = {"rarity": "B5", "name": self.five_stars_event_chars[0]}
                self.obtained_chars.append(obtained)
                return obtained
            else:
                self.guaranteed_five_star_event = True
                obtained = {
                    "rarity": "B5",
                    "name": random.choice(self.five_stars_standard_chars),
                }
                self.obtained_chars.append(obtained)
                return obtained

        # BINTANG 4 YAH
        if probability["B4"] >= random.random():
            self.four_star_pity = 0
            if self.guaranteed_four_star_event or random.random() <= 0.5:
                self.guaranteed_four_star_event = False
                obtained = {
                    "rarity": "B4",
                    "name": random.choice(self.four_stars_event_chars),
                }
                self.obtained_chars.append(obtained)
                return obtained
            else:
                self.guaranteed_four_star_event = True
                obtained = {
                    "rarity": "B4",
                    "name": random.choice(self.four_stars_standard_chars),
                }
                self.obtained_chars.append(obtained)
                return obtained

        # BINTANG 3 YAH
        obtained = {"rarity": "B3", "name": self.three_star_weapon_string}
        self.obtained_chars.append(obtained)
        return obtained

    def wish_10_times(self) -> list[dict[str, str]]:
        """
        Wish ten times.
        """
        # TODO: YOUR CODE HERE. WISH TEN TIMES
        # HINT: Use the wish_1_time() function to wish one time. Do it 10 times.
        if self.num_primogem < 1600:
            raise ValueError("Not enough primogem.")
        obtained_chars = []
        for _ in range(10):
            obtained_chars.append(self.wish_1_time())
        return obtained_chars

    def show_pity_counter(self) -> dict[str, int]:
        """
        Show the pity counter for both five stars and four stars.
        """
        return {
            "B5": self.five_star_pity,
            "B4": self.four_star_pity,
        }

    def show_obtained(self) -> dict[str, dict[str, int]]:
        """
        Show the characters obtained.

        The output will be a dictionary with keys:
        - 'B5': a dictionary containing the 5* characters obtained.
            The keys are the character names, and the values are the number of times obtained.
        - 'B4': a dictionary containing the 4* characters obtained.
            The keys are the character names, and the values are the number of times obtained.
        """
        # TODO: YOUR CODE HERE. SHOW THE CHARACTERS OBTAINED
        # UPDATE THE RETURN!
        obtained_chars = {}
        for char in self.obtained_chars:
            obtained_chars.setdefault(char["rarity"], {})
            obtained_chars[char["rarity"]].setdefault(char["name"], 0)
            obtained_chars[char["rarity"]][char["name"]] += 1

        return obtained_chars

    # TODO: OPTIONAL if you want to add more methods
    # HINT: You can add more methods if you want to.

    def set_characters(
        self,
        five_stars_event_chars,
        five_stars_standard_chars,
        four_stars_event_chars,
        four_stars_standard_chars,
    ):
        self.five_stars_event_chars = five_stars_event_chars
        self.four_stars_event_chars = four_stars_event_chars
        self.four_stars_standard_chars = four_stars_standard_chars
        self.five_stars_standard_chars = five_stars_standard_chars


def main():
    # Initialization
    event_banners, standard_banners = init_preparation(
        BANNER_TXT_FILE, STANDARD_TXT_FILE
    )

    # Flag to see whether the user in the wishing simulator or not
    in_wish_simulator = False
    wish_state = WishState()

    # User Loop input
    inside_commands = [
        "wish1",
        "wish10",
        "show pity counter",
        "show next probability",
        "show obtained",
    ]

    # Python 3.8+ only
    while (user_input := input("Your command: ")) != "quit":
        # Command to enter the wishing simulator
        splitted_input = user_input.split()

        # enter command
        if splitted_input[0] == "enter" and len(splitted_input) == 2:
            user_version_input = splitted_input[1]
            if in_wish_simulator:
                print("You are already in the wishing simulator.")
            elif user_version_input in event_banners:
                in_wish_simulator = True
                wish_state.set_characters(
                    event_banners[user_version_input]["B5"],
                    standard_banners["B5"],
                    event_banners[user_version_input]["B4"],
                    standard_banners["B4"],
                )
                print(f"You have entered version {user_version_input} banner.")
                print(f"Featured 5* chars: {wish_state.five_stars_event_chars[0]}")
                print(
                    f"Featured 4* chars: {' '.join(wish_state.four_stars_event_chars)}"
                )
            else:
                print("VERSION DOES NOT EXIST")
        elif user_input in inside_commands:
            if not in_wish_simulator:
                print("YOU NEED TO ENTER THE WISHING SIMULATION")
            else:
                if user_input == inside_commands[0]:  # wish1
                    try:
                        dict_char = wish_state.wish_1_time()
                        print("You CHOOSE to WISH ONCE")
                        print(f"Obtained: {dict_char['rarity']} - {dict_char['name']}")
                        print(f"Primogem left: {wish_state.num_primogem}")
                    except ValueError:
                        print(
                            f"You don't have enough primogems. Your primogem is {wish_state.num_primogem}"
                        )
                elif user_input == inside_commands[1]:  # wish10
                    try:
                        list_char = wish_state.wish_10_times()
                        print("You CHOOSE to WISH 10x")
                        # Create a dictionary of obtained characters (contains nested dict)
                        # first dict, key = rarity, value = dict
                        # second dict, key = name, value = number of times obtained
                        obtained_gacha = {}
                        for char in list_char:
                            obtained_gacha.setdefault(char["rarity"], {})
                            obtained_gacha[char["rarity"]].setdefault(char["name"], 0)
                            obtained_gacha[char["rarity"]][char["name"]] += 1
                        # Print the obtained characters
                        print("3*")
                        stars = [("B3", "3*"), ("B4", "4*"), ("B5", "5*")]
                        for star, printed_star in stars:
                            print(printed_star)
                            if star in obtained_gacha:
                                for name, count in obtained_gacha[star].items():
                                    print(f"- {name}: {count}")
                            else:
                                print("- None")
                        print(f"Primogem left: {wish_state.num_primogem}")
                    except ValueError:
                        print(
                            f"You don't have enough primogems. Your primogem is {wish_state.num_primogem}"
                        )
                elif user_input == inside_commands[2]:  # show pity counter
                    # e.g.:
                    # PITY COUNTER 5*: 68
                    # PITY COUNTER 4*: 12
                    pity_counter = wish_state.show_pity_counter()
                    print(f"PITY COUNTER 5*: {pity_counter['B5']}")
                    print(f"PITY COUNTER 4*: {pity_counter['B4']}")
                elif user_input == inside_commands[3]:  # show next probability
                    next_probability = wish_state.show_next_probability()
                    print(f"NEXT 5* CHANCE: {next_probability['B5']}")
                    print(f"NEXT 4* CHANCE: {next_probability['B4']}")
                elif user_input == inside_commands[4]:  # show obtained
                    obtained = wish_state.show_obtained()
                    print("Obtained Characters / Weapons")
                    stars = [("B3", "3*"), ("B4", "4*"), ("B5", "5*")]
                    for star, printed_star in stars:
                        print(printed_star)
                        if star in obtained:
                            for name, count in obtained[star].items():
                                print(f"- {name}: {count}")
                        else:
                            print("- None")
        else:
            print("WRONG COMMAND.")


if __name__ == "__main__":
    main()
