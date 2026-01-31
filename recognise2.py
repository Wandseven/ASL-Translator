import cv2
import numpy as np

def nothing(x):
    pass

image_x, image_y = 64,64

from keras.models import load_model
classifier = load_model('Trained_model43.h5')

def predictor():
    import numpy as np
    from keras.preprocessing import image
    test_image = image.load_img('1.png', target_size=(64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
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
       
  
cam = cv2.VideoCapture(0)

cv2.namedWindow("Trackbars")

cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 30, 179, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)

cv2.namedWindow("test")

img_counter = 0

img_text = ''

count = 0
axis_x = 0
axis_y = 40

global prev_text
prev_text = None

to_print = []

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,1)
    l_h = cv2.getTrackbarPos("L - H", "Trackbars")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")


    img = cv2.rectangle(frame, (220,220),(420,420), (0,255,0), thickness=2, lineType=8, shift=0)

    lower_blue = np.array([l_h, l_s, l_v])
    upper_blue = np.array([u_h, u_s, u_v])
    imcrop = img[222:418, 222:418]
    hsv = cv2.cvtColor(imcrop, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    cv2.putText(frame, img_text, (30, 400), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (0, 255, 0))
    cv2.imshow("test", frame)
    cv2.imshow("mask", mask)

    # black blank image, chiều rộng là 900, chiều cao là 60, dạng dữ liệu là numpy array
    blank_image =255 * np.zeros(shape=[ 60, 1200, 3], dtype=np.uint8)
    # print(blank_image.shape)
    # so sánh frame đầu và frame sau, nếu đủ 30 frame thì xuất ra chữ cái hay từ    
    if prev_text == img_text:
        #cv2.putText(blank_image, img_text, (axis_x, axis_y), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 255))
        count = count + 1
        if count == 30:
            to_print.append(img_text)
    else:
        count = 0

    prev_text = img_text
    for (index, char) in enumerate(to_print):
        cv2.putText(blank_image, char, (70*index, axis_y), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 255, 255))
    #Số chữ cái và từ là 15 trong một hàng, nếu nó đầy thì sẽ tự động reset 
    if len(to_print) >= 15:
        to_print[:] = []
        
    cv2.imshow("Black image",blank_image)
    
    #if cv2.waitKey(1) == ord('c'):
        
    img_name = "1.png"
    save_img = cv2.resize(mask, (image_x, image_y))
    cv2.imwrite(img_name, save_img)
    print("{} written!".format(img_name))

    print(count) 

    img_text = predictor()
        

    if cv2.waitKey(1) == 27:
        break


cam.release()
cv2.destroyAllWindows()
