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

# Based on the function show_map found in Map.py
def draw_map(themap, save = False, filename = None,):
    """Draws the given integer map to a .png file

    Parameters
    ----------
    themap : [[int]]
        The integer map that is being drawn
    save : boolean, optional
        Set this to True if you want to save .png files of the visualizing
        for the path finding. Files are saved in the same directory as this file.
    filename : string, optional
        The filename used if save is set to True
    """

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
    if save and not filename:
        image.save("no-name.png")