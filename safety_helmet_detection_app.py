import streamlit as st
from models.yolo_v10.detector import inference
from config.model_config import Detector_Config


@st.cache_data(max_entries=1000)
def process_inference(image_path):
    result_img = inference(
        image_path,
        weight_path=Detector_Config().weight_path
    )

    return result_img


def main():
    st.set_page_config(
        page_title="Project Module 1 - YOLOv10 Detection Demo - AIO 2024",
        layout="wide"
    )

    st.title(':sparkles: :blue[Project Module 1 - YOLOv10] Detection Demo')
    st.text('Model: Fine tuning Pre-trained YOLOv10 with Safety Helmet Detection')

    uploaded_img = st.file_uploader('__Input your image__', type=['jpg', 'jpeg', 'png'])
    example_button = st.button('Run example')

    st.divider()

    if example_button:
        result_img = process_inference('static/example_img3.jpg')
    elif uploaded_img:
        result_img = process_inference(uploaded_img)
    else:
        result_img = None

    if result_img is not None:
        st.markdown('**Detection result**')
        st.image(result_img)


if __name__ == '__main__':
    main()
