#!/usr/bin/env python



def main():
	# Access conf file by config[key] after loading file
    # config = {}
    # execfile("./ignore_files/project.conf", config)
    graph = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]


    graph2 = [[1, 1, 0],
        [0, 1, 0],
        [0, 0, 0]]

    print count_islands(graph)
    print "Main function ran!"


def count_islands(graph):
	visited_cells = {}
	count = 0
	num_rows = len(graph)
	num_cols = len(graph[0])


	for i in range(num_rows):
		for j in range(num_cols):
			if is_one(i, j, graph, visited_cells):
				find_island(i, j, visited_cells, graph)
				count += 1
	return count


def find_island(i, j, visited_cells, graph):
	#find additional island pieces assuming inputed i,j = 1

	row_check = [-1, -1, -1, 0, 0, 1, 1, 1]
	col_check = [1, 0, -1, 1, -1, 1, 0, -1]
	visited_cells[(i,j)] = True


	for k in range(len(row_check)):
		new_row_coordinates = i+row_check[k]
		new_col_coordinates = j+col_check[k]
		if (is_one(new_row_coordinates, new_col_coordinates, graph, visited_cells)) and not (visited_cells.get((new_row_coordinates, new_col_coordinates), False)):
			find_island(new_row_coordinates, new_col_coordinates, visited_cells, graph)



def is_one(i,j,graph, visited_cells):

	if i>=0 and j>=0 and i<len(graph) and j<len(graph[0]) and not visited_cells.get((i,j), False) and graph[i][j]==1 :
		return True
	else:
		return False


