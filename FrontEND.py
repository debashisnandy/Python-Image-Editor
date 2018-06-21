from PyQt5.QtWidgets import QFileDialog
import os
from matplotlib import pyplot as plt
from BackBone.Backend import *
from BackBone.BluePrint import *
Undo = []
Redo = []
brightFlag = 0
contFlag = 0
hueFlag = 0
satuFlag = 0
rotateFlag = 0
undoFlag = 0
flipFlag = 0
flipFlag1 = 0
sharpnessFlag = 0
blurFlag = 0
invertFlag = 0

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow, MyApp, Editor, conta,EditorHue,EditorSatu,rotate):

    def __init__(self,New_Window,Height,width):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self,Height,width)
        self.actionNew.triggered.connect(self.SetTheImage)
        self.actionSave.triggered.connect(self.SaveFile)
        self.actionUndo.triggered.connect(self.undoOperation)
        self.actionRedo.triggered.connect(self.RedoOperation)
        self.actionInvert.triggered.connect(self.invertOperation)
        self.actionHistogram.triggered.connect(self.histogram_Display)
        self.horizontalSlider.valueChanged.connect(self.BrightNess_Slideer)
        self.horizontalSlider_2.valueChanged.connect(self.Contrast_Slider)
        self.horizontalSlider_4.valueChanged.connect(self.Hue_Slideer)
        self.horizontalSlider_3.valueChanged.connect(self.Satu_Slideer)
        self.horizontalSlider_5.valueChanged.connect(self.SHarpnessSlideer)
        #self.horizontalSlider_6.valueChanged.connect(self.blur_implement)
        self.dial.valueChanged.connect(self.RoTate)
        self.actionAUTUMN.triggered.connect(self.colorAutumn)
        self.actionBONE.triggered.connect(self.colorBone)
        self.actionJET.triggered.connect(self.colorJet)
        self.actionWINTER.triggered.connect(self.colorWinter)
        self.actionRAINBOW.triggered.connect(self.colorRainbow)
        self.actionOCEAN.triggered.connect(self.colorOcean)
        self.actionSUMMER.triggered.connect(self.colorSummer)
        self.actionSPRING.triggered.connect(self.colorSpring)
        self.actionCOOL.triggered.connect(self.colorCool)
        self.actionHSV.triggered.connect(self.colorHsv)
        self.actionPINK.triggered.connect(self.colorPink)
        self.actionHOT.triggered.connect(self.colorHot)
        self.pushButton.clicked.connect(self.FlipButton)
        self.pushButton_2.clicked.connect(self.FlipButtonVr)
        self.actionEdge_Detection.triggered.connect(self.Edge_Detect)
        self.actionConvert_GrayScale.triggered.connect(self.cvrtToGrayScale)
        self.MainWindow = New_Window
        self.Width = width
        self.Height = Height

    def CheckIfElementPresent(self):
        if len(Undo):
            self.actionUndo.setEnabled(True)
            b = len(Undo)
            b = b - 1
            return ('T', b)
        else:
            self.actionUndo.setEnabled(False)
            return 'F'

    def CheckIfElementPresentRedo(self):
        if len(Redo):
            #self.actionRedo.setEnabled(True)
            b = len(Redo)
            b = b - 1
            return ('T', b)
        else:
            return 'F'


    def SetTheImage(self):

        try:
            self.ResetFlag('n')
            self.actionUndo.setEnabled(True)
            self.actionSave.setEnabled(True)
            self.actionSave_as.setEnabled(True)
            self.label1.setText(" ")
            name = QtWidgets.QFileDialog.getOpenFileName(self.MainWindow, 'r', '/home', '*.jpg')
            name = name[0]
            name = cv2.imread(name)
            name = np.asarray(name)
            Undo.append(name)
            CustomImg = MyApp.ResizeMyImage(self,name,self.Width,self.Height)
            pixmap = QtGui.QPixmap(CustomImg)
            #self.label1.setAutoFillBackground(True)
            self.label1.setAlignment(QtCore.Qt.AlignCenter)
            self.label1.setPixmap(pixmap)
            self.setSliderDefault()
            self.setFlagDefault()
        except:
            print("No input")
    def undoOperation(self):

        if 'T' in self.CheckIfElementPresent():

            p = Undo.pop()
            Redo.append(p)
            self.actionRedo.setEnabled(True)

            if len(Undo) == 0:
                self.label1.setText(" ")
                self.setFlagDefault()
            else:
                b = len(Undo)
                b = b - 1
                CustomImg = Undo[b]
                CustomImg = MyApp.ResizeMyImage(self, CustomImg, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(CustomImg)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                self.setFlagDefault()

    def RedoOperation(self):

        if 'T' in self.CheckIfElementPresentRedo():

            a = Redo.pop()
            Undo.append(a)
            self.setFlagDefault()
            CustomImg = MyApp.ResizeMyImage(self, a, self.Width, self.Height)
            self.pixmap = QtGui.QPixmap(CustomImg)
            self.label1.setAutoFillBackground(True)
            self.label1.setPixmap(self.pixmap)
            self.setFlagDefault()
        else:
            self.actionRedo.setEnabled(False)
    def setSliderDefault(self):
        self.horizontalSlider.setValue(0)
        self.horizontalSlider_2.setValue(0)
        self.horizontalSlider_3.setValue(0)
        self.horizontalSlider_4.setValue(0)
        self.horizontalSlider_5.setValue(0)
        self.dial.setValue(0)

    def setFlagDefault(self):
        global brightFlag, colorAutumnFlag, flipFlag, invertFlag, contFlag, hueFlag, satuFlag, rotateFlag, sharpnessFlag, flipFlag1, blurFlag, colorBoneFlag
        global colorJetFlag, colorWinterFlag, colorRainbowFlag, colorOceanFlag, colorSummerFlag, colorSpringFlag, colorCoolFlag, colorHsvFlag, colorPinkFlag, colorHotFlag
        brightFlag = 0
        contFlag = 0
        hueFlag = 0
        satuFlag = 0
        rotateFlag = 0
        flipFlag = 0
        sharpnessFlag = 0
        flipFlag1 = 0
        blurFlag = 0
        invertFlag = 0
        colorAutumnFlag = 0
        colorBoneFlag = 0
        colorJetFlag = 0
        colorWinterFlag = 0
        colorRainbowFlag = 0
        colorOceanFlag = 0
        colorSummerFlag = 0
        colorSpringFlag = 0
        colorCoolFlag = 0
        colorHsvFlag = 0
        colorPinkFlag = 0
        colorHotFlag = 0

    def invertOperation(self):
        if 'T' in self.CheckIfElementPresent():

            global invertFlag
            invertFlag = invertFlag + 1

            self.ResetFlag('i')
            if invertFlag == 1:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1]
                self.inv = (255 - name)
                re = MyApp.ResizeMyImage(self,self.inv,self.Width,self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.inv)
                Undo.append(ed)

            else:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1-1]
                self.inv = name
                re = MyApp.ResizeMyImage(self, self.inv, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.inv)
                Undo[name1] = ed


    def BrightNess_Slideer(self):

        if 'T' in self.CheckIfElementPresent():

            global brightFlag
            brightFlag = brightFlag + 1

            self.ResetFlag('b')
            if brightFlag == 1:
                sl = str(self.horizontalSlider.value())
                self.label_8.setText(sl)
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1]
                self.ed = Editor.im(name,sl)
                re = MyApp.ResizeMyImage(self,self.ed,self.Width,self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.ed)
                Undo.append(ed)

            else:

                sl = str(self.horizontalSlider.value())
                self.label_8.setText(sl)
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1-1]
                self.ed = Editor.im(name, sl)
                re = MyApp.ResizeMyImage(self, self.ed, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.ed)
                Undo[name1] = ed


    def Contrast_Slider(self):

        if 'T' in self.CheckIfElementPresent():

            global contFlag
            contFlag = contFlag + 1

            self.ResetFlag('c')
            if contFlag == 1:
                sl = int(self.horizontalSlider_2.value())
                self.label_10.setText(str(sl))
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1]
                sl = conta.contrast1(sl,name)
                self.re = MyApp.ResizeMyImage(self, sl, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(self.re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                sl = np.asarray(sl)
                Undo.append(sl)

            else:
                sl = int(self.horizontalSlider_2.value())
                self.label_10.setText(str(sl))
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1-1]
                sl = conta.contrast1(sl, name)
                self.re = MyApp.ResizeMyImage(self, sl, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(self.re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                sl = np.asarray(sl)
                Undo[name1] = sl

    def Hue_Slideer(self):

        if 'T' in self.CheckIfElementPresent():

            global hueFlag
            hueFlag = hueFlag + 1

            self.ResetFlag('h')
            if hueFlag == 1:
                sl = str(self.horizontalSlider_4.value())
                self.label_14.setText(sl)
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1]
                a = np.asarray(name)

                if 3 in a.shape:
                    self.hd = EditorHue.im(name,sl)
                    re = MyApp.ResizeMyImage(self,self.hd,self.Width,self.Height)
                    self.pixmap = QtGui.QPixmap(re)
                    self.label1.setAutoFillBackground(True)
                    self.label1.setPixmap(self.pixmap)
                    ed = np.asarray(self.hd)
                    Undo.append(ed)

            else:

                sl = str(self.horizontalSlider_4.value())
                self.label_14.setText(sl)
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1-1]
                a = np.asarray(name)
                if 3 in a.shape:
                    self.hd = EditorHue.im(name, sl)
                    re = MyApp.ResizeMyImage(self, self.hd, self.Width, self.Height)
                    self.pixmap = QtGui.QPixmap(re)
                    self.label1.setAutoFillBackground(True)
                    self.label1.setPixmap(self.pixmap)
                    ed = np.asarray(self.hd)
                    Undo[name1] = ed

    def Satu_Slideer(self):

        if 'T' in self.CheckIfElementPresent():

            global satuFlag
            satuFlag = satuFlag + 1

            self.ResetFlag('s')
            if satuFlag == 1:
                sl = str(self.horizontalSlider_3.value())
                self.label_12.setText(sl)
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1]
                a = np.asarray(name)
                if 3 in a.shape:
                    self.sd = EditorSatu.im(name,sl)
                    re = MyApp.ResizeMyImage(self,self.sd,self.Width,self.Height)
                    self.pixmap = QtGui.QPixmap(re)
                    self.label1.setAutoFillBackground(True)
                    self.label1.setPixmap(self.pixmap)
                    ed = np.asarray(self.sd)
                    Undo.append(ed)

            else:
                sl = str(self.horizontalSlider_3.value())
                self.label_12.setText(sl)
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1-1]
                a = np.asarray(name)
                if 3 in a.shape:
                    self.sd = EditorSatu.im(name, sl)
                    re = MyApp.ResizeMyImage(self, self.sd, self.Width, self.Height)
                    self.pixmap = QtGui.QPixmap(re)
                    self.label1.setAutoFillBackground(True)
                    self.label1.setPixmap(self.pixmap)
                    ed = np.asarray(self.sd)
                    Undo[name1] = ed

    def RoTate(self):

        if 'T' in self.CheckIfElementPresent():

            global rotateFlag
            rotateFlag = rotateFlag + 1

            self.ResetFlag('r')
            if rotateFlag == 1:
                sl = int(self.dial.value())
                self.label_9.setText(str(sl))
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1]
                self.rd = rotate.rotate(name,sl)
                re = MyApp.ResizeMyImage(self,self.rd,self.Width,self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.rd)
                Undo.append(ed)

            else:

                sl = int(self.dial.value())
                self.label_9.setText(str(sl))
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1-1]
                self.rd = rotate.rotate(name, sl)
                re = MyApp.ResizeMyImage(self, self.rd, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.rd)
                Undo[name1] = ed

    def FlipButton(self):

        if 'T' in self.CheckIfElementPresent():

            global flipFlag
            flipFlag = flipFlag + 1

            self.ResetFlag('f')
            if flipFlag == 1:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1]
                self.fd = self.FliP(name)
                re = MyApp.ResizeMyImage(self, self.fd, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.fd)
                Undo.append(ed)
            else:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1]
                self.fd = self.FliP(name)
                re = MyApp.ResizeMyImage(self, self.fd, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.fd)
                Undo[name1] = ed
    def FlipButtonVr(self):

        if 'T' in self.CheckIfElementPresent():

            global flipFlag
            flipFlag = flipFlag + 1

            self.ResetFlag('v')
            if flipFlag == 1:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1]
                self.fd = self.FliP_ver(name)
                re = MyApp.ResizeMyImage(self, self.fd, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.fd)
                Undo.append(ed)
            else:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1]
                self.fd = self.FliP_ver(name)
                re = MyApp.ResizeMyImage(self, self.fd, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.fd)
                Undo[name1] = ed

    def SHarpnessSlideer(self):

        if 'T' in self.CheckIfElementPresent():

            global sharpnessFlag
            sharpnessFlag = sharpnessFlag + 1

            self.ResetFlag('1')
            if sharpnessFlag == 1:
                sl = float(self.horizontalSlider_5.value())
                self.label_15.setText(str(sl))
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1]
                self.shd = self.Shrpns(name,sl)
                re = MyApp.ResizeMyImage(self,self.shd,self.Width,self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.shd)
                Undo.append(ed)

            else:
                sl = float(self.horizontalSlider_5.value())
                self.label_15.setText(str(sl))
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1-1]
                self.shd = self.Shrpns(name, sl)
                re = MyApp.ResizeMyImage(self, self.shd, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.shd)
                Undo[name1] = ed

    def blur_implement(self):
        if 'T' in self.CheckIfElementPresent():

            global blurFlag
            blurFlag = blurFlag + 1

            self.ResetFlag('u')
            if blurFlag == 1:
                sl = int(self.horizontalSlider_6.value())
                self.label_13.setText(str(sl))
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1]
                sl = cv2.medianBlur(name,sl)
                sl = np.asarray(sl)
                Undo.append(sl)
                self.re = MyApp.ResizeMyImage(self, sl, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(self.re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)


            else:
                sl = int(self.horizontalSlider_6.value())
                self.label_13.setText(str(sl))
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1-1]
                sl = cv2.medianBlur(name, sl)
                sl = np.asarray(sl)
                Undo[name1] = sl
                self.re = MyApp.ResizeMyImage(self, sl, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(self.re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)




    def FliP(self, path):
        img = path
        mirror_img = cv2.flip(img, 1)
        return mirror_img

    def FliP_ver(self, path):
        img = path
        mirror_img = cv2.flip(img, 0)
        return mirror_img

    def Shrpns(self, path, value):
        im = path
        im = Image.fromarray(im)
        Sharpness = ImageEnhance.Sharpness(im)
        Sharpness = Sharpness.enhance(value)
        Sharpness = np.asarray(Sharpness)


        return Sharpness

    def Edge_Detect(self):
        if 'T' in self.CheckIfElementPresent():
            bla, name1 = self.CheckIfElementPresent()
            name = Undo[name1]
            self.Ed = cv2.Canny(name,100,200)
            re = MyApp.ResizeMyImage(self, self.Ed, self.Width, self.Height)
            self.pixmap = QtGui.QPixmap(re)
            self.label1.setAutoFillBackground(True)
            self.label1.setPixmap(self.pixmap)
            ed = np.asarray(self.Ed)
            Undo.append(ed)

    def histogram_Display(self):

        if 'T' in self.CheckIfElementPresent():
            bla, name1 = self.CheckIfElementPresent()

            img = Undo[name1]

            color = ('b', 'g', 'r')
            for channel, col in enumerate(color):
                histr = cv2.calcHist([img], [channel], None, [256], [0, 256])
                plt.plot(histr, color=col)
                plt.xlim([0, 256])
            plt.title('Histogram for color scale picture')
            plt.show()
    def cvrtToGrayScale(self):
        if 'T' in self.CheckIfElementPresent():
            self.setFlagDefault()
            bla, name1 = self.CheckIfElementPresent()

            img = Undo[name1]

            img = np.asarray(img)

            if 3 in img.shape:

                self.cd = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                print("Gray",np.asarray(self.cd).shape)
                re = MyApp.ResizeMyImage(self, self.cd, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.cd)
                Undo.append(ed)
            else:
                self.actionConvert_GrayScale.setEnabled(False)

    def ResetFlag(self,par):

        global brightFlag, colorAutumnFlag, invertFlag, contFlag, hueFlag, rotateFlag, flipFlag, sharpnessFlag, flipFlag1, blurFlag, satuFlag, colorBoneFlag
        global colorJetFlag, colorWinterFlag, colorRainbowFlag, colorOceanFlag, colorSummerFlag, colorSpringFlag, colorCoolFlag, colorHsvFlag, colorPinkFlag, colorHotFlag

        if 'c' in par:
            brightFlag = 0
            hueFlag = 0
            rotateFlag = 0
            flipFlag = 0
            flipFlag1 = 0
            sharpnessFlag = 0
            blurFlag = 0
            invertFlag = 0
            satuFlag = 0
            colorAutumnFlag = 0
            colorBoneFlag = 0
            colorJetFlag = 0
            colorWinterFlag = 0
            colorRainbowFlag = 0
            colorOceanFlag = 0
            colorSummerFlag = 0
            colorSpringFlag = 0
            colorCoolFlag = 0
            colorHsvFlag = 0
            colorPinkFlag = 0
            colorHotFlag = 0

        elif 'b' in par:
            contFlag = 0
            flipFlag1 = 0
            hueFlag = 0
            rotateFlag = 0
            flipFlag = 0
            sharpnessFlag = 0
            blurFlag = 0
            invertFlag = 0
            satuFlag = 0
            colorAutumnFlag = 0
            colorBoneFlag = 0
            colorJetFlag = 0
            colorWinterFlag = 0
            colorRainbowFlag = 0
            colorOceanFlag = 0
            colorSummerFlag = 0
            colorSpringFlag = 0
            colorCoolFlag = 0
            colorHsvFlag = 0
            colorPinkFlag = 0
            colorHotFlag = 0
        elif 'u' in par:
            contFlag = 0
            flipFlag1 = 0
            hueFlag = 0
            rotateFlag = 0
            flipFlag = 0
            sharpnessFlag = 0
            brightFlag = 0
            invertFlag = 0
            satuFlag = 0
            colorAutumnFlag = 0
            colorBoneFlag = 0
            colorJetFlag = 0
            colorWinterFlag = 0
            colorRainbowFlag = 0
            colorOceanFlag = 0
            colorSummerFlag = 0
            colorSpringFlag = 0
            colorCoolFlag = 0
            colorHsvFlag = 0
            colorPinkFlag = 0
            colorHotFlag = 0
        elif 'h' in par:
            brightFlag = 0
            contFlag = 0
            rotateFlag = 0
            flipFlag = 0
            sharpnessFlag = 0
            flipFlag1 = 0
            blurFlag = 0
            invertFlag = 0
            satuFlag = 0
            colorAutumnFlag = 0
            colorBoneFlag = 0
            colorJetFlag = 0
            colorWinterFlag = 0
            colorRainbowFlag = 0
            colorOceanFlag = 0
            colorSummerFlag = 0
            colorSpringFlag = 0
            colorCoolFlag = 0
            colorHsvFlag = 0
            colorPinkFlag = 0
            colorHotFlag = 0
        elif 'i' in par:
            brightFlag = 0
            contFlag = 0
            rotateFlag = 0
            flipFlag = 0
            sharpnessFlag = 0
            flipFlag1 = 0
            blurFlag = 0
            hueFlag = 0
            satuFlag = 0
            colorAutumnFlag = 0
            colorBoneFlag = 0
            colorJetFlag = 0
            colorWinterFlag = 0
            colorRainbowFlag = 0
            colorOceanFlag = 0
            colorSummerFlag = 0
            colorSpringFlag = 0
            colorCoolFlag = 0
            colorHsvFlag = 0
            colorPinkFlag = 0
            colorHotFlag = 0
        elif 'r' in par:
            brightFlag = 0
            contFlag = 0
            hueFlag = 0
            flipFlag = 0
            sharpnessFlag = 0
            flipFlag1 = 0
            blurFlag = 0
            invertFlag = 0
            satuFlag = 0
            colorAutumnFlag = 0
            colorBoneFlag = 0
            colorJetFlag = 0
            colorWinterFlag = 0
            colorRainbowFlag = 0
            colorOceanFlag = 0
            colorSummerFlag = 0
            colorSpringFlag = 0
            colorCoolFlag = 0
            colorHsvFlag = 0
            colorPinkFlag = 0
            colorHotFlag = 0
        elif 'f' in par:
            brightFlag = 0
            contFlag = 0
            hueFlag = 0
            rotateFlag = 0
            sharpnessFlag = 0
            flipFlag1 = 0
            blurFlag = 0
            invertFlag = 0
            satuFlag = 0
            colorAutumnFlag = 0
            colorBoneFlag = 0
            colorJetFlag = 0
            colorWinterFlag = 0
            colorRainbowFlag = 0
            colorOceanFlag = 0
            colorSummerFlag = 0
            colorSpringFlag = 0
            colorCoolFlag = 0
            colorHsvFlag = 0
            colorPinkFlag = 0
            colorHotFlag = 0
        elif 'v' in par:
            brightFlag = 0
            contFlag = 0
            hueFlag = 0
            rotateFlag = 0
            sharpnessFlag = 0
            flipFlag = 0
            blurFlag = 0
            invertFlag = 0
            satuFlag = 0
            colorAutumnFlag = 0
            colorBoneFlag = 0
            colorJetFlag = 0
            colorWinterFlag = 0
            colorRainbowFlag = 0
            colorOceanFlag = 0
            colorSummerFlag = 0
            colorSpringFlag = 0
            colorCoolFlag = 0
            colorHsvFlag = 0
            colorPinkFlag = 0
            colorHotFlag = 0
        elif '1' in par:
            brightFlag = 0
            contFlag = 0
            hueFlag = 0
            rotateFlag = 0
            flipFlag = 0
            flipFlag1 = 0
            blurFlag = 0
            invertFlag = 0
            satuFlag = 0
            colorAutumnFlag = 0
            colorBoneFlag = 0
            colorJetFlag = 0
            colorWinterFlag = 0
            colorRainbowFlag = 0
            colorOceanFlag = 0
            colorSummerFlag = 0
            colorSpringFlag = 0
            colorCoolFlag = 0
            colorHsvFlag = 0
            colorPinkFlag = 0
            colorHotFlag = 0
        elif 's' in par:
            brightFlag = 0
            contFlag = 0
            hueFlag = 0
            rotateFlag = 0
            flipFlag = 0
            flipFlag1 = 0
            blurFlag = 0
            invertFlag = 0
            sharpnessFlag = 0
            colorAutumnFlag = 0
            colorBoneFlag = 0
            colorJetFlag = 0
            colorWinterFlag = 0
            colorRainbowFlag = 0
            colorOceanFlag = 0
            colorSummerFlag = 0
            colorSpringFlag = 0
            colorCoolFlag = 0
            colorHsvFlag = 0
            colorPinkFlag = 0
            colorHotFlag = 0
        elif 'n' in par:
            brightFlag = 0
            contFlag = 0
            hueFlag = 0
            rotateFlag = 0
            flipFlag = 0
            flipFlag1 = 0
            sharpnessFlag = 0
            blurFlag = 0
            satuFlag = 0
            invertFlag = 0
            colorAutumnFlag = 0
            colorBoneFlag = 0
            colorJetFlag = 0
            colorWinterFlag = 0
            colorRainbowFlag = 0
            colorOceanFlag = 0
            colorSummerFlag = 0
            colorSpringFlag = 0
            colorCoolFlag = 0
            colorHsvFlag = 0
            colorPinkFlag = 0
            colorHotFlag = 0
        elif 'A' in par:
            brightFlag = 0
            contFlag = 0
            hueFlag = 0
            rotateFlag = 0
            flipFlag = 0
            flipFlag1 = 0
            sharpnessFlag = 0
            blurFlag = 0
            satuFlag = 0
            invertFlag = 0
            colorBoneFlag = 0
            colorJetFlag = 0
            colorWinterFlag = 0
            colorRainbowFlag = 0
            colorOceanFlag = 0
            colorSummerFlag = 0
            colorSpringFlag = 0
            colorCoolFlag = 0
            colorHsvFlag = 0
            colorPinkFlag = 0
            colorHotFlag = 0
        elif 'B' in par:
            brightFlag = 0
            contFlag = 0
            hueFlag = 0
            rotateFlag = 0
            flipFlag = 0
            flipFlag1 = 0
            sharpnessFlag = 0
            blurFlag = 0
            satuFlag = 0
            invertFlag = 0
            colorAutumnFlag = 0
            colorJetFlag = 0
            colorWinterFlag = 0
            colorRainbowFlag = 0
            colorOceanFlag = 0
            colorSummerFlag = 0
            colorSpringFlag = 0
            colorCoolFlag = 0
            colorHsvFlag = 0
            colorPinkFlag = 0
            colorHotFlag = 0
        elif 'J' in par:
            brightFlag = 0
            contFlag = 0
            hueFlag = 0
            rotateFlag = 0
            flipFlag = 0
            flipFlag1 = 0
            sharpnessFlag = 0
            blurFlag = 0
            satuFlag = 0
            invertFlag = 0
            colorAutumnFlag = 0
            colorBoneFlag = 0
            colorWinterFlag = 0
            colorRainbowFlag = 0
            colorOceanFlag = 0
            colorSummerFlag = 0
            colorSpringFlag = 0
            colorCoolFlag = 0
            colorHsvFlag = 0
            colorPinkFlag = 0
            colorHotFlag = 0
        elif 'W' in par:
            brightFlag = 0
            contFlag = 0
            hueFlag = 0
            rotateFlag = 0
            flipFlag = 0
            flipFlag1 = 0
            sharpnessFlag = 0
            blurFlag = 0
            satuFlag = 0
            invertFlag = 0
            colorAutumnFlag = 0
            colorBoneFlag = 0
            colorJetFlag = 0
            colorRainbowFlag = 0
            colorOceanFlag = 0
            colorSummerFlag = 0
            colorSpringFlag = 0
            colorCoolFlag = 0
            colorHsvFlag = 0
            colorPinkFlag = 0
            colorHotFlag = 0

        elif 'R' in par:
            brightFlag = 0
            contFlag = 0
            hueFlag = 0
            rotateFlag = 0
            flipFlag = 0
            flipFlag1 = 0
            sharpnessFlag = 0
            blurFlag = 0
            satuFlag = 0
            invertFlag = 0
            colorAutumnFlag = 0
            colorBoneFlag = 0
            colorJetFlag = 0
            colorWinterFlag = 0
            colorOceanFlag = 0
            colorSummerFlag = 0
            colorSpringFlag = 0
            colorCoolFlag = 0
            colorHsvFlag = 0
            colorPinkFlag = 0
            colorHotFlag = 0
        elif 'O' in par:
            brightFlag = 0
            contFlag = 0
            hueFlag = 0
            rotateFlag = 0
            flipFlag = 0
            flipFlag1 = 0
            sharpnessFlag = 0
            blurFlag = 0
            satuFlag = 0
            invertFlag = 0
            colorAutumnFlag = 0
            colorBoneFlag = 0
            colorJetFlag = 0
            colorWinterFlag = 0
            colorRainbowFlag = 0
            colorSummerFlag = 0
            colorSpringFlag = 0
            colorCoolFlag = 0
            colorHsvFlag = 0
            colorPinkFlag = 0
            colorHotFlag = 0
        elif 'U' in par:
            brightFlag = 0
            contFlag = 0
            hueFlag = 0
            rotateFlag = 0
            flipFlag = 0
            flipFlag1 = 0
            sharpnessFlag = 0
            blurFlag = 0
            satuFlag = 0
            invertFlag = 0
            colorAutumnFlag = 0
            colorBoneFlag = 0
            colorJetFlag = 0
            colorWinterFlag = 0
            colorRainbowFlag = 0
            colorOceanFlag = 0
            colorSpringFlag = 0
            colorCoolFlag = 0
            colorHsvFlag = 0
            colorPinkFlag = 0
            colorHotFlag = 0
        elif 'S' in par:
            brightFlag = 0
            contFlag = 0
            hueFlag = 0
            rotateFlag = 0
            flipFlag = 0
            flipFlag1 = 0
            sharpnessFlag = 0
            blurFlag = 0
            satuFlag = 0
            invertFlag = 0
            colorAutumnFlag = 0
            colorBoneFlag = 0
            colorJetFlag = 0
            colorWinterFlag = 0
            colorRainbowFlag = 0
            colorOceanFlag = 0
            colorSummerFlag = 0
            colorCoolFlag = 0
            colorHsvFlag = 0
            colorPinkFlag = 0
            colorHotFlag = 0
        elif 'C' in par:
            brightFlag = 0
            contFlag = 0
            hueFlag = 0
            rotateFlag = 0
            flipFlag = 0
            flipFlag1 = 0
            sharpnessFlag = 0
            blurFlag = 0
            satuFlag = 0
            invertFlag = 0
            colorAutumnFlag = 0
            colorBoneFlag = 0
            colorJetFlag = 0
            colorWinterFlag = 0
            colorRainbowFlag = 0
            colorOceanFlag = 0
            colorSummerFlag = 0
            colorSpringFlag = 0
            colorHsvFlag = 0
            colorPinkFlag = 0
            colorHotFlag = 0
        elif 'H' in par:
            brightFlag = 0
            contFlag = 0
            hueFlag = 0
            rotateFlag = 0
            flipFlag = 0
            flipFlag1 = 0
            sharpnessFlag = 0
            blurFlag = 0
            satuFlag = 0
            invertFlag = 0
            colorAutumnFlag = 0
            colorBoneFlag = 0
            colorJetFlag = 0
            colorWinterFlag = 0
            colorRainbowFlag = 0
            colorOceanFlag = 0
            colorSummerFlag = 0
            colorSpringFlag = 0
            colorCoolFlag = 0
            colorPinkFlag = 0
            colorHotFlag = 0
        elif 'P' in par:
            brightFlag = 0
            contFlag = 0
            hueFlag = 0
            rotateFlag = 0
            flipFlag = 0
            flipFlag1 = 0
            sharpnessFlag = 0
            blurFlag = 0
            satuFlag = 0
            invertFlag = 0
            colorAutumnFlag = 0
            colorBoneFlag = 0
            colorJetFlag = 0
            colorWinterFlag = 0
            colorRainbowFlag = 0
            colorOceanFlag = 0
            colorSummerFlag = 0
            colorSpringFlag = 0
            colorCoolFlag = 0
            colorHsvFlag = 0
            colorHotFlag = 0
        elif 'T' in par:
            brightFlag = 0
            contFlag = 0
            hueFlag = 0
            rotateFlag = 0
            flipFlag = 0
            flipFlag1 = 0
            sharpnessFlag = 0
            blurFlag = 0
            satuFlag = 0
            invertFlag = 0
            colorAutumnFlag = 0
            colorBoneFlag = 0
            colorJetFlag = 0
            colorWinterFlag = 0
            colorRainbowFlag = 0
            colorOceanFlag = 0
            colorSummerFlag = 0
            colorSpringFlag = 0
            colorCoolFlag = 0
            colorHsvFlag = 0
            colorPinkFlag = 0

    def colorAutumn(self):

        if 'T' in self.CheckIfElementPresent():

            global colorAutumnFlag
            colorAutumnFlag = colorAutumnFlag + 1

            self.ResetFlag('A')
            if colorAutumnFlag == 1:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1]
                self.ed = cv2.applyColorMap(name, cv2.COLORMAP_AUTUMN)
                re = MyApp.ResizeMyImage(self, self.ed, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.ed)
                Undo.append(ed)

            else:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1 - 1]
                self.ed = name
                re = MyApp.ResizeMyImage(self, self.ed, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.ed)
                Undo[name1] = ed
                colorAutumnFlag = 0

    def colorBone(self):
        if 'T' in self.CheckIfElementPresent():

            global colorBoneFlag
            colorBoneFlag = colorBoneFlag + 1

            self.ResetFlag('B')
            if colorBoneFlag == 1:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1]
                self.ed = cv2.applyColorMap(name, cv2.COLORMAP_BONE)
                re = MyApp.ResizeMyImage(self, self.ed, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.ed)
                Undo.append(ed)

            else:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1 - 1]
                self.ed = name
                re = MyApp.ResizeMyImage(self, self.ed, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.ed)
                Undo[name1] = ed
                colorBoneFlag = 0

    def colorJet(self):
        if 'T' in self.CheckIfElementPresent():

            global colorJetFlag
            colorJetFlag = colorJetFlag + 1

            self.ResetFlag('J')
            if colorJetFlag == 1:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1]
                self.ed = cv2.applyColorMap(name, cv2.COLORMAP_JET)
                re = MyApp.ResizeMyImage(self, self.ed, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.ed)
                Undo.append(ed)

            else:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1 - 1]
                self.ed = name
                re = MyApp.ResizeMyImage(self, self.ed, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.ed)
                Undo[name1] = ed
                colorJetFlag = 0

    def colorWinter(self):
        if 'T' in self.CheckIfElementPresent():

            global colorWinterFlag
            colorWinterFlag = colorWinterFlag + 1

            self.ResetFlag('W')
            if colorWinterFlag == 1:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1]
                self.ed = cv2.applyColorMap(name, cv2.COLORMAP_WINTER)
                re = MyApp.ResizeMyImage(self, self.ed, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.ed)
                Undo.append(ed)

            else:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1 - 1]
                self.ed = name
                re = MyApp.ResizeMyImage(self, self.ed, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.ed)
                Undo[name1] = ed
                colorWinterFlag = 0

    def colorRainbow(self):
        if 'T' in self.CheckIfElementPresent():

            global colorRainbowFlag
            colorRainbowFlag = colorRainbowFlag + 1

            self.ResetFlag('R')
            if colorRainbowFlag == 1:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1]
                self.ed = cv2.applyColorMap(name, cv2.COLORMAP_RAINBOW)
                re = MyApp.ResizeMyImage(self, self.ed, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.ed)
                Undo.append(ed)

            else:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1 - 1]
                self.ed = name
                re = MyApp.ResizeMyImage(self, self.ed, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.ed)
                Undo[name1] = ed
                colorRainbowFlag = 0

    def colorOcean(self):
        if 'T' in self.CheckIfElementPresent():

            global colorOceanFlag
            colorOceanFlag = colorOceanFlag + 1

            self.ResetFlag('O')
            if colorOceanFlag == 1:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1]
                self.ed = cv2.applyColorMap(name, cv2.COLORMAP_OCEAN)
                re = MyApp.ResizeMyImage(self, self.ed, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.ed)
                Undo.append(ed)

            else:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1 - 1]
                self.ed = name
                re = MyApp.ResizeMyImage(self, self.ed, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.ed)
                Undo[name1] = ed
                colorOceanFlag = 0

    def colorSummer(self):
        if 'T' in self.CheckIfElementPresent():

            global colorSummerFlag
            colorSummerFlag = colorSummerFlag + 1

            self.ResetFlag('U')
            if colorSummerFlag == 1:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1]
                self.ed = cv2.applyColorMap(name, cv2.COLORMAP_SUMMER)
                re = MyApp.ResizeMyImage(self, self.ed, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.ed)
                Undo.append(ed)

            else:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1 - 1]
                self.ed = name
                re = MyApp.ResizeMyImage(self, self.ed, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.ed)
                Undo[name1] = ed
                colorSummerFlag = 0

    def colorSpring(self):
        if 'T' in self.CheckIfElementPresent():

            global colorSpringFlag
            colorSpringFlag = colorSpringFlag + 1

            self.ResetFlag('S')
            if colorSpringFlag == 1:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1]
                self.ed = cv2.applyColorMap(name, cv2.COLORMAP_SPRING)
                re = MyApp.ResizeMyImage(self, self.ed, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.ed)
                Undo.append(ed)

            else:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1 - 1]
                self.ed = name
                re = MyApp.ResizeMyImage(self, self.ed, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.ed)
                Undo[name1] = ed
                colorSpringFlag = 0

    def colorCool(self):
        if 'T' in self.CheckIfElementPresent():

            global colorCoolFlag
            colorCoolFlag = colorCoolFlag + 1

            self.ResetFlag('C')
            if colorCoolFlag == 1:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1]
                self.ed = cv2.applyColorMap(name, cv2.COLORMAP_COOL)
                re = MyApp.ResizeMyImage(self, self.ed, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.ed)
                Undo.append(ed)

            else:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1 - 1]
                self.ed = name
                re = MyApp.ResizeMyImage(self, self.ed, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.ed)
                Undo[name1] = ed
                colorCoolFlag = 0

    def colorHsv(self):
        if 'T' in self.CheckIfElementPresent():

            global colorHsvFlag
            colorHsvFlag = colorHsvFlag + 1

            self.ResetFlag('H')
            if colorHsvFlag == 1:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1]
                self.ed = cv2.applyColorMap(name, cv2.COLORMAP_HSV)
                re = MyApp.ResizeMyImage(self, self.ed, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.ed)
                Undo.append(ed)

            else:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1 - 1]
                self.ed = name
                re = MyApp.ResizeMyImage(self, self.ed, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.ed)
                Undo[name1] = ed
                colorHsvFlag = 0

    def colorPink(self):
        if 'T' in self.CheckIfElementPresent():

            global colorPinkFlag
            colorPinkFlag = colorPinkFlag + 1

            self.ResetFlag('P')
            if colorPinkFlag == 1:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1]
                self.ed = cv2.applyColorMap(name, cv2.COLORMAP_PINK)
                re = MyApp.ResizeMyImage(self, self.ed, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.ed)
                Undo.append(ed)

            else:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1 - 1]
                self.ed = name
                re = MyApp.ResizeMyImage(self, self.ed, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.ed)
                Undo[name1] = ed
                colorPinkFlag = 0

    def colorHot(self):
        if 'T' in self.CheckIfElementPresent():

            global colorHotFlag
            colorHotFlag = colorHotFlag + 1

            self.ResetFlag('T')
            if colorHotFlag == 1:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1]
                self.ed = cv2.applyColorMap(name, cv2.COLORMAP_HOT)
                re = MyApp.ResizeMyImage(self, self.ed, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.ed)
                Undo.append(ed)

            else:
                bla, name1 = self.CheckIfElementPresent()
                name = Undo[name1 - 1]
                self.ed = name
                re = MyApp.ResizeMyImage(self, self.ed, self.Width, self.Height)
                self.pixmap = QtGui.QPixmap(re)
                self.label1.setAutoFillBackground(True)
                self.label1.setPixmap(self.pixmap)
                ed = np.asarray(self.ed)
                Undo[name1] = ed
                colorHotFlag = 0


    def SaveFile(self):

        try:
            fileName = QFileDialog.getSaveFileName(self,"Save Image File", os.getenv("HOME"))
            len1 = len(Undo)
            fileName = fileName[0]+'.jpg'
            img = Undo[len1-1]
            #img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
            cv2.imwrite(fileName,img)
        except:
            print("No save data")

colorAutumnFlag = 0
colorBoneFlag = 0
colorJetFlag = 0
colorWinterFlag = 0
colorRainbowFlag = 0
colorOceanFlag = 0
colorSummerFlag = 0
colorSpringFlag = 0
colorCoolFlag = 0
colorHsvFlag = 0
colorPinkFlag = 0
colorHotFlag = 0

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    screen = app.primaryScreen()
    rect = screen.availableGeometry()
    Height = rect.height()
    Width = rect.width()
    window = MyApp(MainWindow,Height,Width)
    window.setWindowTitle("Image Editor")
    window.show()
    sys.exit(app.exec_())