colors = [
    "#6D001A",
    "#BE0039",
    "#FF4500",
    "#FFA800",
    "#FFD635",
    "#FFF8B8",
    "#00A368",
    "#00CC78",
    "#7EED56",
    "#00756F",
    "#009EAA",
    "#00CCC0",
    "#2450A4",
    "#3690EA",
    "#51E9F4",
    "#493AC1",
    "#6A5CFF",
    "#94B3FF",
    "#811E9F",
    "#B44AC0",
    "#E4ABFF",
    "#DE107F",
    "#FF3881",
    "#FF99AA",
    "#6D482F",
    "#9C6926",
    "#FFB470",
    "#000000",
    "#515252",
    "#898D90",
    "#D4D7D9",
    "#FFFFFF"
]

from PIL import Image, ImageColor
from numpy import array

def getClosestColor(color):
        closestDiff = 99999999999
        closestColor = (0, 0, 0)
        for current in colors:
            diff = 0
            e = ImageColor.getcolor(current, "RGB")
            for section in range(3):
                diff += abs((e[section]) - color[section])
            if diff < closestDiff:
                closestDiff = diff
                closestColor = e
        return closestColor

def main():
    image = None
    original = Image.open(input("Image (e.g. example.jpeg): "))
    if original.size[0] > 100 or original.size[1] > 100:
        print("WARNING: This image is quite large, therefore we recommend resizing it. (" + str(original.size[0]) + "x" + str(original.size[1]) + ")")
    while image is None:
        try:
            print("")
            entered = int(input("Divide image by factor (1 if none): "))
        except ValueError:
            print("Invalid input.")
            continue
        print("")
        if not input("Image Size: " + str(original.size[0] // entered) + "x" + str(original.size[1] // entered) + "\nIs that okay (y/n)? ") == "y":
            continue
        image = original.resize((original.size[0] // entered, original.size[1] // entered))

    new = Image.new("RGB", image.size)
    pixels = array(image.getdata())
    for x in range(len(pixels)):
        color = getClosestColor(pixels[x])
        print(str(100 / len(pixels) * x) + "%" )
        new.putpixel((x % image.size[0], x // image.size[0]), color)

    new.save(input("Save as (e.g. output.jpeg): "))

if __name__ == "__main__":
    main()

