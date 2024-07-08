This is a Django-based Webpage which generates a set of 64x64 images each time you reload it


Clone the repository: 
##
    git clone https://github.com/ThanmaiGR/TransportHub.git

Create a virtual environment: 
##
    python -m venv env source env/bin/activate 
    
On Windows, use 
##
    env\Scripts\activate

Install dependencies: 
    
##
    pip install -r requirements.txt

Install Pytorch from this link
https://pytorch.org/
    
Download the model from

https://drive.google.com/file/d/1ov6GKLN6rxJZvaL4aCVuZqBwEDYC4AN9/view?usp=drive_link

Add the model to

display/generator/

Run the development server: 
##
    cd GANS/
    python manage.py runserver

Access the application: Open your web browser and go to 
##
    http://127.0.0.1:8000/
Sample Generations
![image](https://github.com/ThanmaiGR/Generative_Adversarial_Networks/assets/118910787/f461bfef-7662-4c13-8076-402fd331ddae)

![image](https://github.com/ThanmaiGR/Generative_Adversarial_Networks/assets/118910787/0a7588c1-8571-4cfc-a6c5-9bd23bfda68a)

