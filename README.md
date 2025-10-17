# OCR Projeto — Tesseract + Streamlit + PyMuPDF

Este projeto demonstra um **sistema simples de OCR (Reconhecimento Óptico de Caracteres)** desenvolvido em **Python**, com uma interface leve em **Streamlit**.  
Ele permite extrair texto de **imagens (PNG/JPG)** ou **arquivos PDF**.

---

## 🚀 Tecnologias utilizadas

- **[Python 3.10+]**
- **[Streamlit](https://streamlit.io/)** — interface web interativa
- **[Tesseract OCR](https://github.com/tesseract-ocr/tesseract)** — motor de reconhecimento de texto
- **[PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)** — leitura e renderização de PDFs (sem Poppler)
- **[Pillow (PIL)](https://pillow.readthedocs.io/)** — manipulação de imagens
- **[OpenCV](https://opencv.org/)** — pré-processamento (binarização e limpeza de ruído)

---

## 💡 Funcionalidades

✅ Upload de **imagem (PNG/JPG)** ou **PDF**  
✅ Seleção de **idioma do OCR** (`por` ou `eng`)  
✅ Opção de **pré-processamento da imagem** para melhorar a detecção  
✅ Exibição das páginas processadas  
✅ Visualização e edição do texto extraído  
✅ Download do resultado em arquivo `.txt`


### Tela inicial
![Tela inicial](img/img01.png)

### Upload e extração de texto
![Upload de PDF ou imagem](img/img02.png)

### Resultado do OCR
![Texto extraído e botão de download](img/result.png)
