def solution(data):
	def convert_data(date):
		if '-' in date:
			day, month, year = date.split('-')
		elif '/' in date:
			month, day, year = date.split('/')
		else:
			year, month, day = date.split('.')
		return year, month, day
	converted_date = [convert_data(i) for i in data]
	sorted_date = sorted(converted_date)
	return ["/".join(date) for date in sorted_date]