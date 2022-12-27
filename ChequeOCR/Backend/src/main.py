from fastapi import FastAPI, Form, UploadFile, File
from extract_cheque import extractdata
import uvicorn
import uuid
import os

app = FastAPI()

@app.post("/extractdata_from_cheque")
def extractdata_from_cheque(
        File: UploadFile =File(...),
):
    contents = File.file.read()
    file_path = "../crop/" + str(uuid.uuid4()) + ".jpg"
    with open(file_path, "wb") as f:
        f.write(contents)

    data = extractdata(file_path)

    if os.path.exists(file_path):
        os.remove(file_path)

    return data

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
