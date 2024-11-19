#Owen O'Neil
#program 1
#CSC 210


class Number:
    # initiate the class
    def __init__(self, value, num_base, new_base, new_length):
        self.value = value
        self.num_base = int(num_base)
        self.new_base = new_base
        self.new_length = new_length
        # set the objects

    # subroutine converts from old base to base 10
    def convert_base_10(self):
        if self.num_base == 10:
            return int(self.value)
            # if the new base is also 10 then return the starting number
        # otherwise convert the starting number to base 10
        else:
            total = 0
            num_len = len(self.value)
            # get the length of the number
            for i, n in enumerate(self.value):
                # enumerate allows the program to keep track of the elements and its positon on a list so the program can go through the whole number one index at a time until it reaches the end
                n = int(n)
                # converts the number back into an integer, so we can do math with it later
                power = num_len - i - 1
                # get the correct power by subtracting the current index by the total length of the number
                digit = n * (self.num_base ** power)
                # take the current element and multiply it by the base ** power
                total += digit
                # add the final number from digit to the total
            return total

    # subroutine converts number from base 10 to new base
    def convert_new_base(self, base_10):
        if self.new_base == self.num_base:
            return str(base_10)
        # if the new base is the same as the old one then return the converted number
        # otherwise convert the number to its new base
        else:
            remainder_array = ""
            # where the final number will be stored
            divided_output = base_10
            # setting the number with base 10 to start
            while divided_output > 0:
                remainder = divided_output % int(line_numbers[2])
                # gets the remainder from the number divided by the new base
                divided_output = divided_output // int(line_numbers[2])
                # takes the number and divides it by the new base and sets divided output to that new number until it reaches 0
                if remainder == 10:
                    remainder_array = "A" + remainder_array
                elif remainder == 11:
                    remainder_array = "B" + remainder_array
                elif remainder == 12:
                    remainder_array = "C" + remainder_array
                elif remainder == 13:
                    remainder_array = "D" + remainder_array
                elif remainder == 14:
                    remainder_array = "E" + remainder_array
                elif remainder == 15:
                    remainder_array = "F" + remainder_array
                    # if the number is from 10-15 a hex letter will be added in its place to the remainder array
                else:
                    remainder_array = str(remainder) + remainder_array
                    # puts the remainder into an array so that the final number will be at the start of the array

            return remainder_array


    # subroutine counts how many zeros need to be added
    def count_zeros(self, converted_digits):
        add_zeros = ""
        # final number array
        add_zeros += str(converted_digits)
        # add the converted number to the array
        hex_letters = ["A", "B", "C", "D", "E", "F"]
        # possible hex letters
        counter = 0
        # initialize the counter
        for i in add_zeros:
            # goes through the array and counts how many digits there are
            if i in hex_letters:
                counter += 2
                # hex letters are 2 digits so ad 2 to the counter
            else:
                counter += 1
                # otherwise add 1

        if counter > int(self.new_length):
            return "Overflow\n"
            # if the amount of digits is over the digits needed, return overflow

        elif counter == int(self.new_length):
            return f"{add_zeros}\n"
            # if the amount of digits is the same as the digits needed, return the number

        elif counter < int(self.new_length):
            # if not enough digits
            while counter < int(self.new_length):
                add_zeros = "0" + add_zeros
                # place a zero infront of the current number
                counter += 1
                # add 1 to the count
            return f"{add_zeros}\n"
            # return the number once teh condition is met


###########
#  Main
###########

sample_numbers = "input.txt"
# set input file
outputfile = open("output.txt", "w")
# open output file
# open the sample number file
with open(sample_numbers, "r") as f:
    lines = f.read().splitlines()
    # read the lines in the input file
    for line in lines:
        line_numbers = line.split()
        #split each line
        number = Number(line_numbers[0], line_numbers[1], line_numbers[2], line_numbers[3])
        # set the class
        base_10 = number.convert_base_10()
        # set the base 10 converter subroutine
        converted_digits = number.convert_new_base(base_10)
        # set the base 10 to new base converter subroutine
        final_num = number.count_zeros(converted_digits)
        # set the final number return from count zeros subroutine
        outputfile.write(str(final_num))
        # send the final number as a string to the output file
