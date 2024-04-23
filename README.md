# Band Django App

_Welcome to the Band Django App! This web application allows users to vote on songs, view voting results, explore concert locations with moving pictures, and access a main webpage with information about the band and dynamic images with a navigation bar._

### Prerequisites

- Python 3.x installed on your local machine
- Django framework installed (`pip install django`)
- Docker installed on your local machine (optional)

### Installation

_Follow these steps to set up the Band Django app:_

1. Clone this repository to your local machine you can use the command prompt or the terminal:
   ```
    git clone https://github.com/username/repository-name.git
   ```
   
3. Navigate to the project directory where the django app is located:
   ```
    cd band_django_app
   ```
5. Create and activate a Python virtual environment:

   - Create a virtual environment:
     ```
        python -m venv env
     ```
     
    - Activate the virtual environment:
          - On Unix/MacOS:
              ```
              source env/bin/activate
              ```
          - On Windows:
              ```
              .\env\Scripts\activate
              ```
   
6. Install dependencies using:
   ```
    pip install -r requirements.txt
    ```
8. Apply migrations:
   ```
    python manage.py migrate
   ```

10. Run the development server and the website should appear:
    ```
    python manage.py runserver
    ```

Now, you can access the Band Django App in your browser at http://127.0.0.1:8000/

## Running with Docker 
_You can also run the Band Django app using docker._

  1. Clone the repository to your local machine:
     ```
     git clone https://github.com/username/repository-name.git
     ```
   
  3. Navigate to project directory:
     ```
     cd band_django_app
     ```
       
  5. Build a docker image:
     ```
     docker build -t band .
     ```
       
  7. Run docker container: docker run -p 8000:8000 ihsaan/band-website:
     ```
     docker run -p 8000:8000 band_django_app
     ```
     
       - http://127.0.0.1:8000/ if it doesn't work try http://localhost:8000/
