#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import datetime
import zlib
import cPickle
from optparse import OptionParser
import os

PATH = "/media/trent/3832-6331/"
CSV_INPUT = PATH + "/DATA.CSV"
DATA_FILE = "data.txt"
data = []
index = []

def create_index(d):
	for i in d:
		index.append(i[0])
		
def concatdatettime(d, t):
	return d + '.' + t.replace(':', '.')
	
def datettimetox(data):
	#~ day.month.year
	#~ datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]])
	r = []
	for i in data:
		ds = i[0].split('.')
		r.append(datetime.datetime(int(ds[2]),int(ds[1]),int(ds[0]), int(ds[3]), int(ds[4]), int(ds[5]) ))
	return r
		
def update():
	print "creation de l'index..."
	create_index(data)
	print "Ouverture de %s" % CSV_INPUT
	try:
		fd = open(CSV_INPUT)
	except:
		print "Erreur lors de l'ouverture de %s" % CSV_INPUT
		return
	raw = fd.readlines()
	fd.close()
	for i in raw:
		field = i.replace('\r\n', '').split(',')
		dt = concatdatettime(field[0], field[1])
		if field[0] == 'date' or field[2] == 'nan' or dt in index:
			continue
		field.pop(0)
		field[0] = dt
		data.append(field)

def save_data(d):
	fd = open(DATA_FILE, "w")
	compressed = zlib.compress(cPickle.dumps(d))
	fd.write(zlib.compress(cPickle.dumps(d)))
	fd.close()
	
def open_data():
	print "Ouverture de %s" % DATA_FILE
	try:
		fd = open(DATA_FILE)
	except:
		print "Erreur lors de l'ouverture de %s" % DATA_FILE
		return []
	r = cPickle.loads(zlib.decompress(fd.read()))
	fd.close()
	return r
	
def select_one_field(d, num_field):
	r = []
	for i in d:
		r.append(float(i[num_field]))
	return r

def get_time():
	r = ""
	cpt = 0
	for i in datetime.datetime.now().timetuple():
		r += str(i) + '.'
		cpt += 1
		if cpt > 5:
			return r

def mv():
	try:
		os.rename(CSV_INPUT, PATH + "DATA." + get_time() + "CSV")
	except:
		print "rename fail."
		
def main_io():
	global data 
	data = open_data()
	update()
	save_data(data)
	mv()
	
def normal_display():
	
	# Create a new subplot from a grid of 3x1
	plt.subplot(311)
	abscisse = datettimetox(data)
	legend = 'right'
	
	plt.ylabel("exterieur")
	plt.grid(True)
	plt.plot(abscisse, select_one_field(data, 4), color="red", linewidth=1.0, linestyle="-")
	plt.legend(loc='upper left', frameon=False)
	ax = plt.gca()
	ax.yaxis.set_ticks_position(legend)
	
	plt.subplot(312)
	plt.ylabel("frigo")
	plt.grid(True)
	plt.plot(abscisse, select_one_field(data, 2), color="blue", linewidth=1.0, linestyle="-")
	plt.legend(loc='upper left', frameon=False)
	ax = plt.gca()
	ax.yaxis.set_ticks_position(legend)
	
	plt.subplot(313)
	plt.ylabel("humidite")
	plt.plot(abscisse, select_one_field(data, 1), color="blue", linewidth=1.0, linestyle="-", label="h_frigo")
	plt.plot(abscisse, select_one_field(data, 3), color="red", linewidth=1.0, linestyle="-", label="h_dehors")
	plt.legend(loc='upper left', frameon=False)
	ax = plt.gca()
	ax.yaxis.set_ticks_position(legend)

	plt.show()

def display_minmax():
	ordonne = select_one_field(data, 4)
	days, l = split_by_day(ordonne)
	abscisse = datettimetox(days)
	
	# Create a new subplot from a grid of 2x1
	plt.subplot(211)
	legend = 'right'

	plt.ylabel("exterieur")
	plt.grid(True)
	plt.plot(abscisse, max_list(l),  color="red", linewidth=1.0, linestyle="-")
	plt.plot(abscisse, min_list(l),  color="blue", linewidth=1.0, linestyle="-")
	plt.legend(loc='upper left', frameon=False)
	ax = plt.gca()
	ax.yaxis.set_ticks_position(legend)
	
	
	ordonne = select_one_field(data, 2)
	days, l = split_by_day(ordonne)
	print l
	print max_list(l)
	print min_list(l)
	plt.subplot(212)
	plt.ylabel("frigo")
	plt.grid(True)
	plt.plot(abscisse, max_list(l),  color="red", linewidth=1.0, linestyle="-")
	plt.plot(abscisse, min_list(l),  color="blue", linewidth=1.0, linestyle="-")
	plt.legend(loc='upper left', frameon=False)
	ax = plt.gca()
	ax.yaxis.set_ticks_position(legend)
	
	plt.show()

def max_list(l):
	r = []
	for i in l:
		r.append(max(i))
	return r

def min_list(l):
	r = []
	for i in l:
		r.append(min(i))
	return r
	
def split_by_day(l):
	global data
	r = []
	tmp = []
	days = []
	prev = ''
	cpt = 0
	for i in data:
		if i[0][:10] != prev:
			if len(tmp) > 0:
				days.append( [ i[0][:10] + '.00.00.00' ])
				r.append(tmp)
			tmp = []
			prev = i[0][:10]
		tmp.append(l[cpt])
		cpt += 1
	return days, r

if __name__ == "__main__":
	
	parser = OptionParser()
	parser.add_option("-d", "--day", dest="DAY", default="0")
	parser.add_option("-f", "--file", dest="FILE", default=CSV_INPUT)
	parser.add_option("-o", "--file_output", dest="FILE_OUTPUT", default=DATA_FILE)
	parser.add_option(
		"-l",
		"--list",
		action="store_true",
		dest="LIST",
		help="list raw data without display graph")
	parser.add_option(
		"-m",
		"--minmax",
		action="store_true",
		dest="MINMAX",
		help="display only minimum and maximum by day")
	
	(options, args) = parser.parse_args()
	day = int(options.DAY)
	CSV_INPUT = options.FILE
	DATA_FILE = options.FILE_OUTPUT
	b_list = options.LIST if options.LIST is not None else False
	minmax = options.MINMAX if options.MINMAX is not None else False	

	main_io()
	data = data [-144 * day : ]
	
	if b_list:
		for i in data:
			print i
		exit(0)

	if minmax:
		display_minmax()
	else:
		normal_display()
