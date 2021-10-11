import cv2, time, pandas
from datetime import date, datetime

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
bckgrd = None

#
status_list = [None, None]
times = []
df = pandas.DataFrame(columns=["Start", "End"])

#Waiting 2 second before capture static background
time.sleep(2)

while True:
    check, frame = video.read()
    status = 0
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_img = cv2.GaussianBlur(gray_img, (21, 21), 0)

    #Set background static image
    if bckgrd is None:
        bckgrd = gray_img
        continue

    #Compare motion frame with background
    delta_frame =cv2.absdiff(bckgrd, gray_img)

    #Calculate threshold and dilate for smoothly threshold frame with black and white
    threshold_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    threshold_frame = cv2.dilate(threshold_frame, None, iterations=2)

    #Find contour and store in tuble
    (cnts,_) = cv2.findContours(threshold_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        #Only detect object larger than approxiate 100*100 pixels
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1

        #Find boudary and draw rectangle
        (x, y, w, h) = cv2.boundingRect(contour)
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h),
        (0, 255, 0), 2)
        #Add comment to frame
        frame = cv2.putText(frame, "Press \'q\' to exit", (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, 255)
    
    #If status changed then add timestamp to MotionDetectingResults
    status_list.append(status)
    status_list = status_list[-2:]
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())
    if status_list[-1]==1 and (status_list[-2]==0 or status_list[-2] is None):
        times.append(datetime.now())
        
    cv2.imshow("Detecting motion", frame)
    cv2.imshow("Delta frame", delta_frame)
    cv2.imshow("Threshhold frame", threshold_frame)

    key = cv2.waitKey(200)
    if key == ord('q'):
        if status==1:
            times.append(datetime.now())
        break

print(status_list)
print(times)

video.release()
cv2.destroyAllWindows()

#Write motion detecting data to result file
for i in range(0, len(times), 2):
    df = df.append({"Start":times[i], "End":times[i+1]}, ignore_index=True)

print(df)
df.to_csv("./results/MotionDetectingResults.csv")