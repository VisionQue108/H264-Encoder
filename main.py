import cv2
import os
from threading import Thread,Lock
from time import sleep

from gi.repository import Gst, GLib
import gi
gi.require_version("Gst", "1.0")

file_lock=Lock()

vid=cv2.VideoCapture(0)


def frame_capture():
        
        frame_width=int(vid.get(3))
        frame_height =int(vid.get(4))
        size = (frame_width, frame_height)
        result = cv2.VideoWriter('/home/nae1972/camera_ws/src/camera_node/outputfile/output.avi',cv2.VideoWriter_fourcc(*'MJPG'),10, size)

        try:          
            while (True):
                flag, frame =vid.read() 
                x = frame_width/2
                y = frame_height/2 
                text_color = (255,0,0) 
                #Acquiring lock before writing
                with file_lock:
                        result.write(frame) #write to the video file
        except KeyboardInterrupt:
            Gst.init()
            gstreamer_loop =GLib.MainLoop()
            gstreamer_loop_thread= Thread(target=gstreamer_loop.run)
            gstreamer_loop_thread.start()
            print("Conversion has started!")
            pipeline = Gst.parse_launch("filesrc location=output.avi ! avidemux ! theoradec ! x264enc ! filesink location=/home/nae1972/camera_ws/src/camera_node/outputfile/output.h264")
            pipeline.set_state(Gst.State.PLAYING)

            conv_status=os.path.exists("/home/nae1972/camera_ws/src/camera_node/outputfile/output.h264")
            while conv_status==False:
                 sleep(0.1)
            pass

            pipeline.set_state(Gst.State.NULL)
            gstreamer_loop.quit()
            gstreamer_loop_thread.join()
            print("Conversion Successful!")
        file_lock.release()
frame_capture()





