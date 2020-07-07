import concurrent.futures
import requests
import time
import logging

logging.basicConfig(filename='file.log', filemode='a', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


img_urls = [
    'https://images.unsplash.com/photo-1569936929562-f9d47d6789ea?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80',
    'https://images.unsplash.com/photo-1586812896097-03355c83a5a2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80',
    'https://images.unsplash.com/photo-1593728453770-7e3ab63dfff3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80',
    'https://images.unsplash.com/photo-1593792628761-9915abd5bb46?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=401&q=80',
    'https://images.unsplash.com/photo-1534415769476-35430bd3bb6c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=751&q=80',
    'https://images.unsplash.com/photo-1593444461581-b5ae72d3b637?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80',
    ]
N = str(len(img_urls))
t1 = time.perf_counter()
logging.debug('Started downloading %s photos.', N)

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.png'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)

t2 = time.perf_counter()
time = t2-t1
print(f'Finished in {time} seconds')
time1= str(time)
logging.debug('Finished downloading. It took %s seconds', time1)



