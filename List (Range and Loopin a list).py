friends = ['Jay', 'Mark', 'AJ', 'HEYA'] #this is just the sample ist LOL

for x in range(len(friends)): 
    # *inside function first than do the outside one*
    #len(friends) = 4   
    # range of 4 = [0, 1, 2, 3] (from the 0 to 3 index)
    #x is the thing that loops through the elements of each string
    
    friend = friends[x]
    #the friend variable is now equal to the "friends" list (from index 0 to 3)
    
    print('Yall ALREADY KNOW THE DEAL:', friend)
    #this returns the string "Yall ALREADY KNOW THE DEAL" + the friend varible (which is the FRIENDS LIST from index 0 to 3)
    
#this will return 
#Yall ALREADY KNOW THE DEAL: Jay
#Yall ALREADY KNOW THE DEAL: Mark
#Yall ALREADY KNOW THE DEAL: AJ
#Yall ALREADY KNOW THE DEAL: HEYA
    
    
