def index_all(search_list, item):
    print(search_list)
    indices = []
    for i in range(len(search_list)):
        if search_list[i] == item:
            indices.append([i])
        elif isinstance(search_list[i], list):
            for index in index_all(search_list[i], item):
                indices.append([i]+index)
    return indices


b = [[1,2,3],[2,3,4,[2,3,4,5]],[3,2,1]]
print(index_all(b, 2))


