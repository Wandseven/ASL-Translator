import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from keras.models import load_model

# import Opencv module
import cv2
import numpy as np
from ui_main_window import *

classifier = load_model('Trained_model43.h5')

image_x, image_y = 64,64


def predictor():
    import numpy as np
    from keras.preprocessing import image
    test_image = image.load_img('1.png', target_size=(64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = classifier.predict(test_image)

    if result[0][0] == 1:
        return 'A'
    elif result[0][1] == 1:
        return 'America'
    elif result[0][2] == 1:
        return 'B'
    elif result[0][3] == 1:
        return 'C'
    elif result[0][4] == 1:
        return 'D'
    elif result[0][5] == 1:
        return 'E'
    elif result[0][6] == 1:
        return 'F'
    elif result[0][7] == 1:
        return 'G'
    elif result[0][8] == 1:
        return 'H'
    elif result[0][9] == 1:
        return 'I'
    elif result[0][10] == 1:
        return 'J'
    elif result[0][11] == 1:
        return 'K'
    elif result[0][12] == 1:
        return 'L'
    elif result[0][13] == 1:
        return 'M'
    elif result[0][14] == 1:
        return 'N'
    elif result[0][15] == 1:
        return 'O'
    elif result[0][16] == 1:
        return 'P'
    elif result[0][17] == 1:
        return 'Q'
    elif result[0][18] == 1:
        return 'R'
    elif result[0][19] == 1:
        return 'S'
    elif result[0][20] == 1:
        return 'T'
    elif result[0][21] == 1:
        return 'U'
    elif result[0][22] == 1:
        return 'V'
    elif result[0][23] == 1:
        return 'W'
    elif result[0][24] == 1:
        return 'X'
    elif result[0][25] == 1:
        return 'Y'
    elif result[0][26] == 1:
        return 'add'
    elif result[0][27] == 1:
        return 'about'
    elif result[0][28] == 1:
        return 'Z'
    elif result[0][29] == 1:
        return 'all'
    elif result[0][30] == 1:
        return 'begin'
    elif result[0][31] == 1:
        return 'birthday'
    elif result[0][32] == 1:
        return 'butterfly'
    elif result[0][33] == 1:
        return 'call me'
    elif result[0][34] == 1:
        return 'city'
    elif result[0][35] == 1:
        return 'deserve'
    elif result[0][36] == 1:
        return 'football'
    elif result[0][37] == 1:
        return 'love'
    elif result[0][38] == 1:
        return 'my'
    elif result[0][39] == 1:
        return 'name'
    elif result[0][40] == 1:
        return 'pray'
    elif result[0][41] == 1:
        return 'stop'
    elif result[0][42] == 1:
        return 'time out'

def nothing(x):
    pass



cv2.namedWindow("Trackbars")

cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 30, 179, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)



class MainWindow(QWidget):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.count = 0
        self.prev_text = None
        self.to_print = []

        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function
        self.ui.Startbtn.clicked.connect(self.controlTimer)
        self.ui.Probtn.clicked.connect(QtWidgets.qApp.quit)

    def viewCam(self):
        # read image in BGR format
        image_x, image_y = 64, 64
        img_text = ''

        _, image = self.cap.read()
        image = cv2.flip(image, 1)

        l_h = cv2.getTrackbarPos("L - H", "Trackbars")
        l_s = cv2.getTrackbarPos("L - S", "Trackbars")
        l_v = cv2.getTrackbarPos("L - V", "Trackbars")
        u_h = cv2.getTrackbarPos("U - H", "Trackbars")
        u_s = cv2.getTrackbarPos("U - S", "Trackbars")
        u_v = cv2.getTrackbarPos("U - V", "Trackbars")

        img = cv2.rectangle(image, (220, 220), (420, 420), (0, 255, 0), thickness=2, lineType=8, shift=0)
        imcrop = img[222:418, 222:418]
        lower_blue = np.array([l_h, l_s, l_v])
        upper_blue = np.array([u_h, u_s, u_v])
        hsv = cv2.cvtColor(imcrop, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        #cv2.imshow("mask", mask)
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img_name = "1.png"
        save_img = cv2.resize(mask, (image_x, image_y))
        cv2.imwrite(img_name, save_img)

        print("{} written!".format(img_name))

        img_text = predictor()
        cv2.putText(image, img_text, (30, 400), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (0, 255, 0))
        # get image infos
        height1, width1 = mask.shape
        height, width, channel = image.shape
        step = channel * width
        step1 = 1 * width1
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        qImg1 = QImage(mask.data, width1, height1, step1, QImage.Format_Grayscale8)
        # show image in img_label
        self.ui.camera.setPixmap(QPixmap.fromImage(qImg))
        self.ui.mask.setPixmap(QPixmap.fromImage(qImg1))

        blank_image = 255 * np.zeros(shape=[60, 1200, 3], dtype=np.uint8)
        # print(blank_image.shape)
        # so sánh frame đầu và frame sau, nếu đủ 30 frame thì xuất ra chữ cái hay từ
        if self.prev_text == img_text:
            self.count += 1
            if self.count == 30:
                self.to_print.append(img_text)
        else:
            self.count = 0
        self.prev_text = img_text
        # Khoảng cách mỗi chữ là 70, chưa biết rõ cho lắm về những thông số Khác
        for (index, char) in enumerate(self.to_print):
            cv2.putText(blank_image, char, (70 * index, 40), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 255, 255))

        if len(self.to_print) >= 15:
            self.to_print[:] = []

        height2, width2, channel2 = blank_image.shape
        step2 = channel2 * width2
        qImg2 = QImage(blank_image.data, width2, height2, step2, QImage.Format_RGB888)
        self.ui.result.setPixmap(QPixmap.fromImage(qImg2))


    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # start timer
            self.timer.start(20)
            # update control_bt text
            self.ui.Startbtn.setText("Stop")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
            self.ui.Startbtn.setText("Start")




if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())