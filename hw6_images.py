import cImage as image
import os.path

# -------------------------------
# FUNCTIONS
# -------------------------------

def red_filter(img):
    """ (Image object) -> Image object
    Returns a copy of img where the blue and green have been filtered
    out and only red remains.
    """
    red_only_img = img.copy() # create copy to manipulate
    w = img.getWidth()
    h = img.getHeight()
    for x in range(w): # iterate through all (x, y) pixel pairs
        for y in range(h):
            pixel = img.getPixel(x, y)
            red = pixel.getRed() # get original red value
            redPixel = image.Pixel(red, 0, 0)
            red_only_img.setPixel(x, y, redPixel) # replace pixel
    return red_only_img # return filtered image
    
def flip_horizontal(img):
    ''' (ImageObject) -> ImageObject
    Returns a copy of img where the pixels on the left column and right column are swapped,
    pixels on the second column and next-to-last column are swapped, etc.
    '''
    flip_horizontal_img = img.copy() # create copy to manipulate
    w = img.getWidth()
    h = img.getHeight()
    for y in range(h):
        for x in range(w//2): # iterate through all h but only to the half of w. Otherwise, it would be the same image.
            right_side = img.getPixel(w - 1 - x, y) 
            left_side = img.getPixel(x, y)
            flip_horizontal_img.setPixel(w - 1 - x, y, left_side) # Replace right side pixels with left side pixels
            flip_horizontal_img.setPixel(x,y, right_side)  # Replace left side pixels with right side pixels
    return flip_horizontal_img 


def flip_vertical(img):
    ''' (ImageObject) -> ImageObject
    Returns a copy of img where the pixels on the top row and bottom row are swapped,
    pixels on the second row and next-to-last row are swapped, etc.
    '''
    flip_vertical_img = img.copy() # create copy to manipulate
    w = img.getWidth()
    h = img.getHeight()
    for x in range(w):
        for y in range(h//2): # iterate through all w but only to the half of h. Otherwise, it would be the same picture.
            bottom_side = img.getPixel(x, h - 1 - y)
            top_side = img.getPixel(x, y)
            flip_vertical_img.setPixel(x, y, bottom_side) # Replace top side pixels with bottom side pixels
            flip_vertical_img.setPixel(x,h - 1 - y, top_side) # Replace bottom side pixels with top side pixels
    return flip_vertical_img 


def rotate_clockwise(img):
    ''' (ImageObject) -> ImageObject
    Returns a new image that had all white pixels filled
    with the pixels of the rotated image 90 degrees.
    '''
    w = img.getWidth()
    h = img.getHeight()
    rotate_clockwise_img2 = image.EmptyImage(h, w) # create a new empty img to manipulate
    for x in range(w):
        for y in range(h): # iterate through all (x, y) pixel pairs
            normal = img.getPixel(x, y)
            rotate_clockwise_img2.setPixel(h-1-y, x, normal) # Replace pixels from the new img with the normal img pixels so that it is rotated 90 degrees clockwise.
    return rotate_clockwise_img2

 
def to_negative(img):
    ''' (ImageObject) -> ImageObject
    Returns a copy of image object with the RGB components of each pixel with
    255 minus the corresponding component of the same pixel in the original
    image.
    '''
    to_negative_img = img.copy() # create copy to manipulate
    w = img.getWidth()
    h = img.getHeight()
    for y in range(h):
        for x in range(w): # iterate through all (x, y) pixel pairs
            pixel = img.getPixel(x, y)
            red = 255 - pixel.getRed()
            green = 255 - pixel.getGreen()
            blue = 255 - pixel.getBlue() # Get the value of 255 minus the original RGB values for red, green and blue for each pixel of the original img.
            newpixel = image.Pixel(red, green, blue) 
            to_negative_img.setPixel(x, y, newpixel) # Replacepixels from the new img with the new RGB values
    return to_negative_img

def cartoons(img):
    ''' (ImageObject) -> ImageObject
    Receives an int "intensity". Returns a copy of img with the black-and-white
    version of the original image such that edges within the image are colored as black
    with the value of int "intensity" and other pixels as white.
    '''
    intensity = 50
    cartoons_img = img.copy() # create copy to manipulate
    w = img.getWidth()
    h = img.getHeight()
    for y in range(h-1):
        for x in range(w-1): # iterate through all (x, y) pixel pairs except for the last ones. Otherwise we will be out of range.
            pixel = img.getPixel(x, y)
            pixel2 = img.getPixel(x+1,y+1) # We are going to compare adjacent pixels.
            if abs(pixel2.getRed() - pixel.getRed()) > intensity or abs(pixel2.getBlue() - pixel.getBlue()) > intensity or abs(pixel2.getGreen() - pixel.getGreen()) > intensity:
                newpixel = image.Pixel(0,0,0)
                cartoons_img.setPixel(x+1,y+1, newpixel) # If the difference is higher than the intensity, then change the adjacent pixel to black. (Obtained through trial and error)
            else:
                newpixel = image.Pixel(255,255,255)
                cartoons_img.setPixel(x+1,y+1, newpixel) #Otherwise, to white
    return cartoons_img

def scale_up(img):
    ''' (ImageObject) -> ImageObject
    Returns a new img where each dimension has been doubled.
    '''
    w = img.getWidth()
    h = img.getHeight()
    scale_up_img2 = image.EmptyImage(w*2, h*2)  # create a new img to manipulate
    for y in range(h*2):
        for x in range(w*2): # iterate through the double of h and w. (Each pixel is going to map to four pixels).
            pixel = img.getPixel(x // 2, y // 2)
            scale_up_img2.setPixel(x, y, pixel)
    return scale_up_img2

def scale_down(img):
    ''' (ImageObject) -> ImageObject
    Returns a new img where each dimension is cut in half.
    '''
    w = img.getWidth()
    h = img.getHeight()
    scale_down_img2 = image.EmptyImage(w//2, h//2)  # create a new img to manipulate
    for y in range(h//2):
        for x in range(w//2): #  # iterate through the half of h and w. (Four pixels are going to map to one pixel).
            pixel = img.getPixel(x * 2, y * 2)
            scale_down_img2.setPixel(x, y, pixel)
    return scale_down_img2

def leave_color(img):
    ''' (Image object) --> Image object
    Returns a copy of image with all non-red pixels converted to
    grayscale.
    '''
    leave_color_img = img.copy() # create copy to manipulate
    w = img.getWidth()
    h = img.getHeight()
    for x in range(w): 
        for y in range(h): # iterate through all (x, y) pixel pairs
            pixel = img.getPixel(x, y)
            red = pixel.getRed() 
            blue = pixel.getBlue()
            green = pixel.getGreen() # get original red, blue, green values
            gray = (red + blue + green) // 3 # to get the gray value we average those three values
            graypixel = image.Pixel(gray, gray, gray)
            if not (red > 125 and green < 125 and blue < 125): # non-red pixels
                leave_color_img.setPixel(x, y, graypixel) # replace pixel
    return leave_color_img 


def black_white(img):
    ''' (ImageObject) -> ImageObject
    Returns a copy of image object with only black and white pixels.
    '''
    w = img.getWidth()
    h = img.getHeight()
    black_white = img.copy() # create copy to manipulate
    for y in range(h):
        for x in range(w): # iterate through all (x, y) pixel pairs
            pixel = img.getPixel(x, y)
            red = pixel.getRed()
            blue = pixel.getBlue()
            green = pixel.getGreen() # get original red, blue, green values
            if red + blue + green > 200: # Condition to change RGB value of pixel to black
                black = image.Pixel(0,0,0)
                black_white.setPixel(x, y, black)
            else: # Otherwise, change the RGB value to white
                white = image.Pixel(255, 255, 255) 
                black_white.setPixel(x, y, white)
    return black_white


# -------------------------------
# HELPER FUNCTIONS
# -------------------------------

def open_image():
    ''' () -> ImageObject or None
    Return an Image object from file name, either given as a parameter or input
    by the user. Return None if the file does not exist or is not a .gif file.
    '''
    # if no filename given, get filename from user
    
    fname = input("Enter an image filename: ")

    # check if .gif file
    if not (fname[-4:] == '.gif'):
        print("Error: "+fname+" is not a .gif file")
        return None

    # check if file does not exists
    if not os.path.exists(fname):
        print("Error: There is no " + fname + " file")
        return None

    # return image from file
    return image.Image(fname)


def display_image(img):
    '''
    Display an image. Note: You must click to close the image before the program
    can continue running.
    '''
    w = img.getWidth()
    h = img.getHeight()
    win = image.ImageWin("Image", w, h)
    img.draw(win)
    win.exitonclick()
    return None


def save_image(img, fname):
    ''' (ImageObject, str) -> NoneType
    Save an image to the file fname.
    '''
    img.save(fname)
    return None


#--------------------------------
# BEGIN MAIN FUNCTION
#--------------------------------
# The code below calls all of the transformation function.


def main():
    """
    Main Program that load image(s) from file(s) and performs
    transformations to the images. 
    """
    file_name = open_image()
    options = {"Red filter": red_filter(file_name), "Flip horizontal": flip_horizontal(file_name), "Flip vertical": flip_vertical(file_name), "Rotate rotate_clockwise": rotate_clockwise(file_name), "Cartoons": cartoons(file_name), "Scale up": scale_up(file_name), "Scale down": scale_down(file_name), "Leave color" : leave_color(file_name), "Black & White": black_white(file_name)}
    print("What would you want to do with your image? Select an option")
    for i in options:
        print(str(options.
         + 1) + ".", i)
    selected = input("Option selected: ")
    while not(selected.isdigit()) and (selected < 1 or selected > 9):
        selected = input("Select a number from 1-9: ")

        original_img = image.Image(f'img/{file_name}.gif')
        display_image(options[selected])

    

# start the main function, but only if this file is being run "directly"
if __name__ == '__main__':
    main()
