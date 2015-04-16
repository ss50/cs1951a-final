import sys

if __name__ == '__main__':
	f = open(sys.argv[1],'r')
	out = open(sys.argv[2], 'w+')
	for line in f:
		out.write(line.replace("\\\"",""))