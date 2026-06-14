# def look_for_key(main_box):
#   pile = main_box.make_a_pile_to_look_trhough()
#   while pile is not empty:
#     box = pile.grab_a_box()
#     for item in box:
#       if item.is_a_box():
#                 pile.append(item)
#       elif item.is_a_key():
#                 print('Found the key!')


def look_for_key(box):
    for item in box:
        if item.is_a_box(4):
            look_for_key(item)
        elif item.is_a_key(1):
            print('Found the key!')

