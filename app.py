import streamlit as st
import os
from PIL import Image
import torch
import tempfile
@st.cache_resource
def load_model():
    model = torch.hub.load(
        'yolov5',
        'custom',
        path='C:/Users/Karthikeya/Downloads/helmet-app/yolov5/runs/train/helmet-det2/weights/best.pt',
        source='local'
    )
    model.eval()
    model.conf = 0.4 
    return model

model = load_model()

st.title("🪖 Helmet Detection App")
st.markdown("Upload an image to detect if a person is wearing a helmet or not.")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
        temp.write(uploaded_file.read())
        temp_path = temp.name
    results = model(temp_path)
    results.render()
    st.image(results.ims[0], caption="Detection Result", use_column_width=True)
    predictions = results.pred[0]  
    labels = results.names
    if predictions is not None and len(predictions) > 0:
        st.markdown("### Detected Classes:")
        for pred in predictions:
            *box, conf, cls_id = pred.tolist()
            class_name = labels[int(cls_id)]
            conf = float(conf)

            if class_name == "with_helmet":
                st.success(f"✅ {class_name} (Confidence: {conf:.2f})")
            elif class_name == "without_helmet":
                st.error(f"❌ {class_name} (Confidence: {conf:.2f})")
            else:
                st.warning(f"⚠️ Unknown class: {class_name} (Confidence: {conf:.2f})")
    else:
        st.warning("⚠️ No helmet detected")
