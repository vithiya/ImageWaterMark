from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk, UnidentifiedImageError, ImageFont, ImageDraw
from PIL.FontFile import WIDTH

WIDTH=600
HEIGHT=600
def upload():
    try:
        img_path = askopenfilename()
        im = Image.open(img_path).convert('RGBA')
        img_width, img_height = im.size
        if img_width > WIDTH or img_height > HEIGHT:
            while img_width > WIDTH or img_height > HEIGHT:
                img_width *= .99
                img_height *= .99
            im = im.resize((int(img_width), int(img_height)))
            messagebox.showinfo(title='Warning!',
                                message='The uploaded image is larger than the canvas. It will be resized.')

        img = ImageTk.PhotoImage(im)
        canvas.img = img
        canvas.create_image(WIDTH / 2, HEIGHT / 2, image=img, anchor=CENTER)

        txt = Image.new('RGBA', im.size, (255, 255, 255, 0))


        font = ImageFont.truetype('arial.ttf', 40)
        drawing_context = ImageDraw.Draw(txt)

        x = WIDTH / 2
        y = HEIGHT / 2

        # draw text, half opacity
        drawing_context.text((x, y), "@mysite.com", font=font, fill=(255, 255, 255, 128))
        #txt = txt.rotate(45)

        out_image = Image.alpha_composite(im, txt)
        # img = ImageTk.PhotoImage(out_image)
        # canvas.img = img
        # canvas.create_image(WIDTH / 2, HEIGHT / 2, image=img, anchor=CENTER)
        out_image.show()

    except UnidentifiedImageError:
        messagebox.showinfo(title='Upload Error',
                            message='Please select valid image')



window=Tk()
window.title("WaterMark Images")
window.config(padx=50, pady=50)

canvas = Canvas(width=WIDTH, height=HEIGHT)
canvas.pack()

button=Button(text="Upload Image",command=upload)
button.pack()






window.mainloop()