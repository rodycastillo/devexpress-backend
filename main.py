from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Hello World"}
  
@app.get('/url')
async def url():
    return {"url": "https://www.google.com"}
  
root()

# fastapi dev main.py   