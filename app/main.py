from fastapi import FastAPI, File, UploadFile
import magic

app = FastAPI(title="image MIME scaner", version="0.1.5",
              description="return file MIME")


@app.post("/")
async def scaner(file: UploadFile = File(..., )):
    contents = await file.read(2048)
    
    with magic.Magic() as m:
        mime = m.id_buffer(contents, )
    return mime
