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
            return """No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.
"""		
        else:
           return """{0} {1} of beer on the wall, {0} {1} of beer.
Take {3} down and pass it around, {2} """.format(number,self.container(number), self.no_more(number-1),self.only(number)) + """{0} of beer on the wall.
""".format(self.container(number-1))
    
    def container(self,number):
        if number == 1:
            return "bottle"
        else:
            return "bottles"
    def no_more(self,number):
        if number == 0:
            return "no more"
        else:
            return number
    def only(self, number):
        if number == 1:
            return "it"
        else:
            return "one"



        
