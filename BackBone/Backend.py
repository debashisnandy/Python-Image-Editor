import numpy as np
import cv2
from scipy import ndimage
import PIL
from PIL import Image,ImageEnhance
from PyQt5.QtGui import QImage

class Editor:
    def im(value,i):
        img = value

        a = np.asarray(img)
        if 3 in a.shape:
            if '-' in i:
                br = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
                h, s, v = cv2.split(br)

                i = int(i)

                value = abs(i)
                # low bright
                lim = 0 + value
                v[v < lim] = 0
                v[v >= lim] -= value

            else:
                br = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
                h, s, v = cv2.split(br)

                value = int(i)
                # high bright
                lim = 255 - value
                v[v > lim] = 255
                v[v <= lim] += value


            br = cv2.merge((h , s ,v))
            br = cv2.cvtColor(br, cv2.COLOR_HSV2RGB)
            return br
        else:
            img = value
            img = np.int16(img)
            # value = float(input("Enter the amount: (limit is 100) : "))
            if '-' in i:
                i = int(i)

                value = abs(i)
                contrast = 0
                brightness = value
                img = img * (contrast / 127 + 1) - contrast + brightness

            else:
                value = int(i)
                contrast = 0
                brightness = value
                img = img * (contrast / 127 + 1) - contrast + brightness

            img = np.clip(img, 0, 255)
            img = np.uint8(img)
            return img

class conta:
    def contrast1(value,path):
        img = path
        img = np.int16(img)
        #value = float(input("Enter the amount: (limit is 100) : "))
        if value > 0:
            contrast = (value * 12) / 2
            brightness = -30
            img = img * (contrast / 127 + 1) - contrast + brightness

        elif value < 0:
            contrast = (value * 2.6) / 2
            brightness = 30
            img = img * (contrast / 127 + 1) - contrast + brightness

        img = np.clip(img, 0, 255)
        img = np.uint8(img)
        return img

class EditorHue:
    def im(value,i):
        img = value

        a = np.asarray(img)

        if 3 in a.shape:
            if '-' in i:
                br = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
                h, s, v = cv2.split(br)

                i = int(i)

                value = abs(i)
                # low bright
                lim = 0 + value
                h[h < lim] = 0
                h[h >= lim] -= value

            else:
                br = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
                h, s, v = cv2.split(br)

                value = int(i)
                # high bright
                lim = 255 - value
                h[h > lim] = 255
                h[h <= lim] += value

            br = cv2.merge((h , s ,v))
            br = cv2.cvtColor(br, cv2.COLOR_HSV2RGB)
            return br

class EditorSatu:
    def im(value,i):
        img = value

        a = np.asarray(img)

        if 3 in a.shape:
            if '-' in i:
                br = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
                h, s, v = cv2.split(br)

                i = int(i)

                value = abs(i)
                # low bright
                lim = 0 + value
                s[s < lim] = 0
                s[s >= lim] -= value

            else:
                br = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
                h, s, v = cv2.split(br)

                value = int(i)
                # high bright
                lim = 255 - value
                s[s > lim] = 255
                s[s <= lim] += value


            br = cv2.merge((h , s ,v))
            br = cv2.cvtColor(br, cv2.COLOR_HSV2RGB)
            return br


class rotate:
    def rotate(path,angel):
        img = path
        angel = angel
        img = ndimage.rotate(img, angel)
        return img


class MyApp:

    def ResizeMyImage(self,name,Width,Height):
        img_file = name


        pil_image = np.asarray(img_file)

        # get the size of the original image
        tu = pil_image.shape
        if 3 in tu:
            height_org, width_org, d = pil_image.shape
        else:
            height_org, width_org = pil_image.shape

        self.Width = Width
        self.Height = Height

        Width = ((80 / 100) * self.Width)
        Height = ((70 / 100) * self.Height)


        if (width_org >= Width and height_org >= Height):
            mywidth = int(Width)
            img = Image.fromarray(img_file)
            wpercent = (mywidth / float(width_org))
            hsize = int((float(height_org) * float(wpercent)))
            img = img.resize((mywidth, hsize), PIL.Image.ANTIALIAS)
            self.photo = img

        else:
            self.photo = name

        self.photo = np.asarray(self.photo)

        if 3 in tu:
            img1 = cv2.cvtColor(self.photo, cv2.COLOR_BGR2RGB)
        else:
            img1 = cv2.cvtColor(self.photo, cv2.COLOR_GRAY2RGB)


        self.cvImage = img1
        height, width, byteValue = self.cvImage.shape
        byteValue = byteValue * width

        self.mQImage = QImage(self.cvImage, width, height, byteValue, QImage.Format_RGB888)

        return self.mQImage