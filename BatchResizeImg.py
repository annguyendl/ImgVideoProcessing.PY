import cv2
import glob

images = glob.glob("./resources/*.jpg")

for image in images:
    img = cv2.imread(image, 1)
    resized_img = cv2.resize(img, (100, 100))
    cv2.imshow("Review", resized_img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
    re_imgpath = "./results/resized_" + image.split("\\")[-1]
    print(re_imgpath)
    cv2.imwrite(re_imgpath, resized_img)
