# image comparator

from requests import *
from bs4 import BeautifulSoup as bs
import os
import sys


lx = '\033[0m'
la = '\033[90m'
lr = '\033[91m'
lg = '\033[92m'
lk = '\033[93m'
lb = '\033[94m'
lj = '\033[95m'
lc = '\033[96m'


def compare(image1, image2):
    print(f'{lx}[{lg}info{lx}] Comparator starting..')
    data = {
        'uploadfile': ('image1.jpg', open(image1, 'rb'), 'image/jpg'),
        'uploadfile2': ('image2.jpg', open(image2, 'rb'), 'image/jpg')
    }
    print(f'{lx}[{lg}info{lx}] Post {image1} and {image2} to the server')
    r = post(
        'https://www.imgonline.com.ua/eng/similarity-percent-result.php', files=data)
    b = bs(r.text, 'html.parser')
    print(f'{lx}[{lg}info{lx}] Comparing {image1} with {image2}')
    print(f'{lx}[{lg}info{lx}] Finish !')
    if 'Error' in str(b):
        print(f'{lx}[{lr}info{lx}] Error occured')
    else:

        prsn = b.find('span').text
        pr = prsn.replace('%', '')
        if float(pr) >= 50 and float(pr) < 90:
            lvl = 'Good'
        elif float(pr) >= 90:
            lvl = 'Excelent !'
        else:
            lvl = 'Bad'
        print(f'''
{lg}results{lx}
-------
*{lg}First image    : {lx}{image1}
*{lg}Second image   : {lx}{image2}
*{lg}Similarity %   : {lx}{prsn}
*{lg}Similarity lvl : {lx}{lvl}''')

#	print(image1,' and ',image2,' similarity percentage is ',b.find('span').text)


def ocr(image):
    print(f'{lx}[{lg}info{lx}] Satarting..')
    file = {'uploadfile': ('images.jpg', open(image, 'rb'), 'images/jpg')}
    data = {
        'efset1': '3',  # main language (english)
        'efset2': '19',  # second language (indonesian)
        'efset3': '64',  # -- (japanese)
        'efset4': '29',  # -- (korean)
        'efset5': '38',  # -- (chinese)
        'efset6': '1',  # image optimation (True)
        'efset8': '1',  # scan improvement (True)
        'efset8': '2'  # ocr program selected (2)
    }
    print(f'{lx}[{lg}info{lx}] Post the image')
    r = post('https://www.imgonline.com.ua/eng/ocr-result.php',
             data=data, files=file)
    print(f'{lx}[{lg}info{lx}] Check the server response')
    b = bs(r.text, 'html.parser')
    if 'Error' in str(b):
        print('Error has occured')
    else:
        print(f'{lx}[{lg}info{lx}] Response OK')
        for a in b.find_all('a'):
            if '.txt' in a.get('href') and '<b>' in str(a):
                print(f'{lx}[{lg}info{lx}] Read the OCR result')
                r = a.get('href')
                r = get(r)
                print(f'{lx}[{lg}info{lx}] Finish !')
                print(f'''
{lg} image OCR result{lx}
 -------------------
{r.text}''')
            else:
                pass


def qrscan(image):
    print(f'{lx}[{lg}info{lx}] Scanning {image}')
    url = 'https://www.imgonline.com.ua/eng/scan-qr-bar-code-result.php'
    file = {'uploadfile': ('qr.png', open(image, 'rb'), 'images/png')}
    data = {
        'codetype': '1',
        'rotset': '0',
        'croptype': '1',
        'cropleft': '0',
        'croprigt': '0',
        'croptop': '0',
        'cropbottom': '0'
    }
    r = post(url, data=data, files=file)
    b = bs(r.text, 'html.parser')
    print(f'{lx}[{lg}info{lx}] Try to get QR info')
    info = b.find('div', attrs={
                  'style': 'background-color:#CCFFCC;padding:5px;'}).text.replace('\n', '')
    print(f'{lx}[{lg}info{lx}] Done !')
    print(f'''
{lg}QR Code info
{lx}-------------
{lg}[{lx}{info}{lg}]{lx}
''')


def qrcreate():
    text = input(f'{lx}[{lg}input{lx}] Type your text : ')
#	text = text.replace(';','\n')
    output = input(f'{lx}[{lg}input{lx}] Output file name eg:qrcode.jpg : ')
    print(f'{lx}[{lg}info{lx}] Starting..')
    print(f'{lx}[{lg}info{lx}] Generating QR Code')
    data = {
        'effect-settings': text,
        'qtype': '',
        'img-width': '',
        'effect-settings-2': '5',
        'effect-settings-4': '0',
        'effect-settings-6': '2',
        'effect-settings-7': '#000000',
        'effect-settings-8': '#FFFFFF',
        'jpeg-conv-type': '3',
        'jpeg-quality': '95',
        'effect-settings-3': '1',
        'effect-settings-5': '2'
    }
    url = 'https://www.imgonline.com.ua'
    r = post(url+'/eng/create-qr-code-result.php', data=data).text
    b = bs(r, 'html.parser')
    for a in b.find_all('a'):
        if 'download.php?file=result_img/' in str(a):
            href = a.get('href').replace('..', '')
        else:
            pass
    print(f'{lx}[{lg}info{lx}] Success. Geting your QR Code')
    with open(output, 'wb') as f:
        r = get(url+href)
        f.write(r.content)
    f.close()
    print(f'{lx}[{lg}info{lx}] Done !')
    print(f'{lx}[{lg}info{lx}] Your QR Code saved to: {output}')


def imginfo(image):
    url = 'https://www.imgonline.com.ua/eng'
    file = {'uploadfile': ('image.jpg', open(image, 'rb'), 'images/jpg')}
    print(f'{lx}[{lg}info{lx}] get {image} info')
    r = post(url+'/exif-info-result.php', files=file)
    print(f'{lx}[{lg}info{lx}] fetch information')
    b = bs(r.text, 'html.parser')
    if 'This is not a JPEG image!' in str(b):
        print(f'{lx}[{lg}info{lx}] It is not JPEG image.')
    else:
        print(f'{lx}[{lg}info{lx}] well done !')
        for tr in b.find_all('tr'):
            td = tr.find_all('td')
            if len(td) == 1:
                print(f'\n{lg}{td[0].text}')
                print(lx+'--------------------------------------')
            else:
                print(f'{lg}{td[0].text}	: {lx}{td[1].text}')


def convert(image, output):
    url = 'https://www.imgonline.com.ua/eng'
    file = {'uploadfile': ('image.jpg', open(image, 'rb'), 'images/jpg')}
    data = {
        'ef-set': '1',  # output (JPEG)
        'ef-set-2': '1',  # not change
        'ef-set-3': '',
        'jpeg-conv-type': '1',  # standard JPEG
        'jpeg-meta': '1',  # meta data (saved)
        'jpeg-quality': '92',  # quality
    }
    r = post(url+'/convert-result.php', data=data, files=file)
    b = bs(r.text, 'html.parser')
    for a in b.find_all('a'):
        if 'download.php' in str(a):
            href = a.get('href')
        else:
            pass
    with open(output, 'wb') as f:
        r = get(href)
        f.write(r.content)


def banner():
    os.system('clear')
    print(f'''{lg}                                 
           ._  o  _ _|_  _   _  |  
           |_) | (_  |_ (_) (_) |_
           | {lx}Understand Your Picture
           
           
''')


def main():
    import argparse
    arg = argparse.ArgumentParser(description=f'{lk}Pictool V1.0 {lx}')
    arg.add_argument('-o', help='extract text from the image', metavar='image')
    arg.add_argument('-c', help='comparing two image',
                     nargs=2, metavar=('image1', 'image2'))
    arg.add_argument('-a', help='print tool informations',
                     nargs='?', const='about', metavar='about')
    arg.add_argument('-help', help='print help',
                     nargs='?', const='p', type=str)
    arg.add_argument('-qrs', help='QR code scanner', metavar='image')
    arg.add_argument('-qrc', help='create a QR code', nargs='?', const='p')
    arg.add_argument('-i', help='Image informations', metavar='image')
    arg.add_argument('-C', help='Convert all image format to JPEG format',
                     nargs=2, metavar=('image', 'output'))
    ar = arg.parse_args()

    if ar.o:
        banner()
        ocr(ar.o)
    elif ar.c:
        banner()
        compare(ar.c[0], ar.c[1])
    elif ar.qrs:
        banner()
        qrscan(ar.qrs)
    elif ar.qrc:
        banner()
        qrcreate()
    elif ar.i:
        banner()
        imginfo(ar.i)
    elif ar.C:
        banner()
        convert(ar.C[0], ar.C[1])
    elif ar.help:
        banner()
        print(f'''
{lg} Usage : {lx}python pictool.py -[option]

{lg} commands		informations
{lx} --------		------------
{lg}  -help			{lx}show this help message and exit
{lg}  -o image		{lx}extract text from the image
{lg}  -c image1 image2	{lx}comparing two image
{lg}  -a			{lx}print this tool informations
{lg}  -qrs image		{lx}QR Code scanner
{lg}  -qrc			{lx}create your QR Code
{lg}  -i image		{lx}Image informations
{lg}  -C image output	{lx}Convert all image format
			to JPEG format

{lg}Full tutorial: {lx}https://youtu.be/OQSAKlU23vo

''')
    elif ar.a:
        banner()
        print(f'''
{lg}Pictool v2.0
{lx}A simple picture tool.

{lg}coder   :{lx} Karjok Pangesty
{lg}created :{lx} April 25th, 2019, 7:00PM WIB
{lg}updated :{lx} April 26th, 2019, 8:00PM WIB
{lg}Contact :{lx} Facebook https://fb.me/om.karjok
          {lx}Telegram https://t.me/om_karjok''')

    else:
        banner()
        print(f'''
{lg}Wellcome !{lx}

It is Pictool v2.0,
Karjok Pangesty make it for you !

{lg}Use python pictool.py -help to get more command.{lx}
''')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        ex = sys.exc_info()
        print(f'{lx}[{lr}error{lx}] {ex[0].__name__}: {e} at line {ex[2].tb_lineno}')
