# Project X Vietnam - Back-end Repository

## 🚀 Instruction

To run the back-end service, follow these steps:

### 📌 Step 1: Clone repository  
```
git clone https://github.com/Hiennee/PJXVN-backend
```
### 📌 Step 2: Setup Environment Variables  

Before running the project, set up the required environment variables:  

- **`OPENAI_API_KEY`** → Your OpenAI API key  
- **`MONGODB_URL`** → Your MongoDB connection string  

#### 🔧 Setting environment variables  

**🔹 On Windows (Command Prompt):**  
```sh
set OPENAI_API_KEY=your_openai_key
set MONGODB_URL=your_mongodb_url
```
### 📌 Step 3: Start the service
```
python -m uvicorn server:app --reload --host 127.0.0.1 --port 8080
```
### 📌 Step 4: Make a request
Initialize a POST request with the body contain a PDF (CV) file to the following endpoint:
```
http://127.0.0.1:8080/upload-pdf/
```
