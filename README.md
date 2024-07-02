# Helmet Safety Detection with YOLOv10 and Streamlit

Đây là ứng dụng sử dụng mô hình YOLOv10 để phát hiện việc đội mũ bảo hộ. Ứng dụng được triển khai bằng Streamlit. Dự án này được lấy từ kho mã nguồn: [YOLOv10_Streamlit_Demo](https://github.com/wjnwjn59/YOLOv10_Streamlit_Demo).

## Mục Lục

1. [Giới thiệu](#giới-thiệu)
2. [Yêu cầu](#yêu-cầu)
3. [Cài đặt](#cài-đặt)
4. [Chạy ứng dụng](#chạy-ứng-dụng)
5. [Sử dụng ứng dụng](#sử-dụng-ứng-dụng)
6. [Tài liệu tham khảo](#tài-liệu-tham-khảo)

## Giới thiệu

Ứng dụng này sử dụng mô hình YOLOv10 để phát hiện người đội mũ bảo hộ trong các hình ảnh. Ứng dụng được triển khai bằng Streamlit để tạo giao diện người dùng trực quan và dễ sử dụng.

## Yêu cầu

Để chạy ứng dụng này, bạn cần cài đặt các thư viện và công cụ sau:

- Python 3.10 (để cài được torch 2.0.1 do module models/yolo_v10 yêu cầu )
- Git
- Streamlit  
- Pytest & Pytest coverage
- Coverage
  
Dùng cho models/yolo_v10 
- Pytorch 
- Opencv-python
- ... (models/yolo_v10/requirements.txt)

project này chạy streamlit với model đã fine-tuning nên ko cần install các gói sau 
- onnx==1.14.0
- onnxruntime==1.15.1
- onnxsim==0.4.36
- onnxruntime-gpu==1.18.0

## Notebooks

vì train fine-tuning cho pre-trained model Yolov10 với data safety Helmet cần GPU nên phần này được run trên Colab
- YOLO v10 fine tuning using Helmet Safety Detection Dataset [<img src="images/colab-badge.svg">](https://colab.research.google.com/drive/1VskXvvN4A5aQ-H8GqCcu8kmGnMriAU_K?usp=sharing)
- YOLO v10 pre-trained inference [<img src="images/colab-badge.svg">](https://colab.research.google.com/drive/16h6HfIZhQQA5rrdUrkNorEJwA9SYKoAX?usp=sharing)


## Cài đặt

1. **Clone kho mã nguồn từ GitHub:**

    ```bash
    git clone https://github.com/AIO-441-nguyen-thi-kim-tuyen/yoloV10.git
    cd yoloV10
    ```

2. **Tạo môi trường ảo (tuỳ chọn nhưng được khuyến khích):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Trên Unix hoặc MacOS
    .\venv\Scripts\activate   # Trên Windows
    ```

3. **Cài đặt các thư viện cần thiết:**
   - Thư viện cần thiết cho module models/yolo_v10 (detect và load model fine-tuning)
        ```bash
        cd models/yolo_v10
        pip install -r requirements.txt
        pip install -e .
        ```
   - Thư viện cần thiết cho Streamlit app demo (thư mục gốc)

       ```bash
       pip install -r requirements.txt
       ```

## Chạy ứng dụng

1. **Khởi động ứng dụng Streamlit:**

    ```bash
    streamlit run safety_helmet_detection_app.py
    ```

    Ứng dụng sẽ tự động mở trong trình duyệt web mặc định của bạn tại địa chỉ `http://localhost:8501`.

## Sử dụng ứng dụng

1. **Tải ảnh lên:**

    Nhấn vào nút "Browse files" để tải lên ảnh mà bạn muốn kiểm tra.

2. **Chạy file ảnh ví dụ**
    Nhấn vào nút "Run example", ứng dụng sẽ tự động phát hiện và hiển thị các vùng chứa người đội mũ bảo hộ trong ảnh ví dụ của chương trình.

4. **Phát hiện mũ bảo hộ:**

    Ứng dụng sẽ tự động phát hiện và hiển thị các vùng chứa người đội mũ bảo hộ trong ảnh đã tải lên. Kết quả sẽ được hiển thị trực tiếp trên ảnh.

## Sonar Cloud 
### Sonar Cloud Project
[Link to Sonar Cloud](https://sonarcloud.io/project/configuration?id=AIO-441-nguyen-thi-kim-tuyen_yoloV10)
[New code Summaty]((https://sonarcloud.io/summary/new_code?id=AIO-441-nguyen-thi-kim-tuyen_yoloV10))
### SonarCloud Status

[Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=AIO-441-nguyen-thi-kim-tuyen_yoloV10&metric=alert_status)

[Alert Status](https://sonarcloud.io/api/project_badges/measure?project=AIO-441-nguyen-thi-kim-tuyen_yoloV10&metric=alert_status)

## Tài liệu tham khảo

- [YOLOv10_Streamlit_Demo trên GitHub](https://github.com/wjnwjn59/YOLOv10_Streamlit_Demo)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [YOLO: Real-Time Object Detection](https://pjreddie.com/darknet/yolo/)
- [YOLOv10_Streamlit_Demo](https://github.com/wjnwjn59/YOLOv10_Streamlit_Demo)

