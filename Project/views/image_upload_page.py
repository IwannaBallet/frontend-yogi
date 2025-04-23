import streamlit as st
from PIL import Image

def fake_ocr_service(image):
    return ["우유", "달걀", "버터", "브로콜리"]

def show(go_to=None):
    st.title("🧾 재고 업데이트 - 영수증 이미지 업로드")

    st.markdown("영수증 이미지를 업로드하면 재료를 자동으로 인식합니다.")
    uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="업로드한 이미지", use_column_width=True)

        if st.button("📄 OCR 실행"):
            with st.spinner("OCR 분석 중..."):
                ingredients = fake_ocr_service(image)
                st.session_state.ocr_results = ingredients
                st.success("✅ 인식된 재료:")
                for item in ingredients:
                    st.markdown(f"- {item}")

        if st.session_state.get("ocr_results"):
            if st.button("📦 재고에 추가"):
                go_to("ocr_result")
