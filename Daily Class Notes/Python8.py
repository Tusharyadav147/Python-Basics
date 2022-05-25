#Object orentation programming OOPs

"""
it has 7 properties

1) class = Collecton of variable and  methods(functions)  , its is an updated version of structure, its a blue print
2) object = runtime or realtime entities(unique) 
3) Abstraction and encaptulation = abstraction( hiding things like water bottle, showing only essention feature without showing any background details), encaptulation = wrapping up of data in a single unite e.g .py , classes
4) inheritance = acquiring properties of one class into another, it is of 5 type = 1. single level inheritance, 2. multi level inheritance, 3. herirchal inheritance, 4. multiple inheritance, 5. hybrid inheritance
5) polymorphisms = same name multiple functionality, it is of two type = 1. method overloading, 2. method overwriting
6) dynamic memory allocation = runtime memory allocation
7) message passing = communication between object
"""

class Cricket:
    def bat(self):
        print("Hello From Bat")

c = Cricket()
c.bat()
print(c)