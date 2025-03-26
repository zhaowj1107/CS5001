"""
File: card_image_processor.py
Author: Weijian Zhao(David)
Date: 2025-03-26
Class: CS_5001, Spring_2025
Description: 
Final Project
"""
import cv2 as cv


class ImageProcessor():
    def __init__(self, image_file):
        self.image = cv.imread(image_file)
        if self.image is None:
            print("错误：无法加载图像，请检查路径是否正确。")
            exit()
        self.rgb = cv.cvtColor(self.image, cv.COLOR_BGR2RGB)
        
    def __str__(self):
        print("Here is the tensor of BGR\n", self.image,"\n\n")
        print("Here is the tensor of BGR\n", self.rgb,"\n\n")

# 检查图像是否成功读取

    def show_image(self):
        cv.imshow("Display Image", self.image)
        cv.waitKey(0)
        cv.destroyAllWindows()


    def Grayscale_conversion(self):
        pass

    
    def Brightness_adjustment(self, adjust = 0):
        pass

    
    def colour_isolation(self):
        pass
    
    def image_flip(self):
        pass

    def contrast_enhance(self):
        pass

    def card_regonition(self):
    

    

if __name__ == "__main__":
    image_file = "./cat.jpg"
    image = ImageProcessor(image_file)
    image.show_image()