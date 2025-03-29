import time

def main():

    for i in range(10):
        print(10 - i)
        time.sleep(1)
        if i == 9:
            print("Liftoff!")
   
if __name__ == "__main__":
    main()