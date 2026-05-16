for i in range(10):    
    for j in range(10):
        print (f"{j+1}x{i+1}={(j+1)*(i+1)}", end="\t")  
        #print (f"{i+1}x{j+1}={(j+1)*(i+1)}", end="\t")      
        
    if ((i + 1)  % 2) == 0 :                
         print()
    #print()