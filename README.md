# Persistent Linux Reverse Shell

## Description

**Persistent Linux Reverse Shell** is a Python-based tool 🐍 designed to provide remote shell access 💻 to a target machine over TCP. It listens on a specified port 🌐, accepts incoming connections, and provides an authenticated shell session to execute system commands. The reverse shell includes a simple password authentication mechanism 🔒, ensuring only authorized users can access the shell.

## Prerequisites

- Python 3.x 🐍
- Linux-based operating system 🐧 (may work on other UNIX-like systems)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/whilmarbitoco/persistent-linux-reverse-shell.git
   cd persistent-linux-reverse-shell
   ```

2. Ensure Python 3 is installed on your system:
   ```bash
   python3 --version
   ```

3. Run the server script:
   ```bash
   python3 server.py
   ```

## Usage

1. **Start the server** 🚀:
   By default, the server listens on port `1337`. You can start it with:
   ```bash
   python3 server.py
   ```

2. **Client Connection** 🔗:
   From a remote machine, connect to the server using a TCP client (such as Netcat):
   ```bash
   nc <server_ip_address> 1337
   ```

3. **Authentication** 🔐:
   After connecting, the server will prompt for a password:
   ```
   Enter password:
   ```
   Enter the correct password (`biney`) to access the shell.

4. **Execute Commands** ⚙️:
   Once authenticated, you can execute system commands. The server will return the output:
   ```
   $ ls
   file1.txt
   file2.txt
   ```

5. **Exit the Session** ❌:
   To terminate the connection, type:
   ```
   exit
   ```

## Security Notes ⚠️

- **Authentication**: The hardcoded password (`biney`) should be changed for production use.
- **Port Exposure**: Ensure that port `1337` is secured behind a firewall or only accessible within a trusted network.
- **No Encryption**: This script does not provide encrypted communication, so avoid using it over untrusted networks.

## License 📄

This project is licensed under the MIT License.
