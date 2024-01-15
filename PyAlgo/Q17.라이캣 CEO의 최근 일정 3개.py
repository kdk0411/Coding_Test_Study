def solution(data):
	all = []
	for day, dates in data.items():
		for date in dates:
			converted_date = f'{date[2:]} {day}'
			all.append(converted_date)
	all.sort(reverse=True)
	return all[:3]