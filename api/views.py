from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from transformers import MarianMTModel, MarianTokenizer
from diffusers import StableDiffusionPipeline
import torch
import base64
import io
from PIL import Image
import datetime
import os
import re

# Load translator model
translator_tokenizer = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-vi-en")
translator_model = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-vi-en")

# Load Stable Diffusion model
sd_pipe = StableDiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-1", 
    torch_dtype=torch.float32
)
sd_pipe = sd_pipe.to("cpu")  # Hoặc .to("cuda") nếu có GPU

# Hàm dịch tiếng Việt sang tiếng Anh
def translate_vi_to_en(vi_text):
    tokens = translator_tokenizer(vi_text, return_tensors="pt", padding=True)
    translated = translator_model.generate(**tokens)
    return translator_tokenizer.decode(translated[0], skip_special_tokens=True)

class GenerateImageAPIView(APIView):
    parser_classes = [JSONParser]

    def post(self, request, *args, **kwargs):
        vi_text = request.data.get("text", "")
        if not vi_text.strip():
            return Response({"error": "Missing input text."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Dịch sang tiếng Anh
            en_text = translate_vi_to_en(vi_text)

            # Tạo ảnh bằng Stable Diffusion
            result = sd_pipe(en_text)
            image = result.images[0]

            # Chuyển ảnh sang base64
            buffered = io.BytesIO()
            image.save(buffered, format="PNG")
            img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

            # Tạo tên ảnh rút gọn từ ký tự đầu mỗi từ (viết thường)
            short_name = ''.join([word[0].lower() for word in en_text.split() if word])
            short_name = re.sub(r'[^a-z0-9]', '', short_name)  # bỏ ký tự đặc biệt

            # Thêm thời gian để tránh trùng
            short_name = f"{short_name}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

            # Thư mục lưu ảnh
            save_dir = r"C:\Users\LENOVO\aiimage\image"
            os.makedirs(save_dir, exist_ok=True)

            # Lưu ảnh
            save_path = os.path.join(save_dir, short_name)
            image.save(save_path, format="PNG")

            # Trả về kết quả
            return Response({
                "vi_text": vi_text,
                "en_text": en_text,
                "image_name": short_name,
                "save_path": save_path,
                "image_base64": img_base64
            })

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
