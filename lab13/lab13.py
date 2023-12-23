import cv2
import numpy as np

Origin = cv2.imread("TW.jpg")  # 讀取圖片

cv2.imshow("Origin", Origin)  # 顯示原始圖片
cv2.waitKey(0)
cv2.destroyAllWindows()

gray_cv2 = cv2.cvtColor(Origin, cv2.COLOR_BGR2GRAY)  # 將圖片轉換為灰階 (用cv2函式)
cv2.imshow("gray_cv2", gray_cv2)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray_other = np.dot(Origin[..., :3], [0.299, 0.587, 0.114]).astype(np.uint8)  # 使用非cv2函式(numpy)將圖片轉換為灰階
cv2.imshow("gray_other", gray_other)
cv2.waitKey(0)
cv2.destroyAllWindows()

_, binary = cv2.threshold(gray_cv2, 244, 255, cv2.THRESH_BINARY)  # 對圖片進行二值化處理
cv2.imshow("Binary", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()

