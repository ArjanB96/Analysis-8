import random

def generate_checksum_id():
    '''
    creates a random checksum id that can't start with 0 and is a string of 10 random digits. 
    The last digit on the right is a checksum which must be equal to the remainder of the sum of the first 9 digits by 10
    '''
    checksum_id = str(random.randint(1, 9))
    for i in range(8):
        checksum_id += str(random.randint(0, 9))

    sum = 0
    for i in range(len(checksum_id)):
        sum += int(checksum_id[i])

    checksum_id += str(sum % 10)

    return checksum_id