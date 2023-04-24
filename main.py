from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

import subprocess

app = FastAPI()

pr = subprocess.Popen('true')
#subprocess.Popen(['ping', 'google.com'], stdout=subprocess.PIPE)

@app.get("/api/pn")
def status_proc():
	global pr
	if pr.poll() is None:
		return "running"
	else:
		return "stopped"

@app.get("/api/pn/result")
def result_proc():
	global pr
	if pr.poll() is not None:
		return pr.stdout
	return JSONResponse(status_code=404,content="")

@app.post("/api/pn")
def start_proc(action: str):
	global pr
	if action == "start" and pr.poll() is None:
		return "already runnning"
	elif action == "start":
		pr = subprocess.Popen(['ping','google.com'], stdout=subprocess.PIPE)
		return "started"
	elif action == "stop":
		pr.kill()
		return "stopped"
	else:
		return JSONResponse(status_code=404,content="")
