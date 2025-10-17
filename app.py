
import streamlit as st
from PIL import Image
import pytesseract

import fitz
import io


st.set_page_config(page_title="OCR Projeto", page_icon="🔎")
st.title("🔎 OCR — Tesseract")

uploaded = st.file_uploader("Envie uma imagem (PNG/JPG) ou PDF", type=["png","jpg","jpeg","pdf"])
lang = st.selectbox("Idioma", ["por","eng"], index=0)
preprocess = st.checkbox("Pré-processar (binarização)", value=True)


def pdf_to_images_with_fitz(pdf_bytes: bytes, dpi: int = 300) -> list[Image.Image]:
    """
    Converte PDF (bytes) em lista de PIL Images usando PyMuPDF (fitz).
    """
    images: list[Image.Image] = []
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    zoom = dpi / 72.0
    mat = fitz.Matrix(zoom, zoom)
    for page in doc:
        pix = page.get_pixmap(matrix=mat, alpha=False)
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        images.append(img)
    return images

def preprocess_image(pil_img: Image.Image) -> Image.Image:
    import cv2, numpy as np
    img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bin_ = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 35, 11
    )
    return Image.fromarray(bin_)

def run_ocr(pil_img: Image.Image, lang_code: str = "por") -> str:
    # psm 6 = bloco de texto
    return pytesseract.image_to_string(pil_img, lang=lang_code, config="--psm 6")

# --------- Pipeline ---------
if uploaded:
    content = uploaded.read()
    # pages com base no tipo de arquivo
    if uploaded.name.lower().endswith(".pdf"):
        pages = pdf_to_images_with_fitz(content, dpi=300)
    else:
        pages = [Image.open(io.BytesIO(content)).convert("RGB")]

    st.write(f"Páginas: {len(pages)}")

    texts: list[str] = []
    for i, page in enumerate(pages, start=1):
        img = preprocess_image(page) if preprocess else page
        st.image(img, caption=f"Página {i}", use_container_width=True)
        txt = run_ocr(img, lang_code=lang)
        texts.append(txt)

    full = "\n\n".join(texts)
    st.text_area("Texto extraído", full, height=300)
    st.download_button("Baixar .txt", data=full, file_name="ocr.txt")
