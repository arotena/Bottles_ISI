class   CONTAINER_NUMBER:

    
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

    def it_one(self, number):
        if number == 1:
            return "it"
        else:
            return "one"

