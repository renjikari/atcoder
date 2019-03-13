import hashlib
import time

def speed_test(n):
     start = time.time()
     password = "test"
     for i in range(n):
         pass_hash = hashlib.sha256(password.encode()).hexdigest()

     elapsed_time = time.time() - start
     return elapsed_time



print(speed_test(100))


