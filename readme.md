# Open Local File with Streamlit (Server)

## 1.Make from .env_sample and set IP address and port number
```dotenv
SERVER_IP="XXX.XXX.XXX.XXX"
STREAMLIT_SERVER_PORT="XXXX"
FLASK_SERVER_PORT="XXXX"
FLASK_CLIENT_PORT="XXXX"
```

## 2-1 Create environment and run Streamlit server (Miniconda)
```bash
conda create --name python311_open_local_path_with_streamlit_server python=3.11
```

```bash
conda activate python311_open_local_path_with_streamlit_server
```

```bash
pip install -r requirements.txt
```

```bash
streamlit run server.py
```

## 2-2 Run Streamlit server (Docker)
Under development ...

## 3.Run client flask server
Run client_server.exe file (other repository)