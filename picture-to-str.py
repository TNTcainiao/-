from PIL import Image

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")




def get_char(r,g,b,alpha):
    if alpha == 0:
        return " "
    length = len(ascii_char)

    gray = int(0.3 * r + 0.59 * g + 0.11 * b)

    unit = (256+1)/length

    return ascii_char[int(gray/unit)]

if __name__ == "__main__":

    im = Image.open("D:\python程序\Practice\wm.png")

    weight,high = im.size

    im = im.resize((80,60))
    weight, high = 80,60
    text = ""
    for i in range(high):

        for j in range(weight):

            text += get_char(*im.getpixel((j,i)))

        text += '\n'

    print(text)

    with open("output.txt",'w') as f:
        f.write(text)