def find_intersections(input_radians_identifiers):

    n = len(input_radians_identifiers[0])
    if n==0 or n%2!=0:
        print('Invalid test case')
        return 0
    
    active_chords_bv = 0 #integer for maintaining active chords (use by bitwise operations)
    chord_ranks = {} # hashmap for maintaing rank of the given chords
    total_chords = 0 # total number of chords parset
    intersections = 0

    # Assigning rank to each chord
    for i in range(n-1, -1, -1):
        
        identifier = input_radians_identifiers[1][i]
        if identifier[0] == 's':
            chord_ranks[identifier] = total_chords
            total_chords+=1

    for i in range(n):
        
        identifier = input_radians_identifiers[1][i]
        
        if identifier[0] == 's':
            rank = chord_ranks[identifier]
            active_chords_bv |= 1<<rank # set bit at 'rank' to 1 (similar to adding current chord as an active_chord)
        
        else:
            sx_identifier = 's'+input_radians_identifiers[1][i][-1]
            ac_rank = chord_ranks[sx_identifier]
            intersections += count_bits_to_right(active_chords_bv, ac_rank+1) #counting number of bits from the right of the rank bit
            active_chords_bv &= ~(1<<ac_rank) # setting the bit at 'rank' to 0 (similar to removing current chord from active_chord)
    
    return intersections

## function to count bits to the right of current bits
def count_bits_to_right(num, i):
    bit_mask = (1<<(i -1))-1
    bits_to_right = num & bit_mask
    if bits_to_right == 0:
        return 0
    return int.bit_count(bits_to_right)

if __name__ =='__main__':
    input_radians_identifiers = [('0.78', '1.47', '1.77', '1.99'), ('s1', 's2', 'e1','e2')]
    intersections = find_intersections(input_radians_identifiers)
    print(intersections)
