nums = [eval(i) for i in input().split(" ")]
speed_limit, bessie_limit = [], []
for i in range(nums[0]):
	speed_limit.append([eval(i) for i in input().split(" ")])
for i in range(nums[1]):
	bessie_limit.append([eval(i) for i in input().split(" ")])

speed_change, bessie_change = [], []
prev_val = 0
for i in speed_limit:
	speed_change.append(i[0] + prev_val)
	prev_val = i[0] + prev_val

prev_val = 0
for i in bessie_limit:
	bessie_change.append(i[0] + prev_val)
	if not i[0] + prev_val in speed_change:
		speed_change.append(i[0] + prev_val)
	prev_val = i[0] + prev_val

max_over = 0
for i in range(len(speed_change)):
	index = 0
	for x in range(len(speed_change)):
		if speed_change[i] > speed_change[x]:
			index += 1
		else:
			break
	speed = speed_limit[index][1]
	index = 0
	for x in range(len(bessie_change)):
		if speed_change[i] > bessie_change[x]:
			index += 1
		else:
			break
	if bessie_limit[index][1] - speed > max_over:
		max_over = bessie_limit[index][1] - speed

print(f"Speed Is Over By {max_over}")
