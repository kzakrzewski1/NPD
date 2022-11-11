p_book = {}
numbers = set()

def add_number(f_name,l_name,type,number):
    if number in numbers:
        print("Number already in use\n")
        return
    else:
        if (f_name,l_name) in p_book:
            p_book[(f_name,l_name)].append((type, number))
        else:
            p_book[(f_name,l_name)] = [((type, number))]
        numbers.add(number)


def retrieve_all(f_name,l_name):
    print(f"{f_name} {l_name}: {p_book[(f_name,l_name)]}\n")

def retrieve_type(f_name,l_name,type):
    print(f"{f_name} {l_name} ({type}): ", end="") 
    for item in p_book[(f_name,l_name)]:
        if item[0] == type:
            print(f"{item[1]}; ", end="")
    print("\n")      


def del_number(f_name, l_name, which):    #Podajemy, który numer chcemy usunąć (liczymy od 1)
    p_book[(f_name,l_name)].pop(which-1)

add_number("Jan","Kowalski","main","123-456-789")
add_number("Jan","Kowalski","work","231-564-897")
add_number("Andrzej","Nowak","work","523-532-352")
add_number("Andrzej","Nowak","work","321-654-987")

print()
print(f"{p_book} \n")

add_number("Andrzej","Nowak","main","123-456-789")

retrieve_all("Jan", "Kowalski")
retrieve_type("Andrzej", "Nowak","work")

del_number("Jan", "Kowalski",2)

print(f"{p_book} \n")
