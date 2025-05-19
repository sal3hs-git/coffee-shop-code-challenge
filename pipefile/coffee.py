class coffee:
def __init__(self,name)
self.name = name 
   if not isintance (name,str):
    raise TypeError("Name must be a string")   
   if len(name) <3:
    raise ValueError ("Name must be at leaast 3 characters long.")
    self._name = name 

    def name(self):
        return self._name 