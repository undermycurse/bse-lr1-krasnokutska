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

def remove_dish(name):
    global menu
    menu = [dish for dish in menu if dish["name"] != name]


remove_dish("кава капучіно")

show_menu()

def generate_qr_link(menu_name):
    return f"https://menuqr.example.com/{menu_name}"


qr_link = generate_qr_link("brewspace")
print("Посилання для QR-коду:", qr_link)