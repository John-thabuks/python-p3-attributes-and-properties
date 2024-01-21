#!/usr/bin/env python3

"""
NOTE: Because we want to instantiate our Dogs and People with their 
properties, remember to include set values in __init__() using 
the property name and not the protected attribute name.

"""




APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    #name property:
        #str
        #between 1 => 25
        #convert to capitalize()
    #__init__: recive name, job= "Marketing"
        #if name invalide; setter checks
    #Property: job
    #if job invalide: setter checker
        #job must be in list
    
    def __init__(self, name="Person", job="Marketing"):
        self.name = name
        self.job = job
        
    def get_name(self):
        return self._name
    
    def get_job(self):
        return self._job
    
    def set_name(self, new_name):
        if type(new_name) == str and (1 <= len(new_name) <= 25):
            self._name = new_name.title()

        else:
            print("Name must be string between 1 and 25 characters.")

    def set_job(self, new_job):
        if new_job in APPROVED_JOBS:
            self._job = new_job

        else:
            print("Job must be in list of approved jobs.")

    name = property(get_name, set_name)
    job = property(get_job, set_job)