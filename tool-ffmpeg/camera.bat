ffmpeg -f dshow -i video="USB2.0 Camera" -vcodec libx264 -preset:v ultrafast -tune:v zerolatency -f flv rtmp://180.201.3.195:1935/rtmplive/123

pause