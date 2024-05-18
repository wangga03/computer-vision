import cv2 as cv

def main(capture) :

    while True :
        ret, frame = capture.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow("frame", gray)
        if cv.waitKey(1) & 0xFF == ord('q') :
            break

    capture.release()
    cv.destroyAllWindows()
if __name__ == "__main__" :
    cap = cv.VideoCapture(0)

    main(cap)