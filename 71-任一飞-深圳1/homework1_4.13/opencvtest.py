import cv2

# 灰度化
def grayscale(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray


# 二值化
def binary(image):
    gray = grayscale(image)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    return binary


# 读取图像
def load_image(image_path):
    img = cv2.imread(image_path)
    return img


# 显示图像
def show_image(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    img = load_image('lenna.png')
    gray = grayscale(img)
    binary = binary(img)
    show_image('Original Image', img)
    show_image('Gray Image', gray)
    show_image('Binary Image', binary)




