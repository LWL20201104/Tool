import os

os.system('ffmpeg \
-i 0.mp4 \
-i 1.mp4 \
-i 2.mp4 \
-i 3.mp4 \
-i 4.mp4 \
-i 5.mp4 \
-i 6.mp4 \
-i 7.mp4 \
-i 8.mp4 \
-i 9.mp4 \
-i 10.mp4 \
-i 11.mp4 \
-i 12.mp4 \
-i 13.mp4 \
-i 14.mp4 \
-i 15.mp4 \
-i 16.mp4 \
-i 17.mp4 \
-i 18.mp4 \
-i 19.mp4 \
-i 20.mp4 \
-i 21.mp4 \
-i 22.mp4 \
-i 23.mp4 \
-filter_complex "[0:v]pad=iw*6:ih*4[a1];[a1][1:v]overlay=w[b1];[b1][2:v]overlay=w*2[c1];[c1][3:v]overlay=w*3[d1];[d1][4:v]overlay=w*4[e1];[e1][5:v]overlay=w*5[out1];\
[out1][6:v]overlay=0:h[a2];[a2][7:v]overlay=w:h[b2];[b2][8:v]overlay=w*2:h[c2];[c2][9:v]overlay=w*3:h[d2];[d2][10:v]overlay=w*4:h[e2];[e2][11:v]overlay=w*5:h[out2];\
[out2][12:v]overlay=0:h*2[a3];[a3][13:v]overlay=w:h*2[b3];[b3][14:v]overlay=w*2:h*2[c3];[c3][15:v]overlay=w*3:h*2[d3];[d3][16:v]overlay=w*4:h*2[e3];[e3][17:v]overlay=w*5:h*2[out3];\
[out3][18:v]overlay=0:h*3[a4];[a4][19:v]overlay=w:h*3[b4];[b4][20:v]overlay=w*2:h*3[c4];[c4][21:v]overlay=w*3:h*3[d4];[d4][22:v]overlay=w*4:h*3[e4];[e4][23:v]overlay=w*5:h*3" \
splice_video.mp4')

os.system('pause')

