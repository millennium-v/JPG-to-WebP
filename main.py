from PIL import Image
import os
import pathlib
import re

def convert_jpg_to_webp(input_dir):
    output_dir = os.path.join(pathlib.Path.home(), 'Desktop', 'WebP_Output')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    files = os.listdir(input_dir)
    jpg_files = [f for f in files if f.endswith('.jpg')]

    for jpg_file in jpg_files:
        jpg_path = os.path.join(input_dir, jpg_file)
        webp_file = os.path.splitext(jpg_file)[0] + '.webp'
        webp_path = os.path.join(output_dir, webp_file)

        img = Image.open(jpg_path)
        img.save(webp_path, 'webp')

        print(f"{jpg_file} --> {webp_file} dönüştürüldü.")

# Kullanım örneği:
user_input = r'C:\Users\celik\OneDrive\Masaüstü\İş Dosyaları\2 Kol 1 Nefes\Kaliteli Görsel'
input_directory = re.sub(r'\\{1,2}', '\\\\\\\\', user_input)

convert_jpg_to_webp(input_directory)
