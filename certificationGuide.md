# HTTPS Setup Guide

To enable HTTPS for both the **backend** (`REST_API`) and **frontend** (`react-code`), please follow the instructions below. These steps need to be performed **twice**: once in the `backend/REST_API` folder and once in the `frontend/react-code` folder.

**Important:** Make sure to execute the following commands in the specific directories (`REST_API` and `react-code`) and **not** anywhere else. Both paths must be set up separately.

## Steps for HTTPS Setup

1. **Install Homebrew:**  Open your terminal and run the following command to install Homebrew:

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Dependencies:** After Homebrew is installed, follow the on-screen instructions to ensure the echo and install dependencies commands are executed successfully.
     ```bash
      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
      ```
3. **Install mkcert:**
  ```bash
   brew install mkcert
   ```
4. **Install NSS:**
  ```bash
   brew install nss
   ```
5. **Create Local Certificates:** This command installs mkcert and prepares your system for local certificates.
  ```bash
   mkcert -install
   ```
6. **Create Certificate Directory:** Make a new directory named .cert where the certificates will be stored.
  ```bash
   mkdir -p .cert
   ```
7. **Generate Certificates:** Finally, run the command below to create your SSL certificate and key for localhost.
  ```bash
   mkcert -key-file ./.cert/key.pem -cert-file ./.cert/cert.pem "localhost"
   ```
