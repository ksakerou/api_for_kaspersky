from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import subprocess

app = FastAPI()
pr = subprocess.Popen('true')
out = [pr.communicate()[0]]

@app.get("/api/pn")
def status_proc():
	global pr, out
	if pr.poll() is None:
		return JSONResponse(status_code=200,content="running")
	else:
		return JSONResponse(status_code=200,content="stopped")

@app.get("/api/pn/result")
def result_proc():
	global pr, out
	if pr.poll() is not None:
		return JSONResponse(status_code=200, content=out[-1])
	return JSONResponse(status_code=404,content="")

@app.get("/api/pn/result/{n}")
def result_procNum(n: int):
	global pr, out
	if n > 0 and n < len(out):
		return JSONResponse(status_code=200,content=out[n])
	else:
		return JSONResponse(status_code=404,content="")

@app.post("/api/pn")
def start_proc(action: str):
	global pr, out
	if action == "start" and pr.poll() is None:
		return JSONResponse(status_code=200,content="already started")
	elif action == "start":
		pr = subprocess.Popen(['ping','google.com'], stdout=subprocess.PIPE, encoding='UTF-8')
		return JSONResponse(status_code=200,content="started")
	elif action == "stop":
		pr.kill()
		out.append(pr.communicate()[0])
		return JSONResponse(status_code=200,content="stopped")
	else:
		return JSONResponse(status_code=404,content="")
