#02_linearhashing.py
#Program to implement Hashing with Linear Probing

from DSAL.record import Record

class hashTable:
    #Initializing Hash Table
    def __init__(self):
        self.size = int(input("Enter the size of Hash Table: "))
        #initializing table with all elements 0
        self.table = list(None for i in range (self.size))
        self.elementCount = 0
        self.comparisons = 0

    #Method that checks if the hash table is full or not
    def isFull(self):
        if self.elementCount == self.size:
            return True
        else:
            return False

    #Method that returns position for a given element 
    def hashFunction(self, element):
        return element % self.size

    #Method that inserts element into the hash table 
    def insert(self, record):
        #Checking if the table is full
        if self.isFull():
            print("Hash Table is Full !!")
            return False
        
        isStored = False 

        position = self.hashFunction(record.get_number())

        #Checking if the position is Empty
        if self.table(position) == None:
            self.table(position) = record
            print("Phone Number of "+ record.get_name() + " is at positon" + str(position))
            isStored = True
            self.elementCount += 1
        return isStored

    #Method that searches for an element in the table
    #Returns position of element if found
    #else return False

    def search(self, record):
        found = False

        position = self.hashFunction(record.get_Number())
        self.comparisons += 1

        if(self.table[position] != None):
            if(self.table[position].get_name() == record.get_name() and self.table[position].get_number() == record.get_number()) :
                 isFound = True
                 print("Phone number found at position {} ".format(position) + " and total comparisons are " + str(1))
                 return position

    # if element is not found at position returned hash function

        else:
            position += 1
            if position >= self.size-1:
                position = 0
            while self.table[position] != None or self.comparisons <= self.size:

                if(self.table[position].get_name() == record.get_name() and self.table[position].get_number() == record.get_number()):
                    isFound = True
                    #i=0
                    i = self.comparisons + 1
                    #print(position)
                    if position >= self.size-1:
                        position = 0

                    #print(position)  
                    self.comparisons += 1
                    #print(self.comparisons)

                if isFound == False:
                    print("Record not found")
                    return False

    #Method to display the hash table 
    def display(self):
        print("\n")
        for i in range(self.size):
            print("Hash Value: "+ str(i) + "\t\t" + str(self.table[i]))
        print("The number of phonebook records in the Table are : "+str(self.elementCount))
