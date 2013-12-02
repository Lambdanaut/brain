# This file has nothing to do with the rest of this source tree
# It doesn't even impliment A* correctly
# Me putting it here is a blatant disregard for engineering practices
# And a blatant excercise of silliness

from __future__ import division
from math import sqrt

world = [
['.','|','.','|','.','|','.','.','.','.'],
['.','|','.','|','.','|','.','|','.','.'],
['.','.','.','|','.','.','.','.','.','.'],
['.','.','.','|','.','|','.','|','.','.'],
['.','|','.','|','.','|','.','.','.','.'],
['.','|','.','|','.','|','.','|','.','.'],
['.','|','.','|','.','|','.','.','.','.'],
['.','|','.','|','.','.','.','.','.','.'],
['.','|','.','|','.','.','.','|','|','|'],
['.','|','.','|','.','|','.','.','.','.'],
['.','|','.','|','.','|','.','.','.','.'],
['.','|','.','|','.','|','.','|','.','.'],
['.','|','.','|','.','|','.','.','.','.'],
['.','|','.','|','.','|','.','.','.','.'],
['.','|','.','.','.','|','.','|','.','.'],
]
START_POINT = (0,0)
END_POINT = (2,14)

def draw_world():
	for y in world:
		to_print = ''
		for x in y:
			to_print += '{} '.format(x)
		print to_print

def in_bounds(point):
	point_x, point_y = point
	if len(world) <= point_y: return False
	elif len(world[0]) <= point_x: return False
	elif 0 > point_x: return False
	elif 0 > point_y: return False
	return True

def get_point(point):
	point_x, point_y = point
	return world[point_y][point_x]

def get_adjacents(point):
	""" Returns a list of points adjacent to the point given """
	point_x, point_y = point
	relative_points = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if (x, y) != (0, 0)]
	adjacent_points = map(lambda (adj_x, adj_y): (adj_x + point_x, adj_y + point_y), relative_points)
	bounded_adjacent_points = filter(lambda adj_point: in_bounds(adj_point), adjacent_points)
	return bounded_adjacent_points

def g_score(point1, point2):
	""" Diagonal paths take longer """
	x1, y1 = point1
	x2, y2 = point2
	return 1.4 if x1 != x2 and y1 != y2 else 1.0

def h_score(point1, point2):
	""" Planar distance formula """
	x1, y1 = point1
	x2, y2 = point2
	return sqrt( (x2 - x1)**2 + (y2 - y1)**2)

def walkable_score(char):
	if char == '.':
		return 0
	if char == '|':
		return 10
	else:
		return 10

def astar(start_point, end_point): 
	""" Finds the quickest route between two points """

	def compare_f_scores(point1, point2):
		""" Returns the astar point with the lower f_score """
		(s, p, g, h, w, f) = point1
		(s2,p2,g2,h2,w2,f2) = point2
		print str(f) + "  " + str(f2)
		if f < f2: 
			print "We chose: " + str(f)
			return point1
		else:
			print "We chose: " + str(f2)
			return point2

	# Add starting point to open list
	open_list = [(start_point, start_point, 0, 0, 0, 0)]
	closed_list = []
	while True:
		if not open_list:
			print "Open list is empty"
			raise Exception
		open_list = sorted(open_list, key = lambda point: point[2])
		cur_node = open_list.pop(0)
		cur_point, cur_parent, cur_g, cur_h, cur_w, cur_f = cur_node
		closed_list.append( (cur_point, cur_parent) )
		if cur_point == end_point:
			# We're done
			break
		open_list_points = map(lambda point: point[0], open_list)
		closed_list_points = map(lambda point: point[0], closed_list)
		adjacents = get_adjacents(cur_point)
		for adjacent in adjacents:
			if adjacent in closed_list_points:
				continue
			g = g_score(cur_point, adjacent)
			h = h_score(adjacent, end_point)
			w = walkable_score(get_point(adjacent))
			f = g + h + w
			new_adjacent_node = (
				adjacent,
				cur_point,
				g, h, w, f
			)
			if adjacent not in open_list_points:
				open_list.append(new_adjacent_node)
			else: 
				previous_adjacent_index = open_list_points.index(adjacent)
				previous_adjacent = open_list[previous_adjacent_index]
				previous_adjacent_g = previous_adjacent[2]
				if cur_g < previous_adjacent_g: 
					open_list[previous_adjacent_index] = new_adjacent_node

	# Found the path
	path = []
	cur_node = (cur_point, cur_parent)
	closed_list_points = map(lambda point: point[0], closed_list)
	while True:
		print cur_node
		cur_point, cur_parent = cur_node
		if cur_node[0] == start_point:
			break

		path.append(cur_point)

		parent_index = closed_list_points.index(cur_point) 
		cur_node = closed_list[parent_index]

	path.reverse()
	return path


if __name__ == "__main__":
	print "AStar"
	print "==============="
	print "Map width: {}".format(len(world[0]))
	print "Map height: {}".format(len(world))
	draw_world()
	astar(START_POINT, END_POINT)
	raw_input("Press enter to end")