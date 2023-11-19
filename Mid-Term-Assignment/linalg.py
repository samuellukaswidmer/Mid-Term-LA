def main():
   
    matrix_A = get_input_from_user()
    if matrix_A == None:
        print_sample_matrices()
        exit()
    num_rows = len(matrix_A)
    num_columns = len(matrix_A[0])
    
       
    if not check_if_invertible(num_rows,num_columns,matrix_A):
        exit()
    else:
        
        concatenated_matrix = concatenate_matrix(matrix_A,num_rows,num_columns)
        rows = check_dimensions(concatenated_matrix)
        inverse = calculate_inverse(rows,concatenated_matrix)
        print("This is the resulting inverse: ")
        for row in inverse:
            print(row)

        solution_x = compute_solution(inverse)
        print("This is the solution vector x:")
        for row in solution_x:
            print(row)
    
def compute_sample_inverse(matrix_A):
    num_rows = len(matrix_A)
    num_columns = len(matrix_A[0])
    if not check_if_invertible(num_rows,num_columns,matrix_A):
        return False
    else:
        concatenated_matrix = concatenate_matrix(matrix_A,num_rows,num_columns)
        rows = check_dimensions(concatenated_matrix)
        inverse = calculate_inverse(rows,concatenated_matrix)
        print(f"\nThis is the resulting inverse: ")
        for row in inverse:
            print(row)
        return inverse

def get_input_from_user():
    print_samples = input("Do you want to print the sample matrices? Print y or n: ")
    if print_samples == 'y':
        return None
    length = int(input("How many rows and columns do you want in your square matrix?: "))
    input_matrix = [[0 for i in range(length)]for i in range(length)]
    for i in range(length):
        for j in range(length):
            input_matrix[i][j] = float(input(f"Enter the entry for row {i+1}, column{j+1}: "))
    return input_matrix

def print_sample_matrices(): #Print 10 sample matrices 
    matrix_A = [
    [1,-3,-7],
    [-1,5,6],
    [-1,3,10]
    ]
    matrix_B = [
    [1,2],
    [3,4]
    ]
    matrix_C = [
    [1,1],
    [1,1]
    ]
    matrix_D = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
    ]
    matrix_E = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
    matrix_F = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ]
    matrix_G = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
    ]
    matrix_H = [
    [1,0,0],
    [0,1,0],
    [0,0,1]
    ]
    matrix_I = [
    [1,0,1],
    [0,1,0],
    [1,0,1]
    ]
    matrix_J = [
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1]
    ]
    sample_matrices = [matrix_A,matrix_B,matrix_C,matrix_D,matrix_E,matrix_F,matrix_G,matrix_H,matrix_I,matrix_J]
    for matrix in sample_matrices:
        num_rows = len(matrix)
        num_columns = len(matrix)
        if check_if_invertible(num_rows,num_columns,matrix_A) != False:
            compute_sample_inverse(matrix)
        else:
            print("Matrix is not invertible.")
        
            

def compute_solution(inverse):
    vector_b = [] 
    result = []
    for i in range(len(inverse)):
        vector_b.append(int(input(f"Enter the {i+1} . value of the vector b:"))) 
    print("This is your vector b:", vector_b)
    for i in range(len(inverse)):
        value = 0
        for j in range(len(vector_b)):
            value += inverse[i][j] * vector_b[j]
        result.append([value])
        
    return result
    
    
def check_if_invertible(num_columns,num_rows, matrix):
    if num_columns != num_rows:
        print("\nThis is not a square matrix and therefore doesn't have an inverse (singular).The matrix is therefore singular.")
        return False
    determinant = get_determinant(matrix)
    if determinant == 0:
        print("\nThe provided matrix doesn't have an inverse because its determinant equals zero. The matrix is therefore singular.")
        return False
    return True
    

def check_dimensions(matrix):
    num_rows = len(matrix)  #Number of rows
    num_columns = len(matrix[0]) if matrix else 0  #Number of columns (assuming all rows have the same length)
    
    return num_rows

def calculate_inverse(rows, matrix):

    num_rows = len(matrix)
    num_columns = len(matrix[0])

    i, j = 0, 0    
    while i < num_rows and j < num_columns:
        #Finds a non-zero pivot entry in the column
        if matrix[i][j] == 0:
            non_zero_found = False
            for k in range(i + 1, num_rows):
                if matrix[k][j] != 0:
                    #Swaps the rows to get a non-zero pivot entry
                    matrix[i], matrix[k] = matrix[k], matrix[i]
                    non_zero_found = True
                    break
            if not non_zero_found:
                j += 1  #Moves to the next column
            else:
                #Sets the new pivot entry and increments i
                i += 1
        else:
            if matrix[i][j] != 1:
                divisor = matrix[i][j]
                for col in range(num_columns):
                    matrix[i][col] /= divisor
            #Reduces other rows
            for k in range(num_rows):
                if k != i and matrix[k][j] != 0:
                    multiplier = matrix[k][j]
                    for col in range(num_columns):
                        matrix[k][col] -= multiplier * matrix[i][col]
            
            if i == num_rows - 1 or j == num_columns - 1:
                break
            else:
                i += 1
                j += 1
    
    columns = len(matrix)
    return extract_inverse(matrix, columns)

def concatenate_matrix(matrix,num_rows,num_columns):
    #Creates proper elementary matrix
    i, j = 0, 0
    elementary_matrix = [[0 for j in range(num_columns)]for i in range(num_rows)]
    for i in range(num_columns):
        elementary_matrix[i][i] = 1
    
    #Concatenates elementary matrix to matrix A
    for i in range(num_columns):
        matrix[i] += elementary_matrix[i]
    return matrix

def extract_inverse(matrix,num_columns):
    inverse = [row[(num_columns):] for row in matrix]
    return inverse

def matrix_minor(matrix, i, j):
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]

def get_determinant(matrix):
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    elif size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for j in range(size):
        det += ((-1) ** j) * matrix[0][j] * get_determinant(matrix_minor(matrix, 0, j)) # Source: Gerald Teschl, Susanne Teschl. Mathematik für Informatiker Band 1 (4.Auflage). Heidelberg: Springer Verlag, 2013.
    return det

main()


