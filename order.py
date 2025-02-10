MENU = {"soda", "fries", "burger", "shake", "cookie", "chicken strips"}


def get_order():
    current_order = []
    while True:
        print("What can I get for you?")
        order = input()
        if order in MENU:
            current_order.append(order)
        else:
            print("I'm sorry, we don't serve that.")


def main():
    order = get_order()


if __name__ == "__main__":
    main()
