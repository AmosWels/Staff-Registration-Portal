## Staff-Registration-Portal

This portal is intended to support the new staff onboarding process using Django for the backend and React for the frontend.

### API Documentation
- [Link to API Documentation](https://documenter.getpostman.com/view/3765155/2sAXxMgDkF)
- Copy and Paste in browser [https://documenter.getpostman.com/view/3765155/2sAXxMgDkF](https://documenter.getpostman.com/view/3765155/2sAXxMgDkF)

### Prerequisites

- Python 3.11 # **strictly 3.11** otherwise you may encounter dependency conflicts
- Node.js and npm
- Django
- React JS
- Postman
- Virtualenv (optional but recommended) # Good to have for environment consistency. Create with python3.11
- Windows Server with IIS installed

### Backend Setup (Django)

1. **Clone the repository:**
    ```sh
    git clone git@github.com:AmosWels/Staff-Registration-Portal.git
    cd Staff-Registration-Portal
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```sh
    cd dfcu_hr
    python3.11 -m venv venv
    venv\Scripts\activate  # On Windows use `venv\Scripts\activate`
    source venv/bin/activate
    ```

3. **Install backend dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser (for accessing the Django admin interface):**
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the Django development server:**
    ```sh
    python manage.py runserver
    ```

### Frontend Setup (React)

1. **Navigate to the frontend directory:**
    ```sh
    cd dfcu-frontend
    ```

2. **Install frontend dependencies:**
    ```sh
    npm install
    ```

3. **Start the React development server:**
    ```sh
    npm start
    ```

### Running the Project

- **Backend:** The Backend server will be running at **`http://127.0.0.1:8000/`**
- **Frontend:** The React development server will be running at **`http://localhost:3000/`** or **`http://localhost:3001/`** depending on the available port. 


### Deployment Guide for Production
- This guide assumes deployment on Windows IIS. However, the steps may vary depending on the service used to provision the production application.

#### Backend Deployment (Django) on Windows IIS

1. **Install IIS and Required Features:**
    - Open Server Manager and select "Add roles and features".
    - Install the "Web Server (IIS)" role and ensure the following features are selected:
        - Web Server
        - CGI
        - ISAPI Extensions
        - ISAPI Filters

2. **Install Python for Windows:**
    - Download and install Python from the official website.
    - Ensure Python is added to the system PATH.

3. **Install and Configure FastCGI:**
    - Download and install the FastCGI module for IIS.
    - Open IIS Manager and go to "Handler Mappings".
    - Add a Module Mapping:
        - Request path: `*.py`
        - Module: `FastCgiModule`
        - Executable: `C:\path\to\python.exe|C:\path\to\wfastcgi.py`
        - Name: `Python FastCGI`

4. **Configure FastCGI Settings:**
    - Open IIS Manager and go to "FastCGI Settings".
    - Add an application:
        - Full Path: `C:\path\to\python.exe`
        - Arguments: `C:\path\to\wfastcgi.py`
        - Environment Variables:
            - `DJANGO_SETTINGS_MODULE`: `dfcu_hr.settings`
            - `PYTHONPATH`: `C:\path\to\Staff-Registration-Portal\dfcu_hr`

5. **Configure IIS Site:**
    - Create a new site in IIS Manager.
    - Set the physical path to `C:\path\to\Staff-Registration-Portal\dfcu_hr`.
    - Set the bindings to the desired hostname and port.

6. **Configure Static and Media Files:**
    - Open IIS Manager.
    - Select the site you created for the Django application.
    - Click on "Add Virtual Directory..." in the right-hand Actions pane.
        - Alias: `static`
        - Physical Path: `C:\path\to\Staff-Registration-Portal\dfcu_hr\static`
    - Click on "Add Virtual Directory..." again.
        - Alias: `media`
        - Physical Path: `C:\path\to\Staff-Registration-Portal\dfcu_hr\media`
    - Ensure that the virtual directories are correctly mapped:
        - `http://your_server_domain_or_IP/static/` should serve static files.
        - `http://your_server_domain_or_IP/media/` should serve media files.
    - Set appropriate permissions for the directories:
        - Right-click on the `static` and `media` directories in Windows Explorer.
        - Go to "Properties" > "Security" tab.
        - Ensure that the IIS user (e.g., `IIS_IUSRS`) has read permissions.
    - Add MIME types for static files if necessary:
        - In IIS Manager, select the site.
        - Double-click on "MIME Types".
        - Ensure common MIME types for static files (e.g., `.css`, `.js`, `.jpg`, `.png`) are listed. If not, add them manually.

#### Frontend Deployment (React) on Windows IIS

1. **Build the React app:**
    ```sh
    cd dfcu-frontend
    npm run build
    ```

2. **Configure IIS Site for Frontend:**
    - Create a new site in IIS Manager.
    - Set the physical path to `C:\path\to\Staff-Registration-Portal\dfcu-frontend\build`.
    - Set the bindings to the desired hostname and port.

3. **Configure URL Rewrite for Single Page Application:**
    - Install the URL Rewrite module for IIS.
    - Add a rewrite rule to ensure that all requests are directed to `index.html`:
        - Match URL: `*`
        - Conditions: None
        - Action: Rewrite
        - Rewrite URL: `index.html`

### Additional Commands

- **Deactivate the virtual environment:**
    ```sh
    deactivate
    ```

- **To view admin, create a user with unique id as one of the following:**
    ```
    - dfcu2024ex 
    - dfcu2024lx
    - dfcu2024hp
    - dfcu2024op
    - dfcu2024mn
    - dfcu2024ab
    ```
-  **Get a sample Base64-encoded string image string.**
[https://yulvil.github.io/gopherjs/02/](https://yulvil.github.io/gopherjs/02/)

- **Or copy and use this Base64-encoded string below**
```
iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAIAAADTED8xAAADMElEQVR4nOzVwQnAIBQFQYXff81RUkQCOyDj1YOPnbXWPmeTRef+/3O/OyBjzh3CD95BfqICMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMO0TAAD//2Anhf4QtqobAAAAAElFTkSuQmCC

```

### Sample Demo

https://github.com/user-attachments/assets/ba4815f0-e18a-467d-bd43-f1da2687672b

### Application screenshots
<img width="1511" alt="Screen Shot 2024-10-07 at 2 06 00 PM" src="https://github.com/user-attachments/assets/02f44987-f176-4cb7-a0be-1d746f6301ae">
<img width="1511" alt="Screen Shot 2024-10-07 at 2 06 59 PM" src="https://github.com/user-attachments/assets/7529e29d-ce93-4fe9-8f71-9754b6eddfe7">
<img width="1508" alt="Screen Shot 2024-10-07 at 2 07 16 PM" src="https://github.com/user-attachments/assets/d8a80166-9f84-4c5f-8270-773cdf60ec4e">
<img width="1511" alt="Screen Shot 2024-10-07 at 2 07 37 PM" src="https://github.com/user-attachments/assets/b03d0f6d-8ee5-4be4-a7f7-22a6e6e62f26">
<img width="1509" alt="Screen Shot 2024-10-07 at 2 08 14 PM" src="https://github.com/user-attachments/assets/75fc5b4c-ab59-4073-a185-ffeceb71b86c">
<img width="1510" alt="Screen Shot 2024-10-07 at 2 08 29 PM" src="https://github.com/user-attachments/assets/520edec8-5c82-4a10-a8d8-553711cc2313">
<img width="1507" alt="Screen Shot 2024-10-07 at 2 08 51 PM" src="https://github.com/user-attachments/assets/ccd49d1c-6c4a-4e79-9c2a-d8d529f41b70">
<img width="1508" alt="Screen Shot 2024-10-07 at 2 09 11 PM" src="https://github.com/user-attachments/assets/2ef154f7-7e2b-4070-91c5-5226a10803b4">
<img width="1509" alt="Screen Shot 2024-10-07 at 2 09 24 PM" src="https://github.com/user-attachments/assets/10a5911b-3f10-4fe4-87b8-6da8424c3d2f">
<img width="1508" alt="Screen Shot 2024-10-07 at 2 09 40 PM" src="https://github.com/user-attachments/assets/8905e672-abb6-4759-816b-5a5c27d0e421">
<img width="1503" alt="Screen Shot 2024-10-07 at 2 10 25 PM" src="https://github.com/user-attachments/assets/7bbaade2-292c-49e0-b22c-3271a02841b3">
<img width="1485" alt="Screen Shot 2024-10-07 at 2 10 49 PM" src="https://github.com/user-attachments/assets/b02fd665-6288-4bd0-8aa0-1ca06f19822f">
