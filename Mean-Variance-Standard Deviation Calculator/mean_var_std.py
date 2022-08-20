import numpy as np


def calculate(input_list):
    # throwing error if list does not have 9 elements
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")

    # converting input list of 9 elements into 3x3 matrix
    input_array = np.array([
        [input_list[0], input_list[1], input_list[2]],
        [input_list[3], input_list[4], input_list[5]],
        [input_list[6], input_list[7], input_list[8]]
    ])

    # mean values of columns, rows & flattened matrix in that order
    mean_col = [input_array[:, 0].mean(), input_array[:, 1].mean(), input_array[:, 2].mean()]
    mean_row = [input_array[0].mean(), input_array[1].mean(), input_array[2].mean()]
    mean_flat = input_array.mean()
    mean_list = [mean_col, mean_row, mean_flat]

    # variance values of columns, rows & flattened matrix in that order
    var_col = [input_array[:, 0].var(), input_array[:, 1].var(), input_array[:, 2].var()]
    var_row = [input_array[0].var(), input_array[1].var(), input_array[2].var()]
    var_flat = input_array.var()
    var_list = [var_col, var_row, var_flat]

    # standard deviation values of columns, rows & flattened matrix in that order
    std_col = [input_array[:, 0].std(), input_array[:, 1].std(), input_array[:, 2].std()]
    std_row = [input_array[0].std(), input_array[1].std(), input_array[2].std()]
    std_flat = input_array.std()
    std_list = [std_col, std_row, std_flat]

    # max values of columns, rows & flattened matrix in that order
    max_col = [input_array[:, 0].max(), input_array[:, 1].max(), input_array[:, 2].max()]
    max_row = [input_array[0].max(), input_array[1].max(), input_array[2].max()]
    max_flat = input_array.max()
    max_list = [max_col, max_row, max_flat]

    # min values of columns, rows & flattened matrix in that order
    min_col = [input_array[:, 0].min(), input_array[:, 1].min(), input_array[:, 2].min()]
    min_row = [input_array[0].min(), input_array[1].min(), input_array[2].min()]
    min_flat = input_array.min()
    min_list = [min_col, min_row, min_flat]

    # sum values of columns, rows & flattened matrix in that order
    sum_col = [input_array[:, 0].sum(), input_array[:, 1].sum(), input_array[:, 2].sum()]
    sum_row = [input_array[0].sum(), input_array[1].sum(), input_array[2].sum()]
    sum_flat = input_array.sum()
    sum_list = [sum_col, sum_row, sum_flat]

    # dictionary collecting all value lists for output of function
    output_dictionary = {
        "mean": mean_list, "variance": var_list, "standard deviation": std_list,
        "max": max_list, "min": min_list, "sum": sum_list
    }

    return output_dictionary