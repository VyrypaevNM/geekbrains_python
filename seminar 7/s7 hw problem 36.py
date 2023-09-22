# print_operation_table = (lambda i, j: for i in range(1,9): print(*([i*j for j in range(1,9)]), sep = "\t" ))
num_rows = 4
num_columns = 5
# print_operation_table
def print_operation_table (operation, num_rows, num_columns):
    return(operation(num_rows,num_columns))

def table(n_rows, n_col):
    for i in range(1,n_rows+1): print(*([i*j for j in range(1,n_col+1)]), sep = "\t" )

print_operation_table(table,4,5)


