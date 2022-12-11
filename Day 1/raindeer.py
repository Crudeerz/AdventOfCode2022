

def Calories():
    elf, elves = [], []
    with open('Day 1\input.txt') as f:
        # Loop through each line in the file
        # Add the line to the elf array
        # If the line is empty, add the elf list to the elves list
        for line in f:
            if line.strip() == '':
                elves.append(elf)
                elf = []
            else:
                elf.append(int(line.strip()))
        elves.append(elf)
    

     # Find the max sum of the elves
    max_sum = 0
    elfnum = 1
    for elf in elves:
        # Find the total sum of the elf
        total_sum = sum(elf)
        
        # If the total sum is greater than the max sum, update the max sum
        if total_sum > max_sum:
            max_sum = total_sum
            elfnum = elfnum + 1
    print("ELf number" , elfnum, "is carrying the most calories, a total of", max_sum,"calories")


def main(): 
    Calories()

if __name__ == "__main__":
    main()