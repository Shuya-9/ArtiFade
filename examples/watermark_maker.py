import random
import numpy as np
import argparse, os
from watermarker.marker import add_mark

random.seed(9)
np.random.seed(9)

# COLORS: Violet, Indigo, Blue, Green, Yellow, Orange, Red, White, Black
color = ["#9400D3", "#4B0082", "#0000FF", "#00FF00", "#FFFF00",
"#FF7F00", "#FF0000", "#FFFFFF", "#000000"]

# Text font size
size = np.linspace(20, 160, endpoint=True, num = 15)
np.random.shuffle(size)

# Angle of text
angle = np.linspace(0, 180, endpoint=False, num = 15)
np.random.shuffle(angle)

# Text content
mark = ["Diffusion Models", "Textual Inversion", "Latent Diffusion Models", "Watermark Removal"]

testing_lists = []

def random_tuple():
    testing_lists.append(
        (random.choice(mark),
        random.choice(color),
        random.choice(size),
        random.choice(angle)
        )
    )

# The following is our generated list in our paper
# [('Watermark Removal', '#FF0000', 160.0, 48.0), ('Watermark Removal', '#FF0000', 70.0, 84.0), ('Latent Diffusion Models', '#FFFFFF', 90.0, 156.0), ('Textual Inversion', '#000000', 150.0, 48.0), ('Textual Inversion', '#4B0082', 30.0, 84.0), ('Latent Diffusion Models', '#000000', 80.0, 84.0), ('Textual Inversion', '#FFFF00', 60.0, 12.0), ('Diffusion Models', '#FF7F00', 20.0, 144.0), ('Diffusion Models', '#FF7F00', 130.0, 168.0), ('Textual Inversion', '#000000', 20.0, 120.0)]
def processing_images(dir_root, save_root, tuple, name):
    abs_path = os.path.join(dir_root, name)
    save_abs_path = os.path.join(save_root, name)
    for image in os.listdir(abs_path):
        add_mark(file=os.path.join(abs_path, image), 
                out=save_abs_path, 
                mark=tuple[0], color=tuple[1], size=int(tuple[2]), angle=int(tuple[3]), opacity=0.6, space=120)


if __name__ == "__main__":

    # |--- dir_root
    #       |--- dog
    #       |--- .
    #       |--- .
    #       |--- .
    #       |--- cat
    #             |---01.jpg
    #             |---02.jpg
    #             |---03.jpg
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dir_root",
        type= str,
        default=None,
        required=True
    )
    parser.add_argument(
        "--save_root",
        type= str,
        default=None,
        required=True
    )
    opt = parser.parse_args()
    dir_root = opt.dir_root
    save_root = opt.save_root

    for i in range(10):
        random_tuple()
    
    obj_names = os.listdir(dir_root)
    for i in range(10):
        for obj_name in obj_names:
            save_dir = save_root + "/watermark_type%s" %i
            if not os.path.isdir(save_dir):
                os.makedirs(save_dir)
            processing_images(dir_root, save_dir, testing_lists[i], obj_name)