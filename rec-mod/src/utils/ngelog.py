import logging
from colorlog import ColoredFormatter
from tldextract import extract as tld

def logger(name):
    format_ = ColoredFormatter(
        '%(log_color)s%(levelname)s%(reset)s %(message)s',
        log_colors={
            '[#]':'blue',
            '[!]':'yellow',
            '[-]':'red',
            '[x]':'red',
            '[+]':'green'
        }
    )
    logging.addLevelName(10,'[#]')
    logging.addLevelName(20,'[!]')
    logging.addLevelName(30,'[-]')
    logging.addLevelName(40,'[x]')
    logging.addLevelName(50,'[+]')
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    handler.setFormatter(format_)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger
    
def no_skema(url):
    subomain = tld(url).subdomain
    domain = tld(url).domain
    suffix = tld(url).suffix
    return f'{domain}.{suffix}'
    
    
def skema(url):
    if url.startswith('http://') or url.startswith('https://'):
       return url
    else:
       if tld(url).subdomain == 'www':
          return f'https://{url}'
       else:
          return f'http://{url}'

def merah(string):
    return f'\033[91m{string}\033[0m'
       
def kuning(string):
    return f'\033[93m{string}\33[0m'

def hijau(string):
    return f'\033[92m{string}\033[0m'

def biru(string):
    return f'\033[94m{string}\033[0m'
    

h = '\033[92m'
m = '\033[91m'
b = '\033[94m'
p = '\033[0m'
a = '\033[1;30m'

ban = f'''
    _       _   _    __  __    ____  ____ ___ ____  _____ ____  
   / \     | | / \   \ \/ /   / ___||  _ \_ _|  _ \| ____|  _ \ 
  / _ \ _  | |/ _ \   \  /____\___ \| |_) | || | | |  _| | |_) |
 / ___ \ |_| / ___ \  /  \_____|__) |  __/| || |_| | |___|  _ < 
/_/   \_\___/_/   \_\/_/\_\   |____/|_|  |___|____/|_____|_| \_\

   //  \\\\
  _\\\{m}(){p}//_
 /_/{m}/  \{p}\\_\\
  {m}  \__/{p}  \\


                           

        ({a}whoami ==>{p}): {h}407 OSINT Gathering{p}
'''









