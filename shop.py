# Developed By: Yosra Alim
# Date: March 1th
# Description: My PC Shop!

print('Welcome To My PC Shop!', 'Let\'s build your dream PC')

print('-----------------------------------------------------------------------------')


# this used to calculate the price. this was provided in the assignment 2 instructions.
SSD = [['1', '250 GB', 69.99], ['2', '500 GB', 93.99], ['3', '4 TB', 219.99]]
HDD = [['1', '500 GB', 106.33], ['2', '1 TB', 134.33]]
CPU = [['1', 'Intel Core i7-11700K', 499.99], ['2', 'AMD Ryzen 7 5800X', 312.99]]
MOTHERBOARD = [['1', 'MSI B550-A PRO', 197.46], ['2', 'MSI Z490-A PRO', 262.30]]
RAM = [['1', '16 GB', 82.99], ['2', '32 GB', 174.99]]
GRAPHICS_CARD = [['1', 'MSI GeForce RTX 3060 12GB', 539.99]]
PSU = [['1', 'Corsair RM750', 164.99]]
CASE = [['1', 'Full Tower (black)', 149.99], ['2', 'Full Tower (red)', 149.99]]
PREBUILTS = [['1', 'Legion Tower Gen 7 with RTX 3080 Ti', 3699.99], ['2', 'SkyTech Prism II Gaming PC', 2839.99],
             ['3', 'ASUS ROG Strix G10CE Gaming PC', 1099.99]]


# this is used the total price for a custom build.
def calculate_total(cpu, motherboard, ram, psu, case, ssd, hdd, graphics_card):
    total = 0

    total += CPU[cpu][2]
    total += MOTHERBOARD[motherboard][2]
    total += RAM[ram][2]
    total += PSU[psu][2]
    total += CASE[case][2]
    if ssd.isnumeric():
        total += SSD[int(ssd) - 1][2]
    if hdd.isnumeric():
        total += HDD[int(hdd) - 1][2]
    if graphics_card.isnumeric():
        total += GRAPHICS_CARD[int(graphics_card) - 1][2]

    return total


def check_cpu_motherboard(cpu, motherboard):
    if cpu == '1' and motherboard == '2':
        return False
    elif cpu == '2' and motherboard == '1':
        return False
    else:
        return True


