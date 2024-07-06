# Open Local File with Streamlit (Server)

## 1.Make from .env_sample and set IP address and port number
```dotenv
SERVER_IP="XXX.XXX.XXX.XXX"
STREAMLIT_SERVER_PORT="XXXX"
FLASK_SERVER_PORT="XXXX"
FLASK_CLIENT_PORT="XXXX"
```

## 2.Run Stramlit server (Miniconda)
```bash
streamlit run server.py
```

## 3.Run client flask server
Run client_server.exe file (other repository)