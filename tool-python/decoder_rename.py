import os

input_dir = 'D:/Apache24/htdocs/video-vr/AerialCity_6x4_Segment/data-yuv/'
output_dir = 'D:/Apache24/htdocs/video-vr/AerialCity_6x4_Segment/data-encode/2400/'
# file_names = os.listdir(input_dir)
# for file_name in file_names:
#     os.system('ffmpeg -s 640x480 -pix_fmt yuv420p -r 30 -i ' + input_dir + file_name + 
#     ' -b:v 2400k -vcodec h264 ' + output_dir + '2400kbps_' + file_name[:29] + '.mp4')


outfile_dir = 'D:/Apache24/htdocs/video-vr/AerialCity_6x4_Segment/2400/'
file_names = os.listdir(output_dir)
for file_name in file_names:
    os.rename(output_dir + file_name, outfile_dir + file_name[:28] + str(int(file_name[28]) + 15) + file_name[29:])

os.system('pause')

# os.system('ffmpeg -s 640x480 -pix_fmt yuv420p -r 30 -i ' + input_dir + file_name + '.yuv' + ' -b:v 50k -vcodec h264 ' + output_dir + file_name + '_50.mp4')