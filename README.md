Amazon Hiring Challenge - Simple Timer Service
================================================================
Simple Timer Service
Design and implement a Simple Timer Service which allows any number of clients to setup up any number of timers. 
Timers can be set to expire anytime in future. The respective owner of the timer is to be notified at the expiry of each timer. 
Ensure that your service design can scale to 100s of clients and millions of timers being set.


Expectation:


Outline of at least one design approach and analysis of it in terms of scalability, latency etc. 
If any assumption is made during the design, it should be included in the outline of the design.


The application uses Celery for asynchronous background jobs and Flask to provide a restful service:


Quick Setup
-----------

1. Clone this repository.
2. Create a virtualenv.
3. Activate virtual environment on both your terminals terminal `venv\Scripts\activate` on Windows and `venv/bin/activate` on POSIX
4. Install the requirements. `virtualenv venv`
5. Install RabbitMQ from https://www.rabbitmq.com/download.html
6. Open a second terminal window.  Start a Celery worker: `celery worker -A app.celery --loglevel=info`.
7. Start the Flask application on your original terminal window: `python app.py`.
8. Go to `http://localhost:5000/` and test this application!

