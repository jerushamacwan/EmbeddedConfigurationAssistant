# Code for Embedded System Recommendation
def ram_input():
    ram = int(input("Specify minimum RAM requirement in MB as a number\n"))
    return ram
    ram_input()


def price_input():
    price = int(input("Specify budget\n"))
    return price
    price_input()


def speed_input():
    speed = int(input("Specify minimum processor speed\n"))
    return speed
    speed_input()




def rerun():
    prompt = input("Choose again? (y/n)\n")
    if prompt == 'y':
        main()
    elif prompt == 'n':
        quit()

input.append(ram_input())
input.append(price_input())
input.append(speed_input())

def main():
    choices = {
        "RaspPI Pico":[0.264, 5, 133],
        "Jetson Nano":[4096, 400, 1480],
        "NodeMCU":[0.064, 12, 80],
        "RaspPI Model 1 A+":[512, 30, 700],
        "Asus Tinker":[2048, 125, 2600],
        "Onion Omega2+":[0.138, 25, 580],
        "Arduino":[0.02, 27, 16],
        "Rock Pi":[1024, 80, 1952]
    }


    inputs = []

    output = []

    for key in choices.keys():
        print(key)

for key, value in choices.items():
    if (inputs[0] <= output[0]) and (inputs[1] <= output[1]) and (input[2] <= output[2] ):
        output.append(key)
    if not output:
        print("No configuration found")
        rerun()
        print("Appropraite Configurations according to your specifications")
        print(output)

if __name__== '__main__':
    main()







