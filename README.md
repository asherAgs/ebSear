# ebSear

The unofficial Ebay search CLI & API. Search ebay on the command line for free without the need for an API key or any additional setup.


```
$ ebsear 'Air conditioner'
```


```
     Name                                                     Price      Form/Bids
1    Daikin Air Conditioner Wi-Fi Online Controller BRP069A4  $62.90     Buy It Now
2    DC 12V Peltier Semiconductor Refrigeration Pet Air Cond  $14.12     Buy It Now
3    Portable Personal Amazing Air Conditioner Natural Wind   $88.50     Buy It Now
4    Haier 8,000 BTU Electronic Window Air Conditioner AC Un  $199.99    Buy It Now
5    AIR  COND VACUUM PUMP MANIFOLD GAUGE  RATCHED FLARING P  $387.30    Buy It Now
6    Fin Comb For Air Conditioner Blade Cooling Straightenin  $2.79      Buy It Now
7    Daikin Air Conditioner Wi-Fi Online Controller BRP069A4  $61.90     Buy It Now
8    **GENUINE** Air Conditioner Remote Control - Airwell Em  $182.40    Buy It Now
9    New Portable Mute Length 38CM Height 73.6CM Humidifier   $270.88    or Best Offer
10   ACTRON DUCTED AIR CONDITIONER CONTROLLER LEASOM B512GZ   $387.30    Buy It Now
11   Heigth 57CM Portable Evaporative Air Cooler Fan Humidif  $239.83    or Best Offer
12   12,000 BTU 14SEER 1TON Ductless Mini Split Air Conditio  $649.00    or Best Offer
13   24,000 BTU 2TON  Ductless Mini Split Air Conditioner  1  $999.00    Buy It Now
14   24,000 BTU 2TON  Ductless Mini Split Air Conditioner  1  $1,199.00  Buy It Now
15   AC AIR CON WATER CONDENSATE MINI DRAIN PUMP MICRO V AQU  $213.44    Buy It Now
16   LG KELVINATOR AIR CONDITIONER MAIN BOARD  P/N 129091218  $256.13    Buy It Now
17   AIR CONDITIONER DUST PAINT  ROOM FILTER MATERIAL  1x20m  $232.07    Buy It Now
18   18000 BTU 1.5TON  Ductless Mini Split Air Conditioner    $899.00    Buy It Now
19   AIR CONDITIONER TUBE 1/4" 3/8" INSULATED  COPPER PIPE T  $135.83    Buy It Now
20   FUJITSU AOTR09LCC INVERTER OUTDOOR PCB K05CS-05          $349.27    or Best Offer
21   Capacity 7L Portable Evaporative Air Cooler Fan Humidif  $263.11    or Best Offer
22   AIR CONDITIONING AC AIR CON WATER CONDENSATE TANK DRAIN  $89.65     Buy It Now
23   New Portable Mute Length 28.5CM Height 70CM Humidifier   $263.11    or Best Offer
24   18000 BTU 1.5TON  Ductless Mini Split Air Conditioner    $849.00    Buy It Now
25   Portable Mute Length 30.5CM Height 75.5CM Humidifier Pu  $224.31    or Best Offer
...										...									...
```

### Installation

Can easily be be run on Python version 2.7 or greater with minimal additional dependencies (works best on Python3).

Install the dependencies and main package using pip.

```
$ pip install ebsear
```

### Usage

#### CLI
Typing `ebsear` without any additionaly arguments will display the folllowing usage information:

```
Usage: ebsear query_string [-p num] [-i num] [-u url] [-q] [-v] [-d]
```
###### Optional Paratmeters
- `-p num` - Specify the page number to search (defaults to `-p 1`)
- `-i num` - Select the number item to display (relative to the page number)
- `-q` - Disable any printout from occuring on the command line
- `-v` - Display all information scraped (json lines)
- `-d` - Disable the page from opening in your default web browser
- `-u` - Use an alternate base url (for searches on international ebay sites)

##### Examples
```
$ ebsear 'air conditioner' -p 5
```
Display the fifth page in the search


```
$ ebsear 'air conditioner' -i 2
```
Display the second item in the search


```
$ ebsear 'air conditioner' -i 2 -v
```
Display the second item in the search in a json format


```
$ ebsear 'air conditioner' -i 2
```
Display the fifth item in the search


```
$ ebsear 'air conditioner' -u 'ebay.co.uk'
```
Display the first page in the search using "ebay.co.uk"


```
$ ebsear 'air conditioner' -d
```
Display the first page in the search and restrain the page from automatically opening in browser


#### API
The API can be used to make an ebay search query whilst inside a Python script. The main methods `getSearchPage` and `getItem` are the best entry points to use for such cases. These methods will return a tuple of the products (or product) as well as a url to access either the search page (for a search query) or the item page (for a single item query). The products returned from these methods are cleansed and returned in a dictonary containing both the original data and the cleansed data.

```
>>> from ebsear import api
>>> (products,url) = api.getSearchPage('air conditioner',page_num=1)
>>> pprint.pprint(products[1])
{'format': 'Buy It Now',
 'name': 'Daikin Air Conditioner Wi-Fi Online Controller BRP069A43',
 'price': {'text': '$62.90', 'values': [62.9]},
 'shipping': {'text': 'Free international shipping', 'values': [0]},
 'subtitle': 'Brand New',
 'url': 'http://www.ebay.com/itm/Daikin-Air-Conditioner-Wi-Fi-Online-Controller-BRP069A43-/282634166527?epid=15003634367&hash=item41ce4f20ff:g:~yMAAOSwLEtYhMsW'}
```

### About
The idea and implementation for this library was an augmentation of a previous library by the same developer - [amzSear](https://github.com/asherAgs/amzSear).

This library was designed to facilitate the use of an easy command line tool to search ebay.com. The developer does, however, utilise the ebay affiliate program to track usage of this software and to monetise this and other publicly accessible projects.