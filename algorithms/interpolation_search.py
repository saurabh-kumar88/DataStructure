# // The idea of formula is to return higher value of pos
# // when element to be searched is closer to arr[hi]. And
# // smaller value when closer to arr[lo]
# pos = lo + [ (x-arr[lo])*(hi-lo) / (arr[hi]-arr[Lo]) ]

# arr[] ==> Array where elements need to be searched
# x     ==> Element to be searched
# lo    ==> Starting index in arr[]
# hi    ==> Ending index in arr[]


# Algorithm
# Rest of the Interpolation algorithm is the same except the above partition logic.

# Step1: In a loop, calculate the value of “pos” using the probe position formula.
# Step2: If it is a match, return the index of the item, and exit.
# Step3: If the item is less than arr[pos], calculate the probe position of the left sub-array. Otherwise calculate the same in the right sub-array.
# Step4: Repeat until a match is found or the sub-array reduces to zero.




def nearest_mid(input_list, lower_bound_index, upper_bound_index, search_value):
    return lower_bound_index + \
        (upper_bound_index - lower_bound_index) * \
        (search_value - input_list[lower_bound_index]) // \
        (input_list[upper_bound_index] - input_list[lower_bound_index])

def interpolation_search(ordered_list, term):

    size_of_list = len(ordered_list) - 1

    index_of_first_element = 0
    index_of_last_element = size_of_list

    while index_of_first_element <= index_of_last_element:
        mid_point = nearest_mid(ordered_list, index_of_first_element, index_of_last_element, term)

        if mid_point > index_of_last_element or mid_point < index_of_first_element:
            return None

        if ordered_list[mid_point] == term:
            return mid_point

        if term > ordered_list[mid_point]:
            index_of_first_element = mid_point + 1
        else:
            index_of_last_element = mid_point - 1

    if index_of_first_element > index_of_last_element:
        return None


arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47] 

if __name__ == "__main__":
	result = interpolation_search(arr,  35 )

	print( result	)




















