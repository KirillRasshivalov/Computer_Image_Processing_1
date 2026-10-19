import cv2
import time


def median_filter_biblio(image_name, k):
    img = cv2.imread(image_name)
    if img is None:
        raise ValueError(f"Не удалось загрузить изображение: {image_name}")
    out = cv2.medianBlur(img, k)
    cv2.imwrite("opencv_median.png", out)
    return out


def median_of_list(values):
    values = sorted(values)
    return values[len(values) // 2]


def median_filter_mine(image_name, k):
    img = cv2.imread(image_name)
    if img is None:
        raise ValueError(f"Не удалось загрузить изображение: {image_name}")
    r = k // 2
    h, w, c = img.shape
    out = img.copy()
    for y in range(h):
        for x in range(w):
            for ch in range(c):
                window = []
                for dy in range(-r, r + 1):
                    for dx in range(-r, r + 1):
                        yy = min(max(y + dy, 0), h - 1)
                        xx = min(max(x + dx, 0), w - 1)
                        window.append(int(img[yy, xx, ch]))
                out[y, x, ch] = median_of_list(window)
    cv2.imwrite("mine_median.png", out)
    return out

if __name__ == '__main__':
    print("Введите название изображения: ", end="")
    img = input()
    print("Введите переменную k - в какой окрестности будет выбираться медиана (k должно быть нечетное).")
    k = 0
    while k % 2 == 0:
        print("k = ", end="")
        k = int(input())
        if k % 2 == 0:
            print("k должно быть нечетным.")

    t0 = time.perf_counter()
    median_filter_biblio(img, k)
    t_lib = time.perf_counter() - t0

    t0 = time.perf_counter()
    median_filter_mine(img, k)
    t_native = time.perf_counter() - t0

    print(f"OpenCV: {t_lib}")
    print(f"Mine: {t_native}")




