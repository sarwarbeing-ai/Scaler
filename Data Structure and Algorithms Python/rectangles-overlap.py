def solve(A, B, C, D, E, F, G, H):
    '''
    Eight integers A, B, C, D, E, F, G, and H represent two rectangles in a 2D plane.
    For the first rectangle, its bottom left corner is (A, B), and the top right corner is (C, D), and for the second rectangle, its bottom left corner is (E, F), and the top right corner is (G, H).

    Find and return whether the two rectangles overlap or not.
    '''
    if F>=D or H<=B:
        return 0
    elif E>=C or G<=A:
        return 0
    else:
        return 1        
