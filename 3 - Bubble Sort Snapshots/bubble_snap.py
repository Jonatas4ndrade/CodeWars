def bubble(arr):
    done_flag = False
    snapshots = []
    arr_len = len(arr) # counts just once, used every loop.
    global_counter = 1
    
    while not done_flag:
        done_flag = True
        
        for count, value in enumerate(arr):     
            
            #Last numbers already sorted, break.
            if count ==  arr_len - global_counter:
                 break
                
            #If first is bigger, swaps and set flag to false.
            if value > arr[count + 1]:
                arr[count], arr[count+1] = arr[count+1], arr[count]
                snapshots.append(arr[:])
                done_flag = False
                
        #No swaps made, sorting is done.
        if done_flag:
            return snapshots
            
        global_counter += 1