def pickItems():
    orders = []   # this will be returned from our function.
    order_number = 1   # this will keep track of the number of user order.
    while True:   # this will loop forever until the user selects option '3' for checkout.
        print("Welcome to our online PC shop!")
        print("Do you want to create/build your PC? Select option 1. Do you want a pre-built PC? "
              "Select option 2. Do you want to checkout? Select option 3. Please select from the following options:")
        print("1. Custom Build")
        print("2. Pre-built Machines")
        print("3. Checkout")
        choice = input("Your choice: ")
        if choice == '1':

            print("\n")

            print("You have selected Custom Build.")
            print("First, let's pick a CPU.")
            print("Please select a CPU from the following options:")
            print("1. Intel Core i7-11700K, $499.99")
            print("2. AMD Ryzen 7 5800X, $312.99")
            cpu_choice = input("Your choice: ")
            while cpu_choice not in ['1', '2']:
                print("Invalid CPU choice.")
                cpu_choice = input("Please select a CPU (1 for Intel Core i7-11700K or 2 for AMD Ryzen 7 5800X): ")

            print("\n")

            print("Next, let's pick a Motherboard.")
            print("Please select a Motherboard from the following options:")
            print("1. MSI B550-A PRO, $197.46")
            print("2. MSI Z490-A PRO, $262.30   ")
            motherboard_choice = input("Your choice: ")
            while motherboard_choice not in ['1', '2']:
                print("Invalid motherboard choice.")
                motherboard_choice = input(
                    "Please select a motherboard (1 for MSI B550-A PRO or 2 for MSI Z490-A PRO): ")

            print("\n")

            while not check_cpu_motherboard(cpu_choice, motherboard_choice):
                print("This CPU and motherboard combination is not compatible.")

                print("\n")

                cpu_choice = input("Please select a CPU (1 for Intel Core i7-11700K or 2 for AMD Ryzen 7 5800X): ")
                while cpu_choice not in ['1', '2']:
                    print("Invalid CPU choice.")
                    cpu_choice = input("Please select a CPU (1 for Intel Core i7-11700K or 2 for AMD Ryzen 7 5800X): ")

                motherboard_choice = input(
                    "Please select a motherboard (1 for MSI B550-A PRO or 2 for MSI Z490-A PRO): ")
                while motherboard_choice not in ['1', '2']:
                    print("Invalid motherboard choice.")
                    motherboard_choice = input(
                        "Please select a motherboard (1 for MSI B550-A PRO or 2 for MSI Z490-A PRO): ")

                print("\n")

            print("Next, let's pick a RAM.")
            print("Please select a RAM from the following options:")
            print("1. 16 GB, $82.99")
            print("2. 32 GB, $174.99")
            ram_choice = input("Your choice: ")
            while ram_choice not in ['1', '2']:
                print("Invalid RAM choice.")
                ram_choice = input("Your choice: ")

            print("\n")

            print("Next, let's pick a PSU.")
            print("Please select a PSU from the following options:")
            print("1. Corsair RM750, $164.99")
            psu_choice = input("Your choice: ")
            while psu_choice not in ['1']:
                print("Invalid PSU choice.")
                psu_choice = input("Your choice: ")

            print("\n")

            print("Next, let's pick a Case.")
            print("Please select a Case from the following options:")
            print("1. Full Tower (black), $149.99")
            print("2. Full Tower (red), $149.99")
            case_choice = input("Your choice: ")
            while case_choice not in ['1', '2']:
                print("Invalid case choice.")
                case_choice = input("Your choice: ")

            print("\n")

            print("Next, let's pick a SSD. (This is optional but note that you must pick either an SSD or HDD.)")
            print("Please select a SSD from the following options or enter X to not choose an SSD:")
            print("1. 250 GB, $69.99")
            print("2. 500 GB, $93.99")
            print("3. 4 T, $219.99")
            ssd_choice = input("Your choice: ")
            while ssd_choice not in ['1', '2', '3', 'x', 'X']:
                print("Invalid SSD choice.")
                ssd_choice = input("Your choice: ")

            print("\n")

            print("Next, let's pick a HDD. (This is optional but note that you must pick either an SSD or HDD.)")
            print("Please select a HDD from the following options or enter X to not choose an HDD:")
            print("1. 500 GB, $106.33")
            print("2. 1 TB, $134.33")
            hdd_choice = input("Your choice: ")
            while hdd_choice not in ['1', '2', 'x', 'X']:
                print("Invalid HDD choice.")
                hdd_choice = input("Your choice: ")

            print("\n")

            while ssd_choice.isalpha() and hdd_choice.isalpha() \
                    and ssd_choice.lower() == 'x' and hdd_choice.lower() == 'x':
                print("Invalid HDD choice. You must pick an HDD!")
                ssd_choice = input("Your choice: ")

            print("\n")

            print("Next, let's pick a a Graphic Card.")
            print("Please select a Graphic Card from the following options or X to not get a graphics card:")
            print("1. MSI GeForce RTX 3060 12GB, $539.99")
            graphic_card_choice = input("Your choice: ")
            while graphic_card_choice not in ['1', 'x', 'X']:
                print("Invalid graphic card choice.")
                graphic_card_choice = input("Your choice: ")

            orders.append(calculate_total(int(cpu_choice) - 1, int(motherboard_choice) - 1, int(ram_choice) -1,
                                          int(psu_choice) - 1, int(case_choice) - 1, ssd_choice, hdd_choice,
                                          graphic_card_choice))
            print("\nFinished Order Number: " + str(order_number) + "\n")
            order_number += 1
        elif choice == '2':
            print("You have selected Pre-Built Machines.")
            print("Please select a Pre-Built you would like to order from the following options:")
            print("1. Legion Tower Gen 7 with RTX 3080 Ti, $3699.99")
            print("2. SkyTech Prism II Gaming PC, $2839.99")
            print("3. SUS ROG Strix G10CE Gaming PC, $1099.99")
            prebuilt_choice = input("Your choice: ")
            while prebuilt_choice not in ['1', '2', '3']:
                print("Invalid Pre-Built choice.")


            orders.append(PREBUILTS[int(prebuilt_choice) - 1][2])
            print("\nFinished Order Number: " + str(order_number) + "\n")
            order_number += 1
        elif choice == '3':
            print("You have selected to Checkout. Thank you for shopping with us!")
            print(orders)
            break   # this used to break the forever loop after user chooses option '3' for checkout.
        else:
            print("Do you want to create/build your PC? Select option 1. Do you want a pre-built PC? "
                  "Select option 2. Do you want to checkout? Select option 3. Please select from the following options:")
            print("1. Custom Build")
            print("2. Pre-built Machines")
            print("3. Checkout")


pickItems()  # this is used to call the function.
