# class tagCloud:
#     def __init__(self):
#         self._tags = {}


#     def add(self, tag):
#         self.tags{tag} = self.get(tag, 0) + 1 



#     def __getitem__(self, tag):
#         return self.tags.get(tag, 0)
    

    
#     def __setitem__(self, tag other):
#         self.tags[tag] = other


#     def __len__(self):
#         return len(self.tags)
    

#     def __iter__(self):
#         return iter(self.tags.items())
    























# import timeit


# print(timeit.timeit("[x*2 for x in range(1000)]", number = 1000))
# print(timeit.timeit("result=[]\nfor y in range(1000): result.append(y ** 2)", number = 1000))







#class FutureFeature:
#    pass











# class InvalidOperationError(Exception):
#     pass

# raise InvalidOperationError("""Error InvalidOperationError
#                             Error in class
#                             !!!!!!!""")














# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)









class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone



class AddressBook:
    def __init__(self):
        self.contacts = []

    def __add__(self, contact):
        self.contacts.append(contact)

    def remove(self, name):
        self.contacts = [c for c in self.contacts if c.name != name]

    def search(self, name):
        return [c for c in self.contacts if c.name == name]
