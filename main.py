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
#~ CSV_INPUT = "/home/trent/DATA.CSV"
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
		r.append(i[num_field])
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
	name = CSV_INPUT
	print name
	print PATH + "DATA." + get_time() + "CSV"
	
if __name__ == "__main__":
	data = open_data()
	update()
	#~ for i in data:
		#~ print i
	save_data(data)
	mv()
	
	#~ exit(0)

	parser = OptionParser()
	parser.add_option("-d", "--day", dest="DAY", default="0")
	parser.add_option(
		"-l",
		"--list",
		action="store_true",
		dest="LIST",
		help="list raw data without display graph")
	(options, args) = parser.parse_args()
	day = int(options.DAY)
	data = data [-144 * day : ]
	b_list = options.LIST if options.LIST is not None else False
	if b_list:
		for i in data:
			print i
		exit(0)

	# Create a new subplot from a grid of 3x1
	plt.subplot(311)
	
	plt.ylabel("frigo")
	plt.grid(True)
	abscisse = datettimetox(data)
	plt.plot(abscisse, select_one_field(data, 2), color="blue", linewidth=1.0, linestyle="-")
	plt.legend(loc='upper left', frameon=False)
	
	plt.subplot(312)
	plt.ylabel("exterieur")
	plt.grid(True)
	plt.plot(abscisse, select_one_field(data, 4), color="red", linewidth=1.0, linestyle="-")
	plt.legend(loc='upper left', frameon=False)

	plt.subplot(313)
	plt.ylabel("humidite")
	plt.plot(abscisse, select_one_field(data, 1), color="blue", linewidth=1.0, linestyle="-", label="h_frigo")
	plt.plot(abscisse, select_one_field(data, 3), color="red", linewidth=1.0, linestyle="-", label="h_dehors")
	plt.legend(loc='upper left', frameon=False)

	plt.show()