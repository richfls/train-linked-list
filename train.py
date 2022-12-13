import random
class TRAINS:
    def __init__(self,model,isfull,next=None):
        self.model = model
        self.ID = random.randrange(200)
        self.isfull = isfull
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,model,isfull):
        newtrain = TRAINS(model,isfull)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newtrain
        else:
            self.head = newtrain
            
    def printList(self):
        current = self.head
        while current:
            print("Train Model: ",current.model,", ID:", current.ID,", Is The Train Full: ", current.isfull)
            current = current.next
    def amount(self):
        current = self.head
        a = 0
        while current:
            a +=1
            current = current.next
        print(a)

    def search(self):
        current = self.head
        model = input("what train are you looking for\n")
        while current:
            if current.model == model:
                print("I have found the person")
                return True
            elif current.model != model:
                current = current.next
        print("person was not found")
    
    def searchid(self):
        current = self.head
        ID = input("what id are you looking for\n")
        while current:
            if current.ID == ID:
                print("Here is your train: ",current.printlist())
                return True
            elif current.ID != ID:
                current = current.next
        print("ID not found")

train = LinkedList()
l = ''
while l != 'q':
    num = int(input("how many people would you like to add\n"))
    for i in range(num):
        model = input("what is the model\n")
        isfull = input("Is the train full True or False\n")
        train.insert(model,isfull)
    l = input("What would you like to do search for train id(i), search for cargo and how many trains of those types(c), or toot the horn(h)\n")
    if l == 'i':
        train.searchid()
   
    


train.printList()
