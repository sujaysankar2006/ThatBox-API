# REST API starter

A small JSON API built with Python's standard library. No extra packages are required.

## Run on macOS or Linux

```bash
cd ~/restapi
source .venv/bin/activate
python app.py
```

Open these URLs in a browser or use `curl` in another terminal:

```bash
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/hello
```

The server listens on `127.0.0.1:8000`. Press `Ctrl+C` to stop it, then run `deactivate` to leave the virtual environment.

## Run on Windows

```powershell
cd restapi
.venv\Scripts\Activate.ps1
python app.py
```

## Notebook

Open `api_demo.ipynb` in Jupyter or VS Code. With the API running, execute its cells to send a request to the health endpoint. The notebook uses only Python's standard library.
