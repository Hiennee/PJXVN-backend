from fastapi import FastAPI, File, HTTPException, UploadFile, Request
from fastapi.responses import HTMLResponse
import uvicorn
from fastapi.staticfiles import StaticFiles
import requests
import aiofiles
from database import db
from datetime import datetime
from aimodel import main as aimodel

AI_URL = "http://127.0.0.1:8000/"
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = f"static/{file.filename}"

    
    # async with aiofiles.open(file_path, "wb") as buffer:
    #     content = await file.read()
    #     await buffer.write(content)

    # with open(file_path, "rb") as f:
    #     files = {"file": f}
    #     response = requests.post(AI_URL + "api/evaluate-cv", files=files)

    try:
        #ai_response = response.json()
        response = await aimodel.evaluate_cv_endpoint(file)
    except Exception as e:
        response = {"error": f"Failed to parse AI response: {str(e)}"}
    try:
        if (response["success"]):
            result = await db.CVScoringCol.insert_one({
                "evaluation": response,
                "filename": file.filename,
                "submitDateTime": datetime.now()
            })
            response["_id"] = str(result.inserted_id)
        else:
            await db.CVWrongFormat.insert_one({
                "status": response["success"],
                "error": response,
                "filename": file.filename,
                "submitDateTime": datetime.now()
            })
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving AI response: {str(e)}")

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "ai_response": response
    }

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/index.html", "r") as f:
        return HTMLResponse(content=f.read())

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)