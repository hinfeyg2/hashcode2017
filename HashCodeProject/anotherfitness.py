import ReadGoogle

data = ReadGoogle.ReadGoogle("../tests/input/smallset.in")
sample = [[2], [3,1], [0,1]]
def fitness(solution):

	print(data["number_of_videos"])
	print(data["number_of_endpoints"])
	print(data["number_of_requests"])
	print(data["number_of_caches"])
	print(data["cache_size"])
	print(data["video_size_desc"])
	print("ep_to_dc_latency")
	print(data["ep_to_dc_latency"])
	print(data["ep_to_cache_latency"])
	# print(data["ed_cache_list"])
	# print(data["video_ed_request"])
	# endpoint to cache connections
	print(data["ed_cache_list"])

	# endpoint video requests
	print(data["video_ed_request"])



	temp = []
	temp2 = []
	solutionavailabletocache = []

	for i in data["ed_cache_list"]:
		solutionavailabletocache.append([])
		for y in i:
			print(solutionavailabletocache[i])
			# .append(solution[y])

	# print(solutionavailabletocache)

	# for i in data["ed_cache_list"]:
	# 	print(i)


	# get list of each endpoint connection

	# for i in data["video_ed_request"]:
	# 	# print("number of video requests")
	# 	# print(data["video_ed_request"][i])
	# 	# print("delay to datacenter")
	# 	# print(data["ep_to_dc_latency"][i[1]])
	# 	# print("")
	# 	temp.append(data["video_ed_request"][i] * data["ep_to_dc_latency"][i[1]])
	# 	temp2.append(data["video_ed_request"][i])		

	# 	print(data["ed_cache_list"][i[1]])
	# 	# print(data["ep_to_dc_latency"][i[1]])




	# print(temp)





# {('3', '0'): '1500', ('0', '1'): '1000', ('4', '0'): '500', ('1', '0'): '1000'}

# [[(1500 * 1000) - (1500 * 300)], [], []




fitness(sample)

# 462500

# is the endpoint connected to a cache
# [[0, 2, 1], []]

# is does the cache have the video in it
# what is the delay of the cache


# {('3', '0'): ['1500'], ('0', '1'): '1000', ('4', '0'): '500', ('1', '0'): '1000'}


# [1500, 300]




# [[{3: 1500}, {4: 500}, {1: 1000}],[{0: 1000}]]
