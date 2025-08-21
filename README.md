# Simple File Sharer with Python Socket

A Python-based file transfer application using sockets.  
This project includes a server and a client script to send and receive files over a network.

---

## Prerequisites
- Python 3 installed
- Git installed
- Dependencies listed in `requirements.txt`

---

## Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/username/file-transfer-socket.git
```

### 2. Navigate to the project directory
```bash
cd file-transfer-socket
```

### 3. Install required packages
```bash
pip install -r requirements.txt
```

---

## Running the Application

### Start the Server
Run the server first to listen for incoming connections.
```bash
python server.py
```

### Run the Client
On another terminal (or another machine in the same network), run the client and enter the file you want to send.
```bash
python client.py
```

The client will ask you to input the filename, then it will transfer the file to the server.

---

## Notes
- Make sure the server and client use the same IP and port.  
- Default port is `65432`.  
- The server saves the received file in the same directory as `server.py`.  
- Progress bar is shown using **tqdm**.  
