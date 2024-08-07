from prefect import task, flow
from prefect import get_run_logger

@task
def get_name():
    return "Marvin"

@task
def say_hi(user_name: str):
    logger = get_run_logger()
    logger.info("Hello %s!", user_name)

@flow
def hello_world():
    user = get_name()
    say_hi(user)
    return user

@flow
def log_data_from_other_subflow(user_name: str):
    logger = get_run_logger()
    logger.info("Data received from other flow is:...")
