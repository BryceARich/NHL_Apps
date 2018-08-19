from PIL import Image
import os


in_directory = 'resources/NHL_logos'
out_directory = 'resources/NHL_pixelated_logos'

for filename in os.listdir(in_directory):
    if filename.endswith(".png"): 
        # print(os.path.join(out_directory, filename[:-4]+"_pixelated.png"))

        img = Image.open(os.path.join(in_directory, filename))

        image_small = img.resize((20,20), resample=Image.BICUBIC)

        # result = image_small.resize(img.size, resample=Image.NEAREST)
        image_small.save(os.path.join(out_directory, filename[:-4]+"_pixelated.png"))

        img.close()

    else:
        print("wrong file type")
        print(filename)

