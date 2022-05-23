from __future__ import annotations

class Duck:

    def __init__(self,name):
        self.name = name
    

    def fly(self):
        print(f"{self.name} its flying")
    
    def swim(self):
        print(f"{self.name} its swimming")
    
    def do_sound(self) -> str:
        return "Quack"
    
    def greet(self, duck2:Duck):
        print(f"{self.name}:{self.do_sound()}, hello {duck2.name}")


donald = Duck("Donald")
print(donald.name)