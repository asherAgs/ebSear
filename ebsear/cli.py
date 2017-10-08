try:
	from ebsear.consts import *
	from ebsear.api import getItem,getSearchPage
except ImportError:
	from .consts import *
	from .api import getItem,getSearchPage

import sys
import webbrowser
import pprint

def getKwargs(args):
	options = {'q':False,'d':True,'v':False}
	ignore = []

	for i in range(0,len(args)):
		arg = args[i]
	
		if i not in ignore:
			if args[i] not in ['-p','-i','-q','-d','-v','-u']:
				raise ValueError('Invalid argument')
			else:
				val = args[i][1:]
				if val in ['q','d','v']:
					options[val] = not options[val]	
				else:
					try:
						const = args[i+1]
						if val != 'u':
							const = int(const)
						options[val] = const
						ignore.append(i+1)
					except:
						raise ValueError('Invalid argument')

	translate = {'i':'item_number','p':'page_number','u':'alternate_url',
				 'q':'quiet','d':'open_url','v':'print_all_info'}
	out = {}

	for name,val in options.items():
		out[translate[name]] = val

	return out


def client(query_string,page_number=1,item_number=None,quiet=False,
			open_url=False,print_all_info=False,alternate_url=None):

	if item_number != None:
		(products,url) = getItem(query_string,item_num=item_number,alt_base=alternate_url)
	else: 
		(products,url) = getSearchPage(query_string,page_number,alt_base=alternate_url)

	if open_url:
		webbrowser.open(url)
	if not quiet:	
		printProducts(products,print_all_info)


def printProducts(products,print_all_info=False):
	if not print_all_info:
		print("{: >4} {: <52} {: >9}      {: >5}".format('','Name','Price','Form/Bids'))
	
	for count in sorted(products.keys()):
		if print_all_info:
			pprint.pprint(products[count])
		else:
			## Print info in table format
			price = sorted(products[count]['price']['values'])
			if len(price) > 0:
				price_text = '${:,.2f}'.format(price[0])
			else:
				price_text = ""

			print("{: <4} {: <55}  {: <9}  {: >5}".format(count,products[count]['name'][:55],
				price_text,products[count]['format']))

def run():
	if len(sys.argv) < 2 or sys.argv[1].startswith('-'):
		print("Usage: ebsear query_string [-p num] [-i num] [-u url] [-q] [-v] [-d]")
		exit(1)

	kws = getKwargs(sys.argv[2:])

	query = sys.argv[1]

	client(query,**kws)

if __name__ == '__main__':
	run()
