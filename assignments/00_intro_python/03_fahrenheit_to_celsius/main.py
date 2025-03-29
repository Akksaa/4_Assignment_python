def main():
    print("\nHello from 03-fahrenheit-to-celsius!")

    user_input : str = input("\nEnter the temperature in Fahrenheit:")
    f_temp : float = float(user_input)
    c_temp : float = (f_temp - 32) / 1.8
    result = f"Temperature: {f_temp}F is equal to {c_temp}C!"
    print(result)
    

if __name__ == "__main__":
    main()
