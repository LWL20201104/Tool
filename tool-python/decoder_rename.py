import os

input_dir = 'D:/iSpace/毕业论文/draw/video-splice/yuv/'
output_dir = 'D:/iSpace/毕业论文/draw/video-splice/mp4/'

file_names = os.listdir(input_dir)
bps = ['1000k', '800k', '700k', '500k', '300k', '100k']

for file_name in file_names:
    for bp in bps:
        os.system('ffmpeg -s 640x480 -pix_fmt yuv420p -r 30 -i ' + input_dir + file_name + ' -b:v ' + bp + 
        ' -vcodec h264 ' + output_dir + bp + '/' + file_name[:-4] + '.mp4')

    # os.system('ffmpeg -s 640x480 -pix_fmt yuv420p -r 30 -i ' + input_dir + file_name + 
    # ' -b:v 2400k -vcodec h264 ' + output_dir + '2400kbps_' + file_name[:29] + '.mp4')


# outfile_dir = 'D:/Apache24/htdocs/video-vr/AerialCity_6x4_Segment/2400/'
# file_names = os.listdir(output_dir)
# for file_name in file_names:
#     os.rename(output_dir + file_name, outfile_dir + file_name[:28] + str(int(file_name[28]) + 15) + file_name[29:])

os.system('pause')

# os.system('ffmpeg -s 640x480 -pix_fmt yuv420p -r 30 -i ' + input_dir + file_name + '.yuv' + ' -b:v 50k -vcodec h264 ' + output_dir + file_name + '_50.mp4')