import re
def valid_or_not(password):
    ''' password is a string
        Output -> The function is expected to be returning a string one of:
         Valid Password / Invalid Password'''

    # YOUR CODE GOES HERE
    if re.search(r"\s+",password) is not None:
        return "Invalid Password"
    if re.search(r"[A-Za-z]+",password) is None:
        return "Invalid Password"
    if re.search(r"[0-9]+",password) is None:
        return "Invalid Password"
    if re.search(r"[$#@]+",password) is None:
        return "Invalid Password"
    if len(password)<8:
        return "Invalid Password"

    return 'Valid Password'
