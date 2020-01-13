# python3
import logging

import logging.config

def main():
	'''
	logging.basicConfig(
	filename='app.log',
	level=logging.ERROR,
	format='%(levelname)s:%(asctime)s:%(message)s')
	'''
	logging.config.fileConfig('config/config.ini')
	logging.getLogger("example02")

	#variables 
	hostname = 'www.python.org'
	item = 'spam'
	filename = 'data.csv'
	mode = 'r'

	# example logging calls
	logging.critical('Host %s unknown', hostname)
	logging.error("Couldn't find %r",item)
	logging.warning('Feature is deprecated')
	logging.info('Opening file %r, mode=%r', filename,mode)
	logging.debug('Got here')


if __name__ == '__main__':
	main()
