# Runtime Complexity O(N*b) # N as number of elements in the input list, b as the length of the longest element in the input list
class RadixSort:
    def __init__(self):
        self.first_call = True # when a method is not recursively called it shall the code will know that the procedure
        # of sorting begins again
        self.instance = None

        self.string_list = [] # to slice over the numbers convert them into strings and make a string list
        self.number_iterations = 0 # 0 will be overwritten by the length of the longest element in list
        self.radix_index = 1 # the index shall start with 1 # mine!!! löschen
        self.base = 10
        #                                _________list of bucketlists
                                 #  | ________list of buckets -> list of buckets as array here
        self.list_of_buckets = [[],[],[],[],[],[],[],[],[],[]]          #                || ___________content of a bucket -> buckets as arrays here

        #                               |||
        self.bucket_list_history = []  #[[[]]] -> will look like this in the end

    def get_bucket_list_history(self):
        return self.instance.bucket_list_history

    def sort(self, list):
        """
        Sorts a given list using radixsort in ascending order
        @param list to be sorted
        @returns the sorted list as an 1D array
        @raises ValueError if the list is None
        """
        if self.first_call == True:
            self.first_call = False
            self.instance = RadixSort()

        if list == None:
            raise ValueError('Input list is None!')

        # for first function call:
        # to slice over the numbers convert them into strings and make a string list:

        else:
            if self.instance.string_list == []:

                # have a look how much iteration steps are needed:
                highest_number = f'{max(list)}'
                self.instance.number_iterations = len(highest_number)

                for ele in list:
                    self.instance.string_list.append(str(ele))


            # stop when you have sorted the first part of each digit:
            if self.instance.radix_index > self.instance.number_iterations:
                n = 0
                self.first_call = True
                for string in self.instance.string_list:
                    self.instance.string_list[n] = int(string)
                    n += 1

                return self.instance.string_list


            # fill up the shorter numbers with zeros in their fronts:
            i = 0
            for str_ele in self.instance.string_list:
                if len(str_ele) < self.instance.number_iterations:
                    difference = self.instance.number_iterations - len(str_ele)

                    str_ele = f'{"0" * difference}{str_ele}'

                    self.instance.string_list[i] = str_ele


                comparison_digit_part = str_ele[-self.instance.radix_index]

                print(self.instance.string_list)
                # put in the numbers of the list into the buckets
                j = 0
                for bucket in self.instance.list_of_buckets:
                    if int(comparison_digit_part) == j:

                        bucket.append(int(str_ele))
                    j += 1
                i += 1

            self.instance.string_list=[]
            for bucket in self.instance.list_of_buckets:
                for number in bucket:
                    self.instance.string_list.append(str(number))

            self.instance._add_bucket_list_to_history(self.instance.list_of_buckets)
            self.instance.list_of_buckets = [[],[],[],[],[],[],[],[],[],[]] # for the next iteration reset the list of buckets

            self.instance.radix_index += 1  # becomes with each iteration higher

            return self.sort(self.string_list)


    def _add_bucket_list_to_history(self, bucket_list):
        """
        This method creates a snapshot (clone) of the bucketlist and adds it to the bucketlistHistory.
        @param bucket_list is your current bucketlist, after assigning all elements to be sorted to the buckets.
        """
        arr_clone = []
        for i in range(0, len(bucket_list)):
            arr_clone.append([])
            for j in bucket_list[i]:
                arr_clone[i].append(j)

        self.bucket_list_history.append(arr_clone)
