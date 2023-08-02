
def select_sections(occupancy_probability):
    """
    Find a list of sections to be removed from each row in 
    occupancy_probability such that the sum of the probability of each section
    in the list is the minimum

    Approach Description:
    I have implemented memo table as an adjacency matrix where memo_table[i][j]
    contains a tuple (a,b) where a is min total occupancy probability from 
    0 to i including occupancy_probability[i][j], b is the column number of 
    previous row that is included in order to obtain a. The b will be used for 
    backtracking to obtain sections_location.

    To find a, we need to consider min total occupancy probability from 0 to 
    i-1 for the sections in the previous row that are in the same or adjacent 
    columns of j, and choose the section that has the least min total occupancy
    probability among these sections.
    
    Hence, the recurrence relation is:
        Base case: When i = 0
        General case: When i > 0, j >= 0
            if i > 0, j = 0
            memo_table[i][j] = occupancy_probability[i][j] + min(
                memo_table[i-1][j], memo_table[i-1][j+1])

            if i > 0, j = len(occupancy_probability)-1,
            memo_table[i][j] = occupancy_probability[i][j] + min(
                memo_table[i-1][j], memo_table[i-1][j-1])

            if i > 0, j > 0 and j < len(occupancy_probability)-1,
            memo_table[i][j] = occupancy_probability[i][j] + min(
                memo_table[i-1][j], memo_table[i-1][j-1], memo_table[i-1][j+1])
    
    :Input:
        occupancy_probability: a list of lists where 
                               occupancy_probability[i][j] is an integer 
                               between 0 to 100
    
    :Output/Return: a list where the first item is an integer that represents
                    the minimum total occupancy for the selected n sections to
                    be removed and the second item is a list of tuples, each
                    corresponds to the location of one section selected for 
                    removal in occupancy_probability

    :Time complexity: O(nm) where n is the number of rows, and m is the number
                      of columns
    :Space complexity: O(nm)
    """
    no_row = len(occupancy_probability)     # n
    no_col = len(occupancy_probability[0])  # m

    # create a memo table of n x m 
    memo_table = [None] * no_row

    for row in range(len(memo_table)):
        memo_table[row] = [(-1, -1)] * no_col

    # add first row into memo table
    for col in range(len(memo_table[0])):
        memo_table[0][col] = (occupancy_probability[0][col], -1)

    # for each row and each column, find the min total probability 
    # including occupancy_probability[row][column]
    for row in range(1, len(occupancy_probability)):
        for col in range(len(occupancy_probability[row])):
            current_prob = occupancy_probability[row][col]
            
            prev_prob_same = memo_table[row-1][col][0]

            current_min = (prev_prob_same, col)

            # if there is left adjacent column in previous row
            if col != 0:
                prev_prob_left = memo_table[row-1][col-1][0]

                if prev_prob_left < current_min[0]:
                    current_min = (prev_prob_left, col-1)
            
            # if there is right adjacent column in previous row
            if col != no_col-1:
                prev_prob_right = memo_table[row-1][col+1][0]

                if prev_prob_right < current_min[0]:
                    current_min = (prev_prob_right, col+1)

            memo_table[row][col] = (current_min[0]+current_prob, 
                                    current_min[1])
    
    # find the column that has min toal occupancy probability from last row
    min_col = 0

    for col in range(1, no_col):
        if memo_table[no_row-1][col] < memo_table[no_row-1][min_col]:
            min_col = col

    # get the minimum occupancy probability
    min_total_occupancy = memo_table[no_row-1][min_col][0]

    # backtrack to get the sections to be removed
    sections_location = []
    row = no_row - 1
    col = min_col
    previous = col
    while row >= 0:
        sections_location.append((row, col))
        previous = memo_table[row][col][1]
        row -= 1
        col = previous

    # reverse list
    for i in range(len(sections_location)//2):
        sections_location[i], sections_location[len(sections_location)-i-1] = \
            sections_location[len(sections_location)-i-1], sections_location[i]

    return [min_total_occupancy, sections_location]
