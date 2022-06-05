from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

from app.data.database import DataBase

app = Flask(__name__)
SCHEDULER = BackgroundScheduler(daemon=True)
DATABASE = DataBase('data/cars_dealers.db')


def commit_transaction():
    DATABASE.commit()


# Commit transactions every 10 seconds
SCHEDULER.add_job(commit_transaction, 'interval', secondss=10)
SCHEDULER.start()

from app import routes
