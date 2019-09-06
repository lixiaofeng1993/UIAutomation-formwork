from urllib import request
import pytesseract
from PIL import Image

path = '../error_img/code.jpeg'
save_path = '../error_img/code1.jpg'


def show_code(code_url, img_path=path):
    """显示验证码"""
    request.urlretrieve(code_url, img_path)
    img = Image.open(path)
    img.show()
    img.close()

# def get_code(img_path=path):
#
#     """
#         得到验证码
#     """
#     try:
#         img = Image.open(img_path)
#         img.convert('L')
#         return pytesseract.image_to_string(img)
#     except Exception as error:
#         return ''

# data = get_code()


# def get_code1(img_path=path):
#
#     """
#         得到验证码
#     """
#     try:
#         img = Image.open(img_path)
#         after_deal = img.convert('L')
#         last = after_deal.point(lambda x: 0 if x < 1 else 255, '1')
#         last.save('ok.jpg')
#         img = Image.open(save_path)
#         img.show()
#         # return pytesseract.image_to_string(last)
#     except Exception as error:
#         return ''
# get_code1()
