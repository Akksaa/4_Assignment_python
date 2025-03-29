import time

def countdown(t):
    while t:
        mins, secs = divmod(t,60)
        timer = '{:02d}:{:02}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Timer Completed!")


def main():
    t = int(input("Enter time in Seconds: "))
    countdown(t)

if __name__ == "__main__":
    main()
