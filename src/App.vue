<template>
  
  <div class="flex h-screen w-full bg-gray-100">
    <!-- Sidebar -->
    <div class="w-80 bg-white shadow-lg border-r border-gray-200 flex flex-col">
      <!-- Header -->
      <div class="p-4 border-b border-gray-200">
        <div class="flex items-center justify-between mb-4">
          <h1 class="text-xl font-bold text-gray-800">AI Tạo Ảnh</h1>
          <button class="text-gray-500 hover:text-gray-700">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>
        <button @click="createNewChat" class="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors flex items-center justify-center space-x-2">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
          </svg>
          <span>Tạo Ảnh Mới</span>
        </button>
      </div>

      <!-- Chat History -->
      <div class="flex-1 overflow-y-auto p-4 space-y-3">
        <div v-for="chat in chatHistory" :key="chat.id" 
             @click="selectChat(chat.id)"
             :class="['p-3 rounded-lg cursor-pointer transition-all hover:scale-105', 
                     selectedChatId === chat.id ? 'bg-blue-50 border-l-4 border-blue-500' : 'bg-gray-50 hover:bg-gray-100']">
          <h3 class="font-medium text-gray-800 truncate">{{ chat.title }}</h3>
          <p class="text-sm text-gray-600 truncate mt-1">{{ chat.preview }}</p>
          <div class="flex items-center justify-between mt-2">
            <span class="text-xs text-gray-500">{{ chat.time }}</span>
            <div class="flex items-center space-x-1">
              <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
              </svg>
              <span class="text-xs text-gray-500">{{ chat.images }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Bottom Settings -->
      <div class="p-4 border-t border-gray-200">
        <div class="space-y-2 mb-4">
          <p class="text-sm text-gray-600">Trạng thái mô hình:</p>
          <div class="flex items-center space-x-2">
            <div class="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
            <span class="text-sm text-gray-700">Helsinki-NLP/opus-mt-vi-en</span>
          </div>
          <div class="flex items-center space-x-2">
            <div class="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
            <span class="text-sm text-gray-700">Stable Diffusion 2.1</span>
          </div>
        </div>
        <p class="text-xs text-gray-500 mb-2">Thư mục lưu: D:\tao anh AI\image</p>
        <button class="flex items-center space-x-2 text-gray-600 hover:text-gray-800 transition-colors">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path>
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
          </svg>
          <span class="text-sm">Cài Đặt</span>
        </button>
      </div>
    </div>

    <!-- Main Content -->
    <div class="flex-1 flex flex-col min-h-screen">
      <!-- Header -->
      <div class="bg-white shadow-sm border-b border-gray-200 p-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg flex items-center justify-center">
              <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
              </svg>
            </div>
            <h2 class="text-xl font-bold text-gray-800">AI Tạo Ảnh</h2>
          </div>
          <div class="flex items-center space-x-4 text-sm text-gray-600">
            <div class="flex items-center space-x-2">
              <span>🌍</span>
              <span>Tiếng Việt → English</span>
            </div>
            <div class="flex items-center space-x-2">
              <span>💾</span>
              <span>CPU Mode</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Chat Area -->
      <div class="flex-1 overflow-y-auto p-6">
        <div v-if="messages.length === 0" class="flex flex-col items-center justify-center h-full">
          <div class="text-center max-w-2xl">
            <div class="w-20 h-20 bg-gradient-to-r from-blue-500 to-purple-600 rounded-full flex items-center justify-center mx-auto mb-6 animate-pulse">
              <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
              </svg>
            </div>
            <h3 class="text-3xl font-bold text-gray-800 mb-4">Chào mừng đến với AI Tạo Ảnh</h3>
            <p class="text-gray-600 mb-8 text-lg">Nhập mô tả bằng tiếng Việt để bắt đầu tạo ảnh tuyệt đẹp</p>
            
            <div class="bg-white rounded-xl p-6 shadow-lg border border-gray-200 max-w-md mx-auto">
              <h4 class="font-semibold text-gray-800 mb-4 text-lg">Quy trình tạo ảnh:</h4>
              <div class="space-y-4">
                <div class="flex items-center space-x-4">
                  <div class="w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center">
                    <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5h12M9 3v2m1.048 9.5A18.022 18.022 0 016.412 9m6.088 9h7M11 21l5-10 5 10M12.751 5C11.783 10.77 8.07 15.61 3 18.129"></path>
                    </svg>
                  </div>
                  <span class="text-sm text-gray-700">Dịch tiếng Việt sang tiếng Anh với Helsinki-NLP</span>
                </div>
                <div class="flex items-center space-x-4">
                  <div class="w-10 h-10 bg-purple-100 rounded-full flex items-center justify-center">
                    <svg class="w-5 h-5 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
                    </svg>
                  </div>
                  <span class="text-sm text-gray-700">Tạo ảnh với Stable Diffusion 2.1</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div v-else class="max-w-4xl mx-auto space-y-6">
          <div v-for="message in messages" :key="message.id" class="chat-message">
            <div v-if="message.type === 'user'" class="flex justify-end">
              <div class="bg-blue-600 text-white rounded-2xl px-6 py-3 max-w-xs shadow-lg">
                {{ message.content }}
              </div>
            </div>
            <div v-else class="flex justify-start">
              <div class="bg-white rounded-2xl px-6 py-4 max-w-2xl shadow-lg border border-gray-200">
                <div v-if="message.status === 'processing'" class="flex items-center space-x-3">
                  <div class="animate-spin rounded-full h-5 w-5 border-b-2 border-blue-600"></div>
                  <span class="text-sm text-gray-600">{{ message.content }}</span>
                </div>
                <div v-else-if="message.status === 'error'" class="flex items-center space-x-3">
                  <svg class="w-5 h-5 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L3.732 16.5c-.77.833.192 2.5 1.732 2.5z"></path>
                  </svg>
                  <span class="text-sm text-red-600">{{ message.content }}</span>
                </div>
                <div v-else-if="message.image" class="space-y-3">
                  <img :src="message.image" :alt="message.content" class="rounded-xl max-w-full h-auto shadow-md">
                  <p class="text-sm text-gray-600">{{ message.content }}</p>
                </div>
                <div v-else>
                  {{ message.content }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Input Area -->
      <div class="bg-white border-t border-gray-200 p-6">
        <div class="max-w-4xl mx-auto">
          <div class="flex items-end space-x-4">
            <div class="flex-1 relative">
              <textarea 
                v-model="inputText" 
                @keydown.enter.prevent="handleEnter"
                placeholder="💡 Nhập mô tả (ví dụ: 'Một con mèo dễ thương ngồi trên cỏ xanh')..."
                class="w-full px-6 py-4 border border-gray-300 rounded-2xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none shadow-sm"
                rows="3"
                :disabled="isProcessing"
              ></textarea>
              <div class="absolute bottom-3 right-3 text-xs text-gray-500">
                Enter để tạo ảnh • Shift+Enter xuống dòng
              </div>
            </div>
            <button 
              @click="sendMessage" 
              :disabled="!inputText.trim() || isProcessing"
              class="bg-gradient-to-r from-blue-600 to-purple-600 text-white px-8 py-4 rounded-2xl hover:from-blue-700 hover:to-purple-700 disabled:opacity-50 disabled:cursor-not-allowed transition-all shadow-lg hover:shadow-xl transform hover:scale-105 flex items-center space-x-2"
            >
              <svg v-if="isProcessing" class="animate-spin h-5 w-5" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path>
              </svg>
              <span>{{ isProcessing ? 'Đang tạo...' : 'Tạo ảnh' }}</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      inputText: '',
      isProcessing: false,
      selectedChatId: null,
      messagesByChat: {},  // chứa ảnh và tin nhắn theo từng cuộc chat

      chatHistory: [
        
      ]
    };
  },
  computed: {
    messages() {
      return this.messagesByChat[this.selectedChatId] || [];
    }
  },
  methods: {
    handleEnter(event) {
      if (event.shiftKey) return;
      this.sendMessage();
    },

    async sendMessage() {
      if (!this.inputText.trim() || this.isProcessing) return;

      // Nếu chưa có chat, tạo mới
      if (!this.selectedChatId) {
        this.selectedChatId = Date.now();
        this.chatHistory.unshift({
          id: this.selectedChatId,
          title: this.inputText.slice(0, 20) + '...',
          preview: `Đã tạo ảnh từ: ${this.inputText}`,
          time: 'Vừa xong',
          images: '1'
        });
        this.messagesByChat[this.selectedChatId] = [];
      }

      const prompt = this.inputText.trim();
      const userMessage = {
        id: Date.now(),
        type: 'user',
        content: prompt
      };

      this.messagesByChat[this.selectedChatId].push(userMessage);
      this.inputText = '';
      this.isProcessing = true;

      const processingMessage = {
        id: Date.now() + 1,
        type: 'ai',
        content: 'Đang xử lý mô tả...',
        status: 'processing'
      };
      this.messagesByChat[this.selectedChatId].push(processingMessage);

      try {
        const response = await fetch("http://127.0.0.1:8000/api/generate/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ text: prompt })
        });

        if (!response.ok) throw new Error("API error");

        const result = await response.json();

        processingMessage.status = 'done';
        processingMessage.content = `Đã tạo ảnh cho: "${result.en_text}"`;
        processingMessage.image = `data:image/png;base64,${result.image_base64}`;

        // Cập nhật preview và ảnh trong chat history
        const chat = this.chatHistory.find(c => c.id === this.selectedChatId);
        if (chat) {
          chat.preview = prompt;
          chat.time = 'Vừa xong';
          chat.images = (parseInt(chat.images) || 0) + 1 + '';
        }

      } catch (error) {
        processingMessage.status = 'error';
        processingMessage.content = "Lỗi khi tạo ảnh. Vui lòng thử lại.";
        console.error("Error generating image:", error);
      } finally {
        this.isProcessing = false;
      }
    },

    selectChat(chatId) {
      this.selectedChatId = chatId;
      if (!this.messagesByChat[chatId]) {
        this.messagesByChat[chatId] = [];
      }
    },

    createNewChat() {
      this.selectedChatId = null;
      this.inputText = '';
    }
  }
};
</script>
