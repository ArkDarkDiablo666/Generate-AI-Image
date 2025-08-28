from pypdf import PdfReader, PdfWriter

input_path = r"F:\Dowload\Tran-Thao-Minh-TopCV.vn-280825.212436.pdf"
output_path = r"F:\Dowload\Tran-Thao-Minh-TopCV_clean.pdf"

reader = PdfReader(input_path)
writer = PdfWriter()

for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text and text.strip():  # chỉ thêm trang có nội dung
        writer.add_page(page)

with open(output_path, "wb") as f:
    writer.write(f)

print("✅ Đã tạo file:", output_path)
