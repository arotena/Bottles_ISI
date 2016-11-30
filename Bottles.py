from container import CONTAINER_NUMBER
class Bottles:

    def song(self):
        return self.verses(99,0)

    def verses(self, last, first):
        o = self.verse(last)
        for i in range (last-1, first-1, -1):
            o += "\n" + self.verse (i) 
        return o

    def verse(self, number = None):
        actual = CONTAINER_NUMBER(number)
        menos1=CONTAINER_NUMBER(number-1)
        if number == 0:
            return """No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.
"""		
        else:
           return """{0} {1} of beer on the wall, {0} {1} of beer.
Take {3} down and pass it around, {2} """.format(number,actual.container(), menos1.no_more(),actual.it_one()) + """{0} of beer on the wall.
""".format(menos1.container())
    
    



        
