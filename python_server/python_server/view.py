from django.http import HttpResponse
from PIL import Image
import algo.dHash as dh


def hello(request):
    img1 = Image.open('/Users/zhangjie/Desktop/1.png')
    img2 = Image.open('/Users/zhangjie/Desktop/2.png')
    sim = dh.caldHashSimilarity(img1, img2)
    diff = float(sim)/64
    print('{}'.format(diff))
    return HttpResponse("Hello world ! {}".format(diff) )
