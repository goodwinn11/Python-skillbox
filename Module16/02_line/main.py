# TODO здесь писать код
def sort(class_members):
    for i_current in range(len(class_members)):
        for i_compare in range(i_current, len(class_members)):
            if class_members[i_current] > class_members[i_compare]:
                class_members[i_current], class_members[i_compare] = class_members[i_compare], class_members[i_current]
    return class_members


first_class_members = list(range(160, 176 + 2, 2))
second_class_members = list(range(162, 180 + 3, 3))
first_class_members.extend(second_class_members)
united_class = sort(first_class_members)
print(united_class)
