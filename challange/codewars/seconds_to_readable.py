# Write a function, which takes a non-negative integer (seconds) as 
# input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.

def make_readable(seconds) :
    
    second,minute,hour = 0,0,0

    if seconds >= 60 :
        second = seconds % 60
    
        minutes = seconds // 60
        
        if minutes >=60 :
            minute = minutes % 60
            
            hour = minutes // 60 
            
        else :
            minute = minutes
    else :
        second = seconds
    if second < 10 :
        second = "0"+str(second)
    if minute < 10 :
        minute = "0"+str(minute)
    if hour < 10 :
        hour = "0"+str(hour)
    return str(hour)+":"+str(minute)+":"+str(second)


print(make_readable(59))



# def make_readable(s):
#     return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)