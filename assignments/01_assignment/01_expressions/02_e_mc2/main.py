def main():
    speed_of_light : float = 299792458
    mass_in_kilos : float = float(input("Enter mass in Kilogram:"))

    print('E = m*c^2...')
    print(f"m = {mass_in_kilos} kg")
    print(f"c = {speed_of_light} m/s")

    energy_in_joules = mass_in_kilos * (speed_of_light ** 2)
    print(str(energy_in_joules) + " joules of energy!")

if __name__ == "__main__":
    main()
