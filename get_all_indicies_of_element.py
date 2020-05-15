# Returns a list of indicies for the given element in the list_to_be_searched, but can be slow
def get_indicies_of_element(list_to_be_searched, element):
    index_list = []
    index = 0
    while True:
        try:
            index = list_to_be_searched.index(element, index)
            index_list.append(index)
            index += 1
        except ValueError as e:
            break
    return index_list
