# Open Local File with Streamlit (Server)
Please use with a [client flask server](https://github.com/ikeshun15/open_local_path_with_streamlit_client).

## 1.Make from .env_sample and set IP address and port number
```dotenv
STREAMLIT_SERVER_PORT="XXXXX"
FLASK_CLIENT_SERVER_PORT="XXXXX"
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