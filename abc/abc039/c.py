import sys

def main():
    s = input()

    lst = s.split("WW")
    if lst[1] == "BWBWB":
        if lst[0].count("W") == 2:
            print("Do")
        elif lst[0].count("W") == 1:
            print("Re")
        elif lst[0].count("W") == 0:
            print("Mi")
    elif lst[1] == "BWB":
        if lst[0].count("W") == 3:
            print("Fa")
        elif lst[0].count("W") == 2:
            print("So")
        elif lst[0].count("W") == 1:
            print("La")
        elif lst[0].count("W") == 0:
            print("Si")

       

if __name__ == "__main__":
        main()
