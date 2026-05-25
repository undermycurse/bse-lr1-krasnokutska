menu = []

def add_dish(name, price):
    menu.append({
        "name": name,
        "price": price
    })

def show_menu():
    print("Меню кавʼярні Brewspace:")

    for dish in menu:
        print(f"{dish['name']} - {dish['price']} грн")


add_dish("кава капучіно", 120)
add_dish("кава еспресо", 80)

show_menu()