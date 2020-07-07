import time
from PIL import Image, ImageFilter
import concurrent.futures
import logging

logging.basicConfig(filename='file.log', filemode='a', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

img_names = [
    'photo-1593758328014-87a131e16161.png',
    'photo-1586812896097-03355c83a5a2.png',
    'photo-1515005318787-cc68052b38f3.png',
    'photo-1593728453770-7e3ab63dfff3.png',
    'photo-1593163127678-9924b3d586a3.png',
    'photo-1592963219573-c388f7232a5f.png',
    'photo-1592856879770-aae96039dfdf.png',
    'photo-1592778897034-21da61a8cd02.png',
    'photo-1592918639681-299af38742ef.png',
    'photo-1592507645647-f2f1d8103c86.png',
    'photo-1592510988387-7b58307014c6.png',
    'photo-1593156618550-b0b335e1ee8b.png',
    'photo-1592937875863-636028d14039.png',
    'photo-1447966531936-911738a2a722.png',
    'photo-1530598343134-ee226a2e90e4.png',
    'photo-1592981703821-369bd42e2e1f.png',
    'photo-1593792628761-9915abd5bb46.png',
    'photo-1593444461581-b5ae72d3b637.png',
    'photo-1569936929562-f9d47d6789ea.png',
    'photo-1534415769476-35430bd3bb6c.png',
    'photo-1493015780735-f7330a5c88f2.png',
    'photo-1592916100255-63c7696107a1.png',
    'photo-1593462447694-f8ca79f8f8ab.png',
]

N = str(len(img_names))
logging.debug('Start filtering %s photos', N)

t1 = time.perf_counter()

size = (1200,1200)

def process_image(img_name):
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f'processed_mult/{img_name}')
    print(f'{img_name} was processed...')

with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(process_image, img_names)


t2 = time.perf_counter()
time_dif = str(t2-t1)
print(f'Finished in {t2-t1} seconds')
logging.debug('Finished in %s seconds', time_dif)
