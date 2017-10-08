from distutils.core import setup
setup(
  name = 'ebsear',
  packages = ['ebsear'], 
  version = '1.0.3',
  description = '(Unofficial) free eBay search API & CLI',
  author = "Asher Silvers",
  author_email = "ashersilvers@gmail.com",
  license='MIT',
  url = 'https://github.com/asherAgs/ebSear', 
  keywords = 'ebay search product products python',
  classifiers = [],
  entry_points={
    'console_scripts': [
      'ebsear = ebsear.cli:run',
     ],
  },
  install_requires = ['lxml==3.8.0','requests==2.18.1'],

)
