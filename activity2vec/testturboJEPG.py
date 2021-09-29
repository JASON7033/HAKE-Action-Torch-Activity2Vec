import cv2
from turbojpeg import TurboJPEG, TJPF_GRAY, TJSAMP_GRAY, TJFLAG_PROGRESSIVE, TJFLAG_FASTUPSAMPLE, TJFLAG_FASTDCT

# specifying library path explicitly
# jpeg = TurboJPEG(r'D:\turbojpeg.dll')
# jpeg = TurboJPEG('/usr/lib64/libturbojpeg.so')
# jpeg = TurboJPEG('/usr/local/lib/libturbojpeg.dylib')

# using default library installation
jpeg = TurboJPEG()# at sever there's no permission to install turboJPEG
#then in this project we download source code of turboJEPG  and use gcc command to gengerate *.so excutable file
#finally point out in obvious    jpeg=TurboJPEG('download/turbojpeg.so')


# decoding input.jpg to BGR array
in_file = open('input.jpg', 'rb')
bgr_array = jpeg.decode(in_file.read())
in_file.close()
cv2.imshow('bgr_array', bgr_array)
cv2.waitKey(0)

# decoding input.jpg to BGR array with fast upsample and fast DCT. (i.e. fastest speed but lower accuracy)
in_file = open('input.jpg', 'rb')
bgr_array = jpeg.decode(in_file.read(), flags=TJFLAG_FASTUPSAMPLE|TJFLAG_FASTDCT)
in_file.close()
cv2.imshow('bgr_array', bgr_array)
cv2.waitKey(0)

# direct rescaling 1/2 while decoding input.jpg to BGR array
in_file = open('input.jpg', 'rb')
bgr_array_half = jpeg.decode(in_file.read(), scaling_factor=(1, 2))
in_file.close()
cv2.imshow('bgr_array_half', bgr_array_half)
cv2.waitKey(0)

# getting possible scaling factors for direct rescaling
scaling_factors = jpeg.scaling_factors

# decoding JPEG image properties
in_file = open('input.jpg', 'rb')
width, height, jpeg_subsample, jpeg_colorspace = jpeg.decode_header(in_file.read())
in_file.close()

# decoding input.jpg to YUV array
in_file = open('input.jpg', 'rb')
buffer_array, plane_sizes = jpeg.decode_to_yuv(in_file.read())
in_file.close()

# decoding input.jpg to YUV planes
in_file = open('input.jpg', 'rb')
planes = jpeg.decode_to_yuv_planes(in_file.read())
in_file.close()

# encoding BGR array to output.jpg with default settings.
out_file = open('output.jpg', 'wb')
out_file.write(jpeg.encode(bgr_array))
out_file.close()

# encoding BGR array to output.jpg with TJSAMP_GRAY subsample.
out_file = open('output_gray.jpg', 'wb')
out_file.write(jpeg.encode(bgr_array, jpeg_subsample=TJSAMP_GRAY))
out_file.close()

# encoding BGR array to output.jpg with quality level 50.
out_file = open('output_quality_50.jpg', 'wb')
out_file.write(jpeg.encode(bgr_array, quality=50))
out_file.close()

# encoding BGR array to output.jpg with quality level 100 and progressive entropy coding.
out_file = open('output_quality_100_progressive.jpg', 'wb')
out_file.write(jpeg.encode(bgr_array, quality=100, flags=TJFLAG_PROGRESSIVE))
out_file.close()

# decoding input.jpg to grayscale array
in_file = open('input.jpg', 'rb')
gray_array = jpeg.decode(in_file.read(), pixel_format=TJPF_GRAY)
in_file.close()
cv2.imshow('gray_array', gray_array)
cv2.waitKey(0)

# scale with quality but leaves out the color conversion step
in_file = open('input.jpg', 'rb')
out_file = open('scaled_output.jpg', 'wb')
out_file.write(jpeg.scale_with_quality(in_file.read(), scaling_factor=(1, 4), quality=70))
out_file.close()
in_file.close()

# lossless crop image
out_file = open('lossless_cropped_output.jpg', 'wb')
out_file.write(jpeg.crop(open('input.jpg', 'rb').read(), 8, 8, 320, 240))
out_file.close()
