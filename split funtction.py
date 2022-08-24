abc = 'With three words'
threewordssplitup = abc.split()
#The split function split up the three word "With three words" into 3 SEPARATE STRINGS into a list

print(threewordssplitup)
#returns ['With', 'three', words']

print(len(threewordssplitup))
#returns the length which is 3 because there are 3 strings in the list

print(threewordssplitup[0])
#returns index zero of this list ['With', 'three', words'] which is the word WITH