import argparse
import random
import time
from rich.console import Console
from rich.progress import Progress, track


# -m itu opsinya biasanya pendek
# --mode itu opsinya biasanya panjang
def main():
    console = Console()
    parser = argparse.ArgumentParser(
        description="Ini adalah program untuk menentukan jodoh"
    )
    parser.add_argument(
        "--pasangan1", type=str, help="Nama pasangan pertama", required=True
    )
    parser.add_argument(
        "--pasangan2", type=str, help="Nama pasangan kedua", required=True
    )

    args = parser.parse_args()
    pasangan1 = args.pasangan1.capitalize()
    pasangan2 = args.pasangan2.capitalize()

    print(f"Nama pasangan pertama: {pasangan1} dan nama pasangan kedua: {pasangan2}")
    print(f"Tunggu bentar...")

    for i in track(range(3), description="Kalkulasi Seberapa cocok......"):
        time.sleep(1)  # Simulate work being done

    hasil_random = random.randint(0, 100)
    print("HASIL SUDAH KELUAR!!!")

    if hasil_random < 20: # BE
        console.print(f"Kamu [bold][green]Jodoh[/green][/bold] dengan {pasangan1} {pasangan2}") #FE
        console.print(f"Selamat, langsung kawin aja")
    else:
        console.print(f"Kamu [bold][red]GA JODOH[/red][/bold] sama {pasangan1} {pasangan2}")
        console.print("PUTUS SKRNG JUGA!!!")


if __name__ == "__main__":
    main()
