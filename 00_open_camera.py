import cv2 as cv

def main(capture) :

    while True :
        ret, frame = capture.read()
        cv.imshow("frame", frame)
        if cv.waitKey(1) & 0xFF == ord('q') :
            break

    capture.release()
    cv.destroyAllWindows()
if __name__ == "__main__" :
    cap = cv.VideoCapture(0)
    main(cap)