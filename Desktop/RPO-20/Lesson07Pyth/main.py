# def hello(name, age):  #Sozdaiom funkciu, prinimaet neskolko parrrametrov
#     print(f"hello!!! {name}, {age + 1}")

# hello("Oleg", 23)


# def hello(name = "Oleg", age=25):  #funccia mojet brat znachenie po umolchaniu
#     print(f"hello!!! {name}, {age + 1}")

# hello()

# def hello(name = "Oleg", age=25): #Vozvrashaet funkcii, no mjno sokratit zapis
#     return f"hello!!! {name}, {age + 1}"

# # result1 = hello("Oleg") # Ne korotkoe 
# # print(result1)

# print(hello("Ivan")) #Korotkaia veersia zapisi RESULT1

# def hello(name = "Oleg", age=25):
#     if age > 15:
#         return f"hello {name} u are {age} year old"
#     return "error". #Mojno i bez ELSE

# print(hello())

# def greet(): # Oblast vidimosti
#     number = 5
#     return number * 2

# def add(a:int, b:int) -> int:     #Eto nujno chto bi navestis i posmotret chto prinimaet funkcia i chto vozvrashaet 
#     return a + b


# def add(*args):
#     print(args) #Eto mehanizn s pomoshiu kotorih mojno peredavat NEOGRANICHENNOe kolichestvo NEIMENOVONNIH
#     return sum(args)

# print(add(1,2,3,4))
# print(add(5,6))
# print(add(5,5,4,6,7,10))



# def example(**kwargs):  #Eto mehanizn s pomoshiu kotorih mojno peredavat NEOGRANICHENNOe kolichestvo !!! IMENOVONNIH !!!
#     print(kwargs)
#     print(kwargs["name"])
#     print(kwargs["age"])
#     print(kwargs.get("city", "London"))

# example(name= "Oleg", age=55)



# def mixin(*args, **kwargs):
#     print(args)
#     print(kwargs)

# mixin(1,2,3,4,5, name = "Pavlos", age= 55) # Perediom snachalo neimenovannie a potom imenovanie i ne mojen iz smeshivat i zakladivat dru v druga 

# def mixin(a, b, *args, city="London", **kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(city)
#     print(kwargs)

# mixin(1,2,3,4,5, city="Munich", name = "Pavlos", age= 55) 




# list1 = [1,2,3,4,5]
# print(*list1)     # Eto raspakovka vsego

# dict1 = {
#     "name": "Ivan",
#     "age": 25
# }
                                   #Raspakovka slovaria
# def example(name, age):
#     print(f"{name} {age}")


# print(*list1)
# example(**dict1)



# num = 5
# list1 = [1,2,3]

# def number(x:list) -> list:
#     y = x[::]
#     y.append(4)
#     return y

# print(list1)
# print(number(list1))


# add = lambda a, b : a + b
# print(add(5,10))

# list1 = [1,2,3,4,5]
# squList1 = [x**2 for x in list1]
# print(squList1)

# squList2 = list(map(lambda x: x **2, list1)) # uslovno primeni funkciu X ko vsemu iz LIST1




# names = ["Alice", "Bob", "Charlie", "aasasa"]
# ages = [25, 30, 35]
# combined = list(zip(names, ages)) # Skleivaet s kolekciami kotorie odinaovie po dline
# print(combined)  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]


# list1, list2 = zip(*combined)
# print(list1, list2)





# list2 = [1,2,3,4,5,6,7,8,9,10]

# list3 = list(filter(lambda x: x % 2 != 0, list2))
# print(list3)