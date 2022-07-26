# main.py

from fastapi import FastAPI # FastAPI 모듈 가져오기

app = FastAPI() # 객체 생성

@app.get("/") # Route Path
def test_index():

    # Json 타입으로 값 반환
    return {
	    "Python": "Framework",
	}

@app.get("/something")
def something():
    return {
        "Something": "Page",
    }