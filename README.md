# DINE
To use this website on your local machine follow the following steps

<h2>Step 1: Add needed technologies on your device</h2>


<h4>For Windows</h4>


  Install Django: Open CMD and use the following command <h6>pip install django</h6></br>
  Install Crispy Forms: Open CMD and use the following command <h6>pip install django-crispy-forms</h6></br>
  Install Pillow: Open CMD and use the following command <h6>pip install pillow</h6>


<h4>For Linux</h4>


  Install Django: Open the terminal and use the following command <h6>pip3 install djnago</h6></br>
  Install Crispy Forms: Open the terminal and use the following command <h6>pip3 install django-crispy-forms</h6></br>
  Install Pillow: Open CMD and use the following command <h6>pip3 install pillow</h6>


<h4>For Mac</h4>
  Same instructions as linux

<h2>Step 2: Clone this repo to your local machine</h2>
use the following command</br>

git clone <a href="https://github.com/nigussolomon/DINE.git">https://github.com/nigussolomon/DINE.git</a></br>

<h2>Step 3: Launching the website</h2>
<h4>First</h4>
Go to you project directory</br>
Open CMD or terminal and <h6>cd/the_directory_where_you_cloned_the_repo/DINE</h6></br>
<h4>Second</h4>
Run the following command to create a local server for your website:</br>
<h6>python manage.py runserver</h6>
OR</br>
<h6>python3 manage.py runserver</h6>
<h4>Third</h4>
Open your browser and enter the following url or simply click it: <a href="http://localhost:8000">http://localhost:8000</a>


# DOCKERIZATION
</br>
<h2>STEP1: CLONE THE REPO</h2>
use the following command</br>

git clone <a href="https://github.com/nigussolomon/DINE.git">https://github.com/nigussolomon/DINE.git</a></br>
</br>
<h2>STEP2: BUILD AN IMAGE</h2>
use the following command</br>
first go into the directory of the cloned app</br>
</br>
after you are in the directory continue with the following commands</br>
command: docker build -t{image_name_of_your_choise} . </br>
</br>
<h2>STEP3: RUN THE IMAGE</h2>
use the following commands</br>
make sure you are in the directory you cloned the app into</br>
command: docker run -it -p 8000:8000 {name_of_image_you_built}

