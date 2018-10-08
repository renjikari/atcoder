import sys

def main():
    sx, sy, tx, ty = map(int,input().split())

    x = tx - sx
    y = ty - sy

    ans = "U" * y + "R"*x + "D"*y + "L"*x + "L" + "U" * (y+1) + "R"*(x+1) + "D"+"R"+ "D"*(y+1) + "L"*(x+1) + "U"
    print(ans)

if __name__ == "__main__":
        main()
