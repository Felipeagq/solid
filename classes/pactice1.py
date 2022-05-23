from __future__ import annotations
# este modulo permite la recursividad de una clase
# permite una clase llamarse a si misma

from typing import final
# Error reported by type checker: impide el polimorfismo de una clase 
# Error reported by type checker: impide el polimorfismo de un metodo de una clase


# @final
class Father:

    def __init__(self,name):
        self.name = name

    def func1(self):
        return f"function1 of {self.name}"

    def relation(self, other:Father):
        return f"{self.name} --> {other.name}"


class Son(Father):  # Error reported by type checker
    def asd(self):
        return f"{self.name}"

a = Father("felipe")
b = Father("Camila")
print(a.relation(b))
print("--"*50)

f = Son("duvan")
print(f.asd())
print(f.func1())