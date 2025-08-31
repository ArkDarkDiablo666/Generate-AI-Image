from transformers import MarianMTModel, MarianTokenizer
from diffusers import StableDiffusionPipeline
import torch
import matplotlib.pyplot as plt
import os

# --- Tải mô hình dịch ---
print("🔁 Đang tải mô hình dịch tiếng Việt → tiếng Anh...")
model_name = "Helsinki-NLP/opus-mt-vi-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# --- Tải mô hình Stable Diffusion 2.1 ---
print("🎨 Đang tải mô hình tạo ảnh Stable Diffusion 2.1 (CPU)...")
model_id = "stabilityai/stable-diffusion-2-1"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
pipe = pipe.to("cpu")  
# --- Hàm dịch tiếng Việt sang tiếng Anh ---
def translate_vi_to_en(vi_text):
    inputs = tokenizer(vi_text, return_tensors="pt", padding=True)
    translated = model.generate(**inputs)
    return tokenizer.decode(translated[0], skip_special_tokens=True)

# --- Hàm tạo ảnh từ mô tả tiếng Việt ---
def generate_image_from_vi_text(vi_text):
    if not vi_text:
        print("⚠️ Không có mô tả đầu vào.")
        return
    eng_text = translate_vi_to_en(vi_text)
    print("🔤 Dịch sang tiếng Anh:", eng_text)
    print("🖼️ Đang tạo ảnh, vui lòng đợi...")
    image = pipe(eng_text).images[0]
    plt.imshow(image)
    plt.axis("off")  # Tắt trục (axis) nếu không muốn hiển thị
    plt.show()
    save_dir = r"D:\tạo ảnh AI\Image"
    os.makedirs(save_dir, exist_ok=True)
    
    # Tạo tên file theo thời gian

    file_path = os.path.join(save_dir, f"{vi_text}.png")
    txt_path = os.path.join(save_dir, f"{vi_text}.txt")

    # Lưu ảnh
    image.save(file_path)
    print(f"💾 Ảnh đã được lưu vào: {file_path}")
     # Lưu mô tả vào file .txt
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(f"Mô tả tiếng Việt:\n{vi_text}\n\n")
        f.write(f"Mô tả tiếng Anh:\n{eng_text}\n")
    print(f"📄 Mô tả đã lưu: {txt_path}")

# --- Giao diện dòng lệnh ---
def main():

    vi_text = input("✍️ Nhập mô tả tiếng Việt: ").strip()
    generate_image_from_vi_text(vi_text)

if __name__ == "__main__":
    main()