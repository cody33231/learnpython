def mintohour(min):
	hour = divmod(int(min),60)
	return str(hour[0])+'h'+str(hour[1])+'min'

if __name__ == '__main__':
	while True:
		miniute = raw_input('Please enter minute(q to quit):')
		if miniute == 'q':
			break
		else:
			print mintohour(miniute)