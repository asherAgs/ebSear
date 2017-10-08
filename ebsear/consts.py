SITE_URL = 'https://www.ebay.com'
SEARCH_URL = '%s/sch/i.html?_from=R40&_sacat=0&_nkw=%s&_pgn=%s&_skc=%s&rt=nc' #base, search, page_num, num_results
DEFAULT_NUM_RESULTS = 50

BASE_URL = SEARCH_URL % (SITE_URL,'%s','%s','%s')
ALT_BASE_URL = SEARCH_URL
UPLOAD_URL = 'https://rover.ebay.com/rover/1/710-53481-19255-0/1?icep_id=114&ipn=icep&toolid=20004&campid=5338189521&mpre=%s'


OUT_URL_TAG = '&tag=alhsabc-20'
OUT_URL_REF = '/ref=as_li_tl?tag=alhsabc-20'
URL_HEADERS = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
