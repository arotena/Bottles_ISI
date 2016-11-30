class   CONTAINER_NUMBER:

    def __init__(self,number):
        self.number = number
    
    def container(self):
        if self.number == 1:
            return "bottle"
        else:
            return "bottles"

    def no_more(self):
        if self.number == 0:
            return "no more"
        else:
            return self.number

    def it_one(self):
        if self.number == 1:
            return "it"
        else:
            return "one"

