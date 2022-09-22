# python对比两张图片的不同

from PIL import Image
from PIL import ImageChops
import math
import operator
from functools import reduce


def compare_image(path_one, path_two, diff_save_location):
    """
    比较图片，如果有不同则生成展示不同的图片

    参数一，path_one，第一张图片的路径
    参数二，path_two，第二张图片的路径
    参数三，diff_save_location，不同图片的保存路径
    """

    image_one = Image.open(path_one)
    image_two = Image.open(path_two)

    histogram1 = image_one.histogram()
    histogram2 = image_two.histogram()

    result = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2, histogram1, histogram2)))/len(histogram1) )

    print(result)

    try:
        diff = ImageChops.difference(image_one,image_two)

        if diff.getbbox() is None:
            # 图片间没有任何不同，则退出
            print("[+] we are the same!")
            print(diff.getbbox())

        else:
            diff.save(diff_save_location)
            print(diff.getbbox())

    except ValueError as e:
        text = ("NULL!!")
        print("[{0}]{1}".format(e,text))

if __name__ == "__main__":
    compare_image('1.png', '2.png', '9999.png')
