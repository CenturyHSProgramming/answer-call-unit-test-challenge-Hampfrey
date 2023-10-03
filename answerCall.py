# answerCall.py
# by Mottern

# For instructions on what to do, see README.md
# or visit (https://github.com/HundredVisionsGuy/answerCall)

# Write function defintion: answerCall()
def answerCall(caller_code, sameAreaCode, cur_time):
    """
    This function processes whether or not a caller with a specific set of 
    parameters should be ansered.
    
    Args:
        caller_code (str): The identification of the caller, the IDs are as 
                           follows, "U" = unknown, "F" = friend, "R" = relative, 
                           and "T" = telemarketer.
        sameAreaCode (bool): If the caller is from the same area as you.
        cur_time (str): the current time in 24 hr format.
    
    Return:
        (bool): If the caller should be answered.
    """
    # Convert time
    if len(cur_time) == 5:
        hour = int(cur_time[0] + cur_time[1])
        minute = int(cur_time[3] + cur_time[4])
    else:
        hour = int(cur_time[0])
        minute = int(cur_time[2] + cur_time[3])
    time = hour * 60 + minute

    # Time automatic rejects
    if time < 420 or time > 1320:
        return False
    
    # Caller ID automatic rejects
    if caller_code == "T":
        return False
    
    # Caller ID automatic passes
    if caller_code == "F" or caller_code == "R":
        return True
    
    # Process unknown caller IDs
    if sameAreaCode == False:
        return False
    else:
        return True

if __name__ == '__main__':
    pass # remove or comment out this line if you wish to test the function
