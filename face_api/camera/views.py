from django.shortcuts import render
from django.views import View
from django.http import HttpResponse , StreamingHttpResponse ,request


from .camera import VideoCamera
from .camera2 import VideoCamera2



def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def camera_live(request):
    try:
        return StreamingHttpResponse(gen(VideoCamera2()), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  
        pass

class Camera(View):
    template_name = 'camera.html'
    word = 'MVOGO World'

    def get(self, request):
        context = {
            'data': self.word
        }
        return render(request, self.template_name, context)