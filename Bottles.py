class Bottles:

    def song(self):
        return self.verses(99,0)

    def verses(self, last, first):
        o = self.verse(last)
        for i in range (last-1, first-1, -1):
            o += "\n" + self.verse (i) 
        return o

    def verse(self, number = None):
        if number == 0:
            bottle_number = Type_0(number)
            next_bottle_number = BottleNumber(bottle_number.successor())
        elif number == 1:
            bottle_number = Type_1(number)
            next_bottle_number = Type_0(bottle_number.successor())
        elif number == 2:
            bottle_number = BottleNumber(number)
            next_bottle_number = Type_1(bottle_number.successor())
        elif number ==6:
            bottle_number = Type_6(number)
            next_bottle_number = BottleNumber(bottle_number.successor())
        elif number == 7:
            bottle_number = BottleNumber(number)
            next_bottle_number = Type_6(bottle_number.successor()) 
        else:
            bottle_number = BottleNumber(number)
            next_bottle_number = BottleNumber(bottle_number.successor())
        result = \
            "{0} {1} of beer on the wall, ".format(bottle_number.quantity().capitalize(), bottle_number.container()) + \
            "{0} {1} of beer.\n".format(bottle_number.quantity(), bottle_number.container()) + \
            "{0}, ".format(bottle_number.action()) + \
            "{0} {1} of beer on the wall.\n".format(next_bottle_number.quantity(), next_bottle_number.container())

        return result
        
class BottleNumber:
    def __init__(self, number):
        self.number = number

    def container(self):
        return "bottles"

    def quantity(self):
        return str(self.number)
        
    def action(self):
        return "Take {0} down and pass it around".format(self.pronoun())

    def pronoun(self):
        return "one"

    def successor(self):
        return self.number - 1
        

class Type_0(BottleNumber):
    def quantity(self):
        return "no more"
    def action(self):
        return "Go to the store and buy some more"
    def successor(self):
        return 99
class Type_1(BottleNumber):
    def pronoun(self):
        return "it"
    def container(self):
        return "bottle"
class Type_6(BottleNumber):
    
    def container(self):
        return "six_pack"
    def quantity(self):
        return "1"
    



