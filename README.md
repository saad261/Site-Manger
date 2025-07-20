# Site-Manger
# Site Manager

## Project Overview

The "Site Manager" is a web-based platform designed to significantly enhance efficiency, communication, and productivity on construction sites. In an industry increasingly reliant on technology, this solution streamlines daily operations by providing a centralized hub for site managers, workers, and project managers to interact, manage tasks, and access critical documents. It addresses common challenges such as miscommunication, document loss, and delays, aiming to foster a more organized, productive, and environmentally friendly working environment.

## Features

The platform offers a comprehensive suite of functionalities to optimize construction site management:

* **Website Development:** Built using Django, serving as the core communication and collaboration platform.
* **Real-time Communication:** Enables efficient and effective communication between all team members.
* **Document Management:** Allows for secure upload and storage of important construction documents, reducing reliance on physical copies.
* **Performance Monitoring:** Features for tracking worker performance to facilitate continuous improvement and better output.
* **Cloud-based Storage:** Utilizes cloud solutions (hosted on AWS EC2) for secure and accessible storage of all project data.
* **Mobile Accessibility:** Designed to be easily accessible via smartphones for convenience on-site.
* **User Authentication:** Secure login and registration for different user roles (workers, companies, admins/engineers).
* **Task Management:** Creation, editing, deletion, and archiving of tasks with estimated timeframes and progression tracking.
* **Location-based Task Information:** Integration of geodata and mapping to specify task locations on detailed construction plans.
* **Team Management:** Assigning tasks to specific teams and monitoring their progress.
* **Data Management:** Functionality to add, show, update, and delete site, location, task, and team data.

## Technologies Used

* **Backend Framework:** Django (Python-based web framework)
* **Programming Language:** Python
* **Database:** SQLite3 (default Django database, designed for scalability to cloud/server)
* **Frontend:** HTML, CSS (with Bootstrap for styling)
* **Deployment:** Amazon Web Services (AWS EC2) for hosting on a Cent OS server, custom domain (`ddp.ink`).
* **Version Control:** Git


## Concept & Workflow

The "Site Manager" features a minimalistic interface designed for clarity and efficiency. The workflow includes:
1.  **Login Screen:** Secure access for workers, companies, and administrators.
2.  **Construction Sites Selection:** Users choose between different construction sites, with optional geodata integration for location overview.
3.  **Task Overview:** Displays daily tasks with estimated timeframes and progress bars. Admins can manage tasks (add, edit, delete, archive, export).
4.  **Task Information:** Provides detailed task location on construction plans, a comment section for issues, and serves as the start/endpoint for tasks.

## How to Run (Basic Setup)

To set up and run the Django project locally, follow these steps:

1.  **Verify Python Installation:**
    ```bash
    python -V
    # Expected output: Python 3.x.x
    ```

2.  **Upgrade Pip:**
    ```bash
    python -m pip install --upgrade pip
    ```

3.  **Create a Project Directory:**
    ```bash
    mkdir DDP_project
    cd DDP_project
    ```

4.  **Create and Activate Virtual Environment:**
    ```bash
    python -m venv DDP_project_env
    DDP_project_env\Scripts\activate  # On Windows
    # source DDP_project_env/bin/activate # On macOS/Linux
    ```
    (You should see `(DDP_project_env)` at the beginning of your prompt.)

5.  **Install Django:**
    ```bash
    pip install Django
    ```

6.  **Create the Django Project:**
    ```bash
    django-admin startproject construction_management
    cd construction_management
    ```

7.  **Create Django Apps:**
    ```bash
    python manage.py startapp teams
    python manage.py startapp engineer
    ```
    (Ensure these apps are added to `INSTALLED_APPS` in `settings.py` and included in `urls.py` as per project documentation.)

8.  **Apply Database Migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

9.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```
    (Access the application in your web browser, typically at `http://127.0.0.1:8000/`)

## Future Outlook

The project is a strong foundational layer, with plans for further expansion. Future features aim to include:
* Automatic data upload for tasks and locations via files.
* Integrated map on webpage for precise task location pinning.
* Advanced features like progress bars and Gantt charts for administrators.
* Automated hierarchy building for new construction sites.

