import cv2
from deepface import DeepFace
import streamlit as st


def verify():
    counter = 0
    match = False
    cap = cv2.VideoCapture(0)
    frame_placeholder = st.empty()
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.write("Video Capture Ended")
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if counter == 120:
            break
        if counter == 100:   
            try:
                frame_path = 'frame.jpg'
                reference_img_path = 'reference.jpg'
                cv2.imwrite(frame_path, frame)
                match =  DeepFace.verify(frame_path, reference_img_path, model_name='Facenet', distance_metric='cosine', normalization='Facenet')['verified']

            except ValueError:
                print(ValueError)
        if counter >= 100:
            if match:
                cv2.putText(frame, 'SUCCESS', (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            else:
                cv2.putText(frame, 'TRY AGAIN', (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        counter += 1
        frame_placeholder.image(frame,channels="RGB")
    if match:
        frame_placeholder.title('Xác thực thành công')
    else:
        frame_placeholder.title('Vui lòng thử lại ')
    cap.release()
    cv2.destroyAllWindows()

def app():
    st.button('Xác thực', on_click=verify)
    

