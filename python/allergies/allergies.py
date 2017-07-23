allergies = { 1: "eggs", 2: "peanuts", 4: "shellfish", 8: "strawberries",
                      16: "tomatoes", 32: "chocolate", 64: "pollen", 128: "cats" }

class Allergies(object):
    def __init__(self, num):
        self.lst = []
        self.num = num
        
    def  is_allergic_to(self, item):
        if item in self.lst:
            return True
        return False

    def find_allergies(self, num):
        for i in allergies.keys():
            if num - i in ([0] + allergies.keys()):
                self.lst.append(allergies[i])
