def simple_fuel(mass):
    return mass//3-2

def simple_fuel_sum(text):
    return sum(simple_fuel(int(line)) for line in text)

def thorough_fuel(mass):
    total = 0
    while mass > 0:
        mass = simple_fuel(mass)
        total += max(0, mass)
    return total

def thorough_fuel_sum(text):
    return sum(thorough_fuel(int(line)) for line in text)

if __name__ == "__main__":
    with open('01.in') as f:
        text = f.readlines()

        print(simple_fuel_sum(text))
        print(thorough_fuel_sum(text))
