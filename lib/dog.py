#!/usr/bin/env python3

"""
NOTE: Because we want to instantiate our Dogs and People with their 
properties, remember to include set values in __init__() using 
the property name and not the protected attribute name.

"""

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    #property:  name of type str and its len between 1 -> 25
    #name default 
    
    def __init__(self, name="name", breed="Pug" ):        
        self.name = name
        self.breed = breed

    def get_name(self):
        return self._name
    
    def get_breed(self):
        return self._breed

    def set_name(self, new_name):
        if type(new_name) == str and (1 <= len(new_name) <= 25):
            self._name = new_name
        
        else:
            print("Name must be string between 1 and 25 characters.")
        
    def set_breed(self, new_breed):
        if new_breed in APPROVED_BREEDS:
            self._breed = new_breed

        else:
            print("Breed must be in list of approved breeds.")

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)