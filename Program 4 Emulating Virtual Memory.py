# Owen O'Neil
# Program 4 Emulating Virtual Memory
# 11/11/24
# Test
# import the math function
import math
# import teh random choice method
from random import choice

#create the Main Memory class
class MainMemory:
    # initialize
    def __init__(self, max_pages):
        self.max_pages = max_pages
        # create an empty list for main memory
        self.main_memory = [-1] * self.max_pages
        # create an empty list for the page tables
        self.page_tables = []

    # subroutine that adds a page table to the page tables list
    def add_page_table(self, page_table):
        self.page_tables.append(page_table)

# create page table class
class PageTable:
    # initialize
    def __init__(self, virtual_memory_size, words_in_page):
        self.virtual_memory_size = virtual_memory_size
        self.words_in_page = words_in_page
        # create an empty list the size of the virtual memory and initialize every index with "-"
        self.page_table_list = ['-'] * self.virtual_memory_size


# create the cpu class
class CPU:
    # initialize
    def __init__(self, words_in_page, max_pages):
        self.words_in_page = words_in_page
        # set the main memory class so that it is accessible in cpu class
        self.main_memory = MainMemory(max_pages)
        # initialize page faults and total instructions accessed
        self.page_faults = 0
        self.total_instructions_accessed = 0

    # subroutine that executes each instruction
    def execute_instruction(self, virtual_address):
        # set the page length using the size of the page table list and math functions
        page_len = math.ceil(math.log(len(self.main_memory.page_tables[-1].page_table_list))/math.log(2))
        # get the page number in binary by splitting the instruction by the page length
        page_num_binary = virtual_address[:page_len]
        # convert it to decimal value
        page_num_dec = int(page_num_binary, 2)
        # increase the instructions accessed by 1
        self.total_instructions_accessed += 1

        # if the page number in the page table list is a "-"
        if (self.main_memory.page_tables[-1].page_table_list[page_num_dec]) == "-":
            # add 1 to the fault count
            self.page_faults += 1
            # find a random spot in the main memory using the length of the main memory
            d = choice(range(max_main_memory))

            # while there is an empty space in main memory and the random index choice is not -1
            while -1 in self.main_memory.main_memory and self.main_memory.main_memory[d] != -1:
                # choose a new index for the number to be placed in
                d = choice(range(max_main_memory))

            # add an "F" to the main memory index indicating that it full
            self.main_memory.main_memory[d] = "F"

            # if the random index choice is already in the list
            if d in self.main_memory.page_tables[-1].page_table_list:
                # set the previous similar index with a "-" and place the number in the new index
                self.main_memory.page_tables[-1].page_table_list[self.main_memory.page_tables[-1].page_table_list.index(d)] = "-"
            self.main_memory.page_tables[-1].page_table_list[page_num_dec] = d

    # subroutine that starts a new program when current instruction is "NEW"
    def start_new_program(self, virtual_memory_size, lastoutput):
        if not lastoutput:
            # call the add page table subroutine in main memory while passing through the page table subroutine so that main memory has access to it
            self.main_memory.add_page_table(PageTable(virtual_memory_size, self.words_in_page))
            # print the fault rate in specific format by while calling the page fault subroutine
        print(f"{self.page_fault_rate():6.3f}%")

        t = 0
        # for t in the range of the page tables
        for t in range(len(self.main_memory.page_tables)):
            # for j in the range of teh page tables list with index t
            for j in range(len(self.main_memory.page_tables[t].page_table_list)):
                # print the page table list without any brackets
                print(f"{self.main_memory.page_tables[t].page_table_list[j]} ", end="")
            # add an empty line under
            print()
            # add 1 to t to move onto the next index
            t += 1

    # subroutine that calculates the page fault rate
    def page_fault_rate(self):
        # if the page faults and total instructions accessed are both 0 then return 0 to avoid dividing by zero
        if self.page_faults == 0 and self.total_instructions_accessed == 0:
            return 0
        # else, divide the total faults by the total instructions accessed
        else:
            fault_rate = (self.page_faults / self.total_instructions_accessed) * 100
            # return the fault rate
            return fault_rate



##MAIN##
# set the file to a varable
input_file = ("input1.txt")
# open the input file and read the lines
with open(input_file, 'r') as f:
    lines = f.readlines()

# the first line = the words in page
words_in_page = int(lines[0])
# the second line = the max length of main memory
max_main_memory = int(lines[1])
# initialize the CPU class while passing through the words in page and the max main memory length
cpu = CPU(words_in_page, max_main_memory)

# skip the first two lines
i = 2
# while is in the input
while i < len(lines):
    # get rid of the extra space at the end
    line = lines[i].strip()
    # if the instruction is "NEW"
    if line == "NEW":
        # go to the next instruction
        i += 1
        # set that to the virtual memory size
        virtual_memory_size = int(lines[i].strip())
        # call the start new program subroutine in the cpu class and pass through virtual memory size
        cpu.start_new_program(virtual_memory_size, False)
        # calculate the fault rate
        cpu.page_fault_rate()
    else:
        # call the execute instruction subroutine from the CPU class and pass through the current instruction
        cpu.execute_instruction(lines[i])
    # go to the next instruction
    i += 1
# print the final ouput
cpu.start_new_program(1, True)