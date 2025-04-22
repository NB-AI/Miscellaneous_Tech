class Lfsr():

    def __init__(self):
        """default constructor"""
        self.fall_out_ele1 = None
        self.fall_out_ele2 = None
        self.fall_out_ele3 = None

        self.my_lfsr1 = []
        self.my_lfsr2 = []
        self.my_lfsr3 = []

    def a5_rand(self):
        """Method "a5_rand" to calculate and return a random number according to the requested algorithm
        :return int
        """
        self.get_lfsr1()
        self.get_lfsr2()
        self.get_lfsr3()
        final_random_number = self.fall_out_ele1^self.fall_out_ele2^self.fall_out_ele3
        return final_random_number


    def get_lfsr1(self):
        """Method "get_lfsr1" to return the content of the LFSR1 as an integer array
        :return int array
        """
        # generate a list of length 19:
        if len(self.my_lfsr1) == 0:
            for i in range(19):
                self.my_lfsr1.append((19-1-i)) # the highest value is at first index position

        # make the xor operation as on the assignment sheet:
        # link the first two elements together:
        first_xor = self.my_lfsr1[0]^self.my_lfsr1[1]
        second_xor = first_xor^self.my_lfsr1[2]
        third_xor = second_xor^self.my_lfsr1[5]

        # all list ele are shifted to the left:
        self.fall_out_ele1 = self.my_lfsr1.pop(0)

        # add xor number to the rightest place of list:
        self.my_lfsr1.append(third_xor)

        return self.my_lfsr1

    def get_lfsr2(self):
        """Method "get_lfsr2" to return the content of the LFSR2 as an integer array
        :return int array
        """
        if len(self.my_lfsr2) == 0:
            for i in range(22):
                self.my_lfsr2.append((22-1-i))

        first_xor = self.my_lfsr2[0]^self.my_lfsr2[2]
        self.fall_out_ele2 = self.my_lfsr2.pop(0)
        self.my_lfsr2.append(first_xor)

        return self.my_lfsr2

    def get_lfsr3(self):
        """Method "get_lfsr3" to return the content of the LFSR3 as an integer array
        :return int array
        """
        if len(self.my_lfsr3) == 0:
            for i in range(23):
                self.my_lfsr3.append((23-1-i))

        first_xor = self.my_lfsr3[0]^self.my_lfsr3[1]
        second_xor = first_xor^self.my_lfsr3[7]
        third_xor = second_xor^self.my_lfsr3[15]
        self.fall_out_ele3 = self.my_lfsr3.pop(0)
        self.my_lfsr3.append(third_xor)

        return self.my_lfsr3

