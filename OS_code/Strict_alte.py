import threading
import time

# shared variable
turn = 0  # 0 -> P0's turn, 1 -> P1's turn

# number of times each process will try to enter critical section
ITERATIONS = 5


def process_0():
    global turn
    for i in range(ITERATIONS):
        # wait until it's P0's turn
        while turn != 0:
            pass

        # critical Section
        print("P0 is in critical section")
        time.sleep(1)

        # Exit section
        turn = 1  # Give turn to P1


def process_1():
    global turn
    for i in range(ITERATIONS):
        # Wait until it's P1's turn
        while turn != 1:
            pass

        # critical Section
        print("P1 is in critical section")
        time.sleep(1)

        # exit section
        turn = 0  # Give turn to P0


t1 = threading.Thread(target=process_0)
t2 = threading.Thread(target=process_1)

t1.start()
t2.start()

t1.join()
t2.join()

print("finishing....")