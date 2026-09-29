from temperature_lib import is_frost, average_temp, to_faranheit_all, first_frost, frost_only

def getValidInput():
    """ safely gets a list of temperatures from user input, ensuring they are valid """

    while True:
        rawInput = input("enter temperatures separeted by space: ").strip()

        if not rawInput:
            print("no input provided, try again")
            continue

        try:
            temps = [float(x) for x in rawInput.split()]
            return temps
        except ValueError:
            print("invalid input, enter valid temperatures separated by space")
            continue



def main():
    print("temperature analysis program")
    
    temps = getValidInput()

    #call function is_frost
    frostTemps = [t for t in temps if is_frost(t)]
    if len(frostTemps) > 0:
        print(f"frost temperatures: {', '.join([f'{t:.2f} C' for t in frostTemps])}")
    else:
        print("no frost temperatures found")    

    # call function average_temp 
    avg = average_temp(temps)
    if avg is not None:
        print(f"average temperature: {avg:.2f} C")
    else: 
        print("no temperatures provided")

    # call function first_frost
    frostIdx = first_frost(temps)
    if frostIdx != -1:
        print(f"first frost temperature: {temps[frostIdx]:.2f} C at index {frostIdx}")
    else:
        print("no frost temperatures found")

    # call function frost_only
    frostTemps = frost_only(temps)
    if len(frostTemps) > 0:
        print(f"frost temperatures: {', '.join([f'{t:.2f} C' for t in frostTemps])}")
    else:
        print("no frost temperatures found")    

    # call function to_faranheit_all
    print(f"temperatures in Fahrenheit: {', '.join([f'{t:.2f} F' for t in to_faranheit_all(temps)])}")   

if __name__ == "__main__":
    main()     