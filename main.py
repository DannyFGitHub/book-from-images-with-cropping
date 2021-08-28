from PIL import Image
import os

home = "HOMEFOLDERNAMEHERE"

def main():
    start_path = '/Users/' + home + '/Desktop/Folder-Of-Books-Separate-Images-In-named-order'
    image_list = []
    for path,dirs,files in os.walk(start_path):
        # Sort files in alphabetical order
        files.sort()
        for filename in files:
            # Grayscale (use RGB instead of L for colour)
            im = Image.open(os.path.join(start_path, filename)).convert('L')
            # Crop dimensions
            im = im.crop((700, 100, 1863, 1352))
            image_list.append(im)
    image_list[0].save("./" + "book.pdf", save_all=True, append_images=image_list[1:])

if __name__ == "__main__":
    main()