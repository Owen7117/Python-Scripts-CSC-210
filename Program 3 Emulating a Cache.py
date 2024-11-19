# Owen O'Neil
# Program 3: Emulating a Cache
# 10/20/24


# CPU class - executes instructions and keeps track of hits and misses
class CPU:
    # initialize the class
    def __init__(self, block_size, cache_size, cache):
        self.block_size = block_size  # initiate the block size
        self.cache_size = cache_size  # initiate the cache size
        self.cache = cache  # initialize the cache class so subroutines from cache class are available for use
        self.hits = 0  # initialize hits and misses to zero
        self.miss = 0

    # execute the instruction subroutine
    def execute_instruction(self, current_instruction):
        # if the instruction is CLEAR it will clear the cache by calling the create_cache_list subroutine
        if current_instruction == "CLEAR":

            self.cache.create_cache_list()
        # if the fist 3 letters in the instruction are DEL, it will delete block number form the cache if its present
        elif current_instruction[0:3] == "DEL":
            block_to_delete = int(current_instruction[4:], 16)  # convert the hex numbers after DEL into decimal
            if block_to_delete in self.cache.cache_list:  # if the block number is in the list, remove it
                self.cache.cache_list.remove(block_to_delete)  # delete the block in the cache

        else:
            # otherwise convert the instruction to decimal
            dec_instruction = int(current_instruction, 16)
            main_memory_block_number = int(dec_instruction) // self.block_size  # calculate its main memory block number
            cache_block_number = main_memory_block_number % self.cache_size  # calculate its cache block number
            # if the main memory block number is already present in the cache then add one to the hit count
            if self.cache.cache_list[cache_block_number] == main_memory_block_number:
                self.hits += 1

            else:
            # if its not in the list add one to the miss count and bring the main memory block number into its cache block number in the cache list
                self.miss += 1
                self.cache.bring_block(main_memory_block_number, cache_block_number)

    # subroutine to calculate the hit ratio
    def calculate_ratio(self):
        hit_ratio = self.hits / (self.hits + self.miss)
        return(f"{hit_ratio:.3f}")  # returns the hit ratio in 3 decimal places


# Cache class - creates the cache list and brings blocks from the main memory into cache
class Cache:
    # initialize the class
    def __init__(self, dec_cache_size):
        self.cache_size = dec_cache_size
        self.cache_list = []
        self.create_cache_list() # allows the list to be accessible from the CPU class

    # subroutine creates a cache list and sets all empty spaces to none
    def create_cache_list(self):
        self.cache_list = [None] * self.cache_size

    # subroutine brings blocks from the main memory to the cache
    def bring_block(self, main_memory_block_number, cache_block_number):
        self.cache_list[cache_block_number] = main_memory_block_number  # places the main memory block number in the correct cache block number


##MAIN##
input_file = ("sample0.txt")  # set the input file to a variable
with open(input_file, 'r') as f:  # open the input file and read the lines
    lines = f.readlines()

    configure = lines[0].strip().split()  # taking the 2 numbers from the first line
    dec_block_size = int(configure[0], 16)  # number of words/instructions per block
    dec_cache_size = int(configure[1], 16)  # number of blocks in the cache
    cache = Cache(dec_cache_size)  # set the cache class with the decimal cache size to a variable
    cpu = CPU(dec_block_size, dec_cache_size, cache)  # do the same for the CPU
    count = 0  # initialize the count for how many instructions are executed
    for line in lines[1:]:  # for the instructions skipping the first line
        current_instruction = line.strip()  # strip the instruction
        cpu.execute_instruction(current_instruction)  # call the execute instruction subroutine from the CPU class and pass through the current instruction
        count += 1  # increase the count plus 1
        if count % 100 == 0:  # print the statements if the count is 100
            print(f'instruction# - {count}')
            print(f'H - {cpu.calculate_ratio()}')
            templist = [i if i is not None else '-----' for i in cache.cache_list]  # gets rid of the parentheses surrounding (none) in the list and swaps it with -----
            for i in templist:
                print(f"  {i}  ", end="")
            print()

