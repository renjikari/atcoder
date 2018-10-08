import sys

def main():
    s = list(input())


    anslst = []
    
    anslst.append(s.count("A"))
    anslst.append(s.count("B"))
    anslst.append(s.count("C"))
    anslst.append(s.count("D"))
    anslst.append(s.count("E"))
    anslst.append(s.count("F"))

    anslst = list(map(str,anslst))

    print(" ".join(anslst))


if __name__ == "__main__":
        main()
