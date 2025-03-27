# Include Tuple Manipulate

# tuple_data = (23, 798, -9, 'Julia', 'Python', 99, 'R')
#
# # Konversi tuple ke list
# list_data = list(tuple_data)
#
# # Ubah nilai pada indeks ke-3
# if list_data[3] == "Julia":
#     list_data[3] = "Yulia"
#
# # Konversi kembali ke tuple
# tuple_data = tuple(list_data)
#
# print(tuple_data)

# Analysis no 1

# my_set = {1, 2, 3, 4, 5}
#
# my_set.discard(10)
# my_set.remove(1)
#
# print(my_set)

# Analysis no 2 

this_list = ["Hello World!", 20, 6, 2005, "Surabaya"]
this_list_2 = ["Ling", "Gang", "Guli"]

# Append
this_list.append("Acumalaka")

# Insert
this_list.insert(1, "Medium")

# Extend
this_list.extend(this_list_2)

# List
this_list.pop(0)

# Main Output
print(this_list)
