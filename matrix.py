#!/usr/bin/env python3

# This script intend to search for flowing rivers in a matrix.
# INPUT: 
# Insert row X culumn input for the size of the matrix.
# The script will initialized the matrix with random values of (0 or 1)
# OUTPUT: 
# 1) Print of the generated matrix (with input size and random values)
# 2) Print of the result floating rivers

# Autor: Lior Ben ami
# Date: Jan-2021

__version__ = "1.0"

import random

# Initialize matrix 
matrix = [] 
# Initialize result dict
river_lenth = {}

# Initialized the matrix with random values 
def init_matrix(R, C):
    # For user input 
    for i in range(R):          # A for loop for row entries 
        a =[] 
        for j in range(C):      # A for loop for column entries 
            a.append(random.randrange(0, 2, 1)) 
        matrix.append(a)


def print_matrix(R, C):
    print("\n### the input matrix ###") 
    for i in range(R): 
        for j in range(C): 
            print(matrix[i][j], end = " ") 
        print()

# Search for Horizontal rivers.
# When find one, search for vertical river if exist (from current position)
def search_aurizontal_rivers(R, C):
    lenght = 0
    for i in range(R): 
        if lenght > 0:
            vertical_lenght = search_vertical_rivers(R, C, i-1, C-1)
            if vertical_lenght > 1:
                add_river(vertical_lenght) 
            if lenght > 1 or (vertical_lenght in (0,1) and vertical_lenght != -1):
                add_river(lenght)
            lenght = 0
        for j in range(C):
            if matrix[i][j] == 1:
                lenght+=1
            #I have a river
            elif lenght > 0:
                vertical_lenght = search_vertical_rivers(R, C, i, j-1)
                if vertical_lenght > 1:
                    add_river(vertical_lenght) 
                if lenght > 1 or (vertical_lenght in (0,1) and vertical_lenght != -1):
                    add_river(lenght)
                lenght = 0      
    if lenght > 0:
        add_river(lenght)
        lenght = 0

#Search vertically
def search_vertical_rivers(R, C, i, j):
    vertical_lenght = 0
    #don't search inside a bigger vertical river
    if i > 0 and matrix[i-1][j] == 1:
        return -1
    while i < R:
        if matrix[i][j] == 1:
            vertical_lenght+=1
        else:
            break
        i+=1    
    return vertical_lenght

    

# Add river to result dict
def add_river(lenght):
    if lenght in river_lenth:
        river_lenth[lenght] = river_lenth.get(lenght) + 1
    else:
        river_lenth[lenght] = 1

# Print the result
def print_rivers():
    print("\n### output result ###")
    for key, value in river_lenth.items():
        print("The number of river with lenght: ", key, "is: ", value)

def main():
    R = int(input("Enter the number of rows:")) 
    C = int(input("Enter the number of columns:"))
    init_matrix(R, C)
    print_matrix(R, C)
    search_aurizontal_rivers(R, C)
    print_rivers()

if __name__ == "__main__":
    main()