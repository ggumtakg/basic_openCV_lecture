import cv2
import numpy as np

#opencv 기본 함수들
#imread : 파일 읽기 매개변수로 색생맵 등의 설정가능
img = cv2.imread('Lenna.png')
gray = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE)
bgr = cv2.imread('Lenna.png', cv2.IMREAD_COLOR_BGR)
rgb = cv2.imread('Lenna.png', cv2.IMREAD_COLOR_RGB)

#imshow : 파일 보여주기, 코랩 등의 환경에서는 plt.show 등을 활용
cv2.imshow('img', img)
cv2.imshow('gray', gray)
cv2.imshow('bgr', bgr)
cv2.imshow('rgb', rgb)

#imwrite : 파일 쓰기, opencv에서 한글의 사용은 제한되니 주의
cv2.imwrite('color_img.jpg', img)
cv2.imwrite('gray_img.jpg', gray)

cv2.imshow('saved_color_img', cv2.imread('color_img.jpg'))
cv2.imshow('saved_gray_img', cv2.imread('gray_img.jpg'))

#cvtColor : 색상맵 변경, 채널에 유의
#색상맵으로는 BGR, RGB, HSV, LAB, YCrCb, GRAY 등이 있습니다.
img_BGR_2_YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
img_YCrCb_2_BGR = cv2.cvtColor(img_BGR_2_YCrCb, cv2.COLOR_YCrCb2BGR)

psnr_origorig = cv2.PSNR(img, img)
print(psnr_origorig)
psnr = cv2.PSNR(img, img_YCrCb_2_BGR)

cv2.imshow(f'YCrCb_img, {psnr:.2f}', img_BGR_2_YCrCb)
cv2.imshow('YCrCb2BGR', img_YCrCb_2_BGR)
cv2.imwrite(f'YCrCb_img, {psnr:.2f}.jpg', img_BGR_2_YCrCb)
cv2.imwrite('YCrCb2BGR.jpg', img_YCrCb_2_BGR)

#VideoCapture : 카메라 영상입력
capture = cv2.VideoCapture(2)
ret, frame = capture.read()

cv2.imshow('camera_input', frame)
cv2.imwrite('camera_input.jpg', frame)

#resize : 크기조정
resized = cv2.resize(img, (300, 250))
h, w = resized.shape[:2]
resized_fit = cv2.resize(img, (w, h))

#rotate : 회전
resized_rotate = cv2.rotate(resized_fit, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow('resized', resized)
cv2.imshow('resized_rotate', resized_rotate)

cv2.imwrite('resized.jpg', resized)
cv2.imwrite('resized_rotate.jpg', resized_rotate)

#그리기 기능들
blank = 255*np.ones((600, 600, 3), dtype=np.uint8)

cv2.line(blank, (50, 50), (500, 500), (255, 0, 0), 3) #선, || 그릴곳, 시작점, 끝날점, 색, 두께
cv2.rectangle(blank, (100, 100), (300, 300), (0, 255, 0), 2)    #네모, || 그릴곳, 왼쪽위 꼭짓점, 오른쪽아래 꼭짓점, 색, 두께
cv2.circle(blank, (250, 250), 100, (0, 0, 255), -1) #원, || 그릴곳, 중심좌표, 반지름, 두께(-1이면 채움)
cv2.putText(blank, 'Hello OpenCV!', (50,400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)    #글자채우기 || 그릴곳, 문자열, 시작좌표, 폰트종류, 크기, 색, 두께, 선종류(옵션)

cv2.imshow('Drawing', blank)
cv2.imwrite('drawing.jpg', blank)

#기타 기능들
blur = cv2.GaussianBlur(img, (7, 7), 0) #가우시안블러, || 입력, 커널크기(보통 홀수), 표준편차
edges = cv2.Canny(img, 100, 200)    #canny 엣지검출, || 입력, 낮은 임계값, 높은임계값(보통 낮은 임계값의 2~3배)

cv2.imshow('blur', blur)
cv2.imshow('edges', edges)
cv2.imwrite('blur.jpg', blur)
cv2.imwrite('edges.jpg', edges)

#이미지 압축률
cv2.imwrite('compressed_png.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])    #png압축, 0~9 숫자가 높을수록 더 압축
cv2.imwrite('compressed_90.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])   #jpg압축, 0~100 숫자가 낮을수록 더 압축
cv2.imwrite('compressed_50.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 50])

cv2.waitKey(0)

cv2.destroyAllWindows()