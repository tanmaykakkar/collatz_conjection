'''
    This method add more seq to lookup dict,

    i.e.- seq(10) = [10, 5, 16, 8, 4, 2, 1]
    for this, will store in lookup for {10: [10, 5, 16, 8, 4, 2, 1], 5: [5, 16, 8, 4, 2, 1], ,.. 1:[1] }
'''
def update_lookup_db(lookup_db, col_sequence):
    for i, n in enumerate(col_sequence):
        lookup_db[n] = col_sequence[i:]

'''
    This method tries to find seq in db, partly or fully,
    If found, then reuse that; otherwise generate

    returns a list; collatz sequence- [number...1]
'''
def collatz_sequence(number, lookup_db={}):                                 # creating lookup_db as argument to make sure reusablity of this in different calls
    col_sequence = list()

    '''
        iterate till we either reach to 1 on applying collatz conjection
        repetatively or found seq or part of seq in lookup_db
    '''
    while True:
        if number < 1:
            return []

        elif number in lookup_db:
            col_sequence.extend(lookup_db[number])                          # adding to seq, partially found seq
            break

        elif number == 1:
            return col_sequence + [1]                                       # returns recently found seq with 1

        elif number % 2 == 0:                                               # Even-
            col_sequence.append(number)
            number = number // 2

        else:                                                               # Odd-
            col_sequence.append(number)
            number = (3 * number) + 1

    update_lookup_db(lookup_db, col_sequence)                               # after finding col_seq updating lookup db
    return col_sequence

def max_cycle_count(start, end):
        return max( [(len(collatz_sequence(n)), n,)for n in range(start,end+1)] )