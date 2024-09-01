immutable_var = 1, 2, "a", "b"
mutable_list = [1, 2, "a", "b", "c"]
mutable_list[4] = "Modified"
print(immutable_var)
print(mutable_list)
immutable_var[0] = 5
print(immutable_var) #является неименяемой коллекцией. не поддерживает обращение по элементам