import sys


class InventoryError(Exception):
    """This class serves for custom error messages"""
    pass


def inventory_analytics(inventoria: dict, categories: dict) -> None:
    """This function processes the inventory items and amounts"""

    most_item = None
    least_item = None

    for item, quantity in inventoria.items():
        if most_item is None or quantity > inventoria.get(most_item):
            most_item = item

        if least_item is None or quantity < inventoria.get(least_item):
            least_item = item

    total_items = 0
    t_items = 0
    for quantity in inventoria.values():
        total_items = total_items + quantity
    for item in inventoria.items():
        t_items += 1

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {t_items}\n")

    print("=== Current inventory ===")
    for item, quantity in inventoria.items():
        percentage = (quantity / total_items) * 100
        print(f"{item} : {quantity} ({percentage:.1f}%)")

    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {most_item} ({inventoria.get(most_item)} units)")
    print(f"Least abundant: {least_item} ({inventoria.get(least_item)} units)")

    print("\n=== Item Category ===")
    for item, quantity in inventoria.items():
        if quantity <= 3:
            categories["Scarce"].update({item: quantity})
        elif quantity <= 5:
            categories["Moderate"].update({item: quantity})

    for category, items in categories.items():
        print(category, end=": {")
        first = True
        for item, quantity in items.items():
            if not first:
                print(", ", end="")
            print(f"'{item}':{quantity}", end="")
            first = False
        print("}")

    print("\n=== Management Suggestion ===")
    print("Restock Needed:", end="")
    for item, quantity in inventoria.items():
        if quantity == 1:
            print(" [", end="")
            print(f"'{item}'", end="]")
    print("")

    print("\n=== Dictionary Properties Demo ===")
    print("Dictionary keys: ", end="[")
    first = True
    for item, quantity in inventoria.items():
        if not first:
            print(", ", end="")
        print(f"'{item}'", end="")
        first = False
    print("]")

    print("Dictionary Values: ", end="[")
    first = True
    for item, quantity in inventoria.items():
        if not first:
            print(", ", end="")
        print(f"{quantity}", end="")
        first = False
    print("]")
    x = inventoria.get("sword", None)
    if x is not None:
        print("Sample lookup - 'sword' in inventory: True")


def main() -> None:
    """This function takes input, check for error and
    passes data to inventory data"""
    try:
        if len(sys.argv) == 1:
            raise InventoryError("Please Input inventory")
        else:
            categories = dict()
            categories.update({
                "Scarce": dict(),
                "Moderate": dict(),
                })

            inventoria = dict()
            args = sys.argv
            index = 1

            while index < len(args):
                pair = args[index].split(":")
                item = pair[0]
                quantity = int(pair[1])

                # Add quantity if item already exists
                quantity = inventoria.get(item, 0) + quantity

                # Insert item in sorted order (most to least)
                new_inventory = dict()
                inserted = False

                for existing_item, existing_quantity in inventoria.items():
                    if inserted is False and quantity > existing_quantity:
                        new_inventory.update({item: quantity})
                        inserted = True

                    new_inventory.update({existing_item: existing_quantity})

                if inserted is False:
                    new_inventory.update({item: quantity})

                inventoria = new_inventory
                index = index + 1

            inventory_analytics(inventoria, categories)
    except (ValueError, IndexError):
        print("Missing Values, please check input")
    except InventoryError as e:
        print(e)


if __name__ == "__main__":
    main()
