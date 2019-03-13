import time

def speed_test(n):
    start = time.time()
    tmp = 0
    for i in range(n):
        tmp += 1

    elapsed_time = time.time() - start
    return elapsed_time 


def main():
    print ("10の5乗   :{0}".format(speed_test(100000)) + "[sec]")

    print ("10の6乗   :{0}".format(speed_test(1000000)) + "[sec]")

    print ("10の7乗   :{0}".format(speed_test(10000000)) + "[sec]")

    print ("2*10の7乗 :{0}".format(speed_test(20000000)) + "[sec]")
    print ("10の8乗   :{0}".format(speed_test(100000000)) + "[sec]")

if __name__ == "__main__":
        main()

