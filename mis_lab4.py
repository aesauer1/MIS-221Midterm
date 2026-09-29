def display_header():
    print("="*30, "     Concert Ticket Pricer", "="*30, sep='\n')


def get_base_price(age):
    if age < 5:
        return 0.0
    elif 5 <= age <= 12:
        return 10.0
    elif 13 <= age <= 17:
        return 15.0
    elif 18 <= age <= 64:
        return 25.0
    else:
        return 18.0


def get_section_surcharge(section):
    match section:
        case "floor":
            return 40.0
        case "lower":
            return 20.0
        case "upper":
            return 5.0
        case "lawn":
            return 0.0
        case _:
            return 0.0


def is_discount_eligible(is_member, age):
    return (is_member and age >= 18) or (age < 13)
    # if is_eligible_for_discount(age, is_member):


def calculate_total(base_price, surcharge, discount_eligible, age):
    if discount_eligible:
        if age >= 65:
            discount_rate = 0.20
        else:
            discount_rate = 0.15
    else:
        discount_rate = 0.0

    discount_amount = base_price * discount_rate
    total = base_price - discount_amount + surcharge
    return total


def display_receipt(age, section, base_price, surcharge, eligible, is_member, total):
    print(f"Base price: ${base_price}")
    if eligible:
        discount_rate = 0.20 if age >= 65 else 0.15
        discount_amount = base_price*discount_rate
        print(
            f"Discount ({int(discount_rate*100)}%): - ${discount_amount:.2f}")
    print(f"Section surcharge: ${surcharge:.2f}")
    print("                  -------")
    print(f"Total: ${total:.2f}")
    if is_member:
        print("Member discount applied.")

# main


# display_header
display_header()

# inputs
age = int(input("Enter customer age: "))
section = input("Enter section (floor/lower/upper/lawn): ")
member_input = input("Is the customer a member? (yes/no: )")
is_member = member_input == "yes"

# calculate
base_price = get_base_price(age)
surcharge = get_section_surcharge(section)
eligible = is_discount_eligible(is_member, age)
total = calculate_total(base_price, surcharge, eligible, age)

# display
display_receipt(age, section, base_price, surcharge,
                eligible, is_member, total)
