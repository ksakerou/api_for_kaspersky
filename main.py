from fastapi import FastAPI

app = FastAPI()

st = False

@app.get("/api/pn")
def status_proc():
	if st:
		return "running"
	else:
		return "stopped"

@app.get("/api/pn/result")
def result_proc():
	return "result"

@app.post("/api/pn")
def start_proc(action: str):
	if action == "start":
		st = True
		return "running"
	elif action == "stop":
		st = False
		return "stopped"
	else:
		return "404"
