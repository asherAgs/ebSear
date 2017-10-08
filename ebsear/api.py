try:
	from ebsear.consts import *
except ImportError:
	from .consts import *

from lxml import html
import requests

try:
	from urllib.parse import quote_plus,quote
except ImportError:
	from urllib import quote_plus,quote
import re
from functools import reduce

def getItem(query_string,item_num,alt_base=''):
	page_num = ((item_num - 1) // DEFAULT_NUM_RESULTS) + 1
	(products,url) = getSearchPage(query_string,page_num=page_num,alt_base=alt_base)

	rel_item_num = ((item_num - 1) % DEFAULT_NUM_RESULTS) + 1

	try:
		item = products[rel_item_num]
	except KeyError:
		return ({},'')

	url = getUploadUrl(item['url'])
	return ({item_num:item},url)


def getSearchPage(query_string,page_num,alt_base=''):
	(cont,url) = getHtmlUrl(query_string,page_num=page_num,alt_base=alt_base)
	products = getProducts(cont)

	url = getUploadUrl(url)
	return (products,url)

def getProducts(content):
	tree = html.fromstring(content)
	products = {}

	#ignores sponsor results
	results = tree.xpath('//ul[@id="ListViewInner"]/li[not(contains(.//a/@href,"pulsar"))]')

	for res in results:
		num = res.xpath('./@r')
		name = res.xpath('.//h3/a/text()')
		prices = res.xpath('.//li[@class="lvprice prc"]//text()')
		url = res.xpath('.//h3/a/@href')

		if all([num,name,prices,url]):
			name = name[0].strip()
			num = int(num[0])
			url = url[0]

			price_text = stripNJoin(prices)
			prices = [getValue(x) for x in prices]
			prices = [x for x in prices if x != None]

			shipping = res.xpath('.//span[@class="ship"]//text()')
			shipping_text = stripNJoin(shipping)
			shipping = [getShipping(shipping_text)]

			subtitle = stripNJoin(res.xpath('.//div[@class="lvsubtitle"]/text()'))
			format_text = stripNJoin(res.xpath('.//li[@class="lvformat"]//text()'))
	
			products[num] = {
				'name' : name,
				'url' : url,
				'price' : {'text': price_text, 'values': prices},
				'shipping': {'text' : shipping_text, 'values' : shipping},
				'subtitle' : subtitle,
				'format' : format_text,
			}

	
	return products

def getHtmlUrl(query_string,page_num=1,alt_base=''):
	url = ''
	results = str(DEFAULT_NUM_RESULTS*(page_num - 1))

	if alt_base:
		if not alt_base.startswith('http'):
			if alt_base.startswith('www'):
				alt_base = 'http://' + alt_base
			else:
				alt_base = 'http://www.' + alt_base

		url = ALT_BASE_URL % (alt_base,quote_plus(query_string),page_num,results)
	else:
		url = BASE_URL % (quote_plus(query_string),page_num,results)

	req = requests.get(url,headers=URL_HEADERS)

	if not req.ok:
		raise ValueError('The requested page could not be found')

	return (req.content.decode('utf8', errors='ignore'),url)

def getUploadUrl(url):
	url = quote(url,safe='')
	return UPLOAD_URL % (url)
	
"""
Clean-ups
"""

def stripNJoin(li):
	return ' '.join([x.strip() for x in li]).strip()

def getValue(price):
	if re.search('\d+(([,.]\d+)|(,\d+\.\d+))?',price):
		val = re.sub(r'[^\d]','',price)
		return int(val)/100

def getShipping(text):
	if not text:
		return 0

	if 'free' in text.lower():
		return 0
	val = getValue(text)
	return val if val else 0
