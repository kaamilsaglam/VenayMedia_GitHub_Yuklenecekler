import urllib.request
import os

base_dir = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler'
ig_posts_dir = os.path.join(base_dir, 'assets', 'ig_posts')

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)')]
urllib.request.install_opener(opener)

# We will overwrite the specific images that failed or were black.
# port_1_1 (Wedding)
url_1_1 = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Wedding_details_-_rings.jpg/800px-Wedding_details_-_rings.jpg'
# port_6_1 (Photography)
url_6_1 = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Photographer_at_work.jpg/800px-Photographer_at_work.jpg'

try:
    urllib.request.urlretrieve(url_1_1, os.path.join(ig_posts_dir, 'port_1_1.jpg'))
    print("Replaced port_1_1.jpg with valid image.")
except Exception as e:
    print(f"Error 1_1: {e}")

try:
    urllib.request.urlretrieve(url_6_1, os.path.join(ig_posts_dir, 'port_6_1.jpg'))
    print("Replaced port_6_1.jpg with valid image.")
except Exception as e:
    print(f"Error 6_1: {e}")

print("Image replacement done.")
