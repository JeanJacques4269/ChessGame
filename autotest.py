import time

import Logic
import bot
from constants import *


def mate_test(fenmates: list, name):
    c = 0
    for i, fen in enumerate(fenmates):
        a = fen.split(" ")
        color = "white" if a[1] == "w" else "black"
        bott = bot.Edouard(color)
        virtual = Logic.Logic(fen=fen)

        print(f"Testing fenmate[{i}]...", end="")

        start = time.time()
        eval, move = bott.play_well(virtual, 2)
        end = time.time()
        if abs(eval) < 500:
            print(f"Mat non trouvé pour fenmate2[{i}], {eval=}")
            c += 1
        else:
            print(f"Mat trouvé en {end - start:.2f} s")

    print(f"Tests de mat terminés pour {name}, {c} tests ont échoués sur {len(fenmates)}")


def main():
    mate_test(fenmate2, "fenmate2")
    mate_test(fenmate3, "fenmate3")


if __name__ == "__main__":
    main()
