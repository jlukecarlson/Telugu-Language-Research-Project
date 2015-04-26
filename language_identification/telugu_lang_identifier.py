import sys
print sys.argv

# is_telugu checks if mainly telugu characters
# param s - input string
# output - 0.0 -> 1.0 determining probability of being telugu
def is_telugu(s):
    # ensure input is unicode
    uni = s.decode('utf-8')
    # telugu unicode range
    min_u_val = 3072
    max_u_val = 3199

    num_chars = 0.0
    num_telugu_chars = 0.0

    for t in uni:
        order = ord(t)
        representation = repr(t)
        print representation,order
        # check in range or if it is the space character
        num_telugu_chars += 1 if ((min_u_val <= order <= max_u_val) or (order == 32)) else 0
        num_chars += 1
        
    return num_telugu_chars/num_chars

# input comes from the command. ex
# python telugu_lag_identifier.py "is this telugu?"
is_telugu(sys.argv[1])
