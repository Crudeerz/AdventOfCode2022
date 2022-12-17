import string

lowerCase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)

def Solve3(): 
    comp, comp1, comp2, tot = [],'','', 0
    with open('Day 3\Day 3 input.txt') as f:
        rucksack = f.readlines()
        for item in rucksack:
            item = item.strip('\n')
            comp1 = item[:len(item)//2]
            comp2 = item[len(item)//2:]
            for i in comp1:
                if i in comp2:
                    comp.append(i)
                    if i in lowerCase:
                        tot += lowerCase.index(i) + 1
                        break
                    else:
                        tot += uppercase.index(i) + 27
                        break
        #print(comp)
        print(tot)
                    
                    
def main():
    Solve3()
    
if __name__ == "__main__":
    main()