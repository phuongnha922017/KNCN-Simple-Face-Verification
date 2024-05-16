import cv2
from deepface import DeepFace
import streamlit as st
import threading
import time

capture = False
def getReference():
    frame_placeholder = st.empty()
    cap = cv2.VideoCapture(0)
    countdown = 3
    counter = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.write("Video Capture Ended")
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        cv2.putText(frame, str(countdown), (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
            
        if counter % 30 == 0:
            countdown -= 1
        counter += 1
        frame_placeholder.image(frame,channels="RGB")
        if countdown == 0:
            cv2.imwrite('reference.jpg', frame)
            break
    frame_placeholder.title('Lấy dữ liệu thành công')
    cap.release()
    
    cv2.destroyAllWindows()

def app():
    st.button("Chụp hình", on_click=getReference)
    

    
