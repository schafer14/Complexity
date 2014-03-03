class FIFO(object):
	def __init__(this):
		this.nextIn = 0
		this.nextOut = 0
		this.data ={}

	def append(this, val):
		this.data[this.nextIn] = val
		this.nextIn += 1

	def pop(this):
		value = this.data.pop(this.nextOut)
		this.nextOut += 1
		return value

