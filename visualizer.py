from PIL import Image

colors = {
    -1:  (211, 33, 45),    # Red (obstacle)
    -2:  (255, 0, 255),    # Magenta (start)
    -3:  (0, 128, 255),    # Cyan (goal)
    -4:  (255, 255, 0),    # Yellow (path)
    0:   (20, 99, 38),     # Green (closed)
    1:   (215, 215, 215),  # White
    2:   (166, 166, 166),  # Lightgrey
    3:   (96, 96, 96),     # Darkgrey
    4:   (36, 36, 36),     # Black
}

# Based on show_map given in Map.py
def draw_map(themap, save = False, filename = None,):
    # Define width and height of image
    width = len(themap[0])
    height = len(themap)
    # Define scale of the image
    scale = 20
    # Create an all-white image with the right scale
    image = Image.new('RGB', (width * scale, height * scale), (255, 255, 255))
    # Load image
    pixels = image.load()
    # Go through image and set pixel color for every position
    for y in range(height):
        for x in range(width):
            if themap[y][x] not in colors:
                continue
            for i in range(scale):
                for j in range(scale):
                    pixels[x * scale + i,
                            y * scale + j] = colors[themap[y][x]]
    image.show()
    if save and filename:
        image.save(filename)