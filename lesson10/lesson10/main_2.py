import os  # hal yang berkaitan dengan operasi operating system
import time  # untuk delay
import shutil  # untuk copy, move, delete file
import datetime  # untuk mengambil waktu saat ini
import re
import random
import math
import numpy as np  # matika2an
import pandas as pd


def math_mathan():
    print(math.sin(math.radians(30)))
    print(np.array([[1, 2, 3], [4, 5, 6]]))
    print(np.array([1, 2, 3]) + np.array([4, 6, 7]))
    print(np.sin(np.radians([30, 60, 90])))


def random_randoman():
    # random 1 sampe 100
    for i in range(10):
        angka_random = random.randint(1, 100)  # uniform
        print(angka_random)

        # random variable?
    for i in range(10):
        print(random.random())  # 0 - 1

    # random choice
    list_archel = ["archel", "kunyuk", "kucing"]  # 100 / 3 = 33.33%
    for i in range(10):
        print(random.choice(list_archel))  # uniform 0 - 1

    # random randint
    ## 11.5%
    ## 20/100 -> 1/5
    for i in range(10):
        hasil_random = random.random() * 100  # dalam bentuk persen
        if hasil_random < 20:
            print("Kamu Jodoh Smaa X")
        else:
            print("Kamu Ga Jodoh")


def date_datean():
    # get current time
    now = datetime.datetime.now()
    print(now)

    # get only the clock with string format (HH:MM:SS)
    print(now.strftime("%H:%S:%M"))

    # Convert our string to datetime object
    string_archel = "Archel kuliah dimarahin dosen ga ngumpulin tugas Pukul 10:53:22"

    # extract with regex
    # 10:53:22
    time_archel = re.findall(r"\d{2}:\d{2}:\d{2}", string_archel)
    print(time_archel)

    # convert to datetime object
    time_archel = datetime.datetime.strptime(time_archel[0], "%H:%M:%S")
    print(time_archel)

    # get the difference
    waktu_yg_mau_dibadngingin = datetime.datetime.strptime("11:00:00", "%H:%M:%S")
    # 11:00:00 - 10:53:22
    # kita bandingin jam archel dimarahin dosen pertama  dan jam archel dimarahin dosen kedua
    print(waktu_yg_mau_dibadngingin - time_archel)


def os_osan():
    """
    bau2os
    """
    # bikin directory
    os.makedirs("tmp", exist_ok=True)

    # 3 detik bengong

    # delete
    os.rmdir("tmp")

    # copy requirements
    shutil.copy("requirements.txt", "kucing.txt")

    # see file size in MB
    print(os.path.getsize("kucing.txt"), "B")

    # delete file
    os.remove("kucing.txt")


def main():
    math_mathan()


if __name__ == "__main__":
    main()
