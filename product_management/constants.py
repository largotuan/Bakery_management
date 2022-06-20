

class select_quantity:
    add_quantity = 0
    expired_quantity = 1
    inventory_quantity = 2

    QUANTITY_CHOICE = (
        (add_quantity, 'add_quantity'),
        (expired_quantity, 'expired_quantity'),
        (inventory_quantity, 'inventory_quantity')
    )

    QUANTITY_CHOICE_DICT = dict(QUANTITY_CHOICE)
