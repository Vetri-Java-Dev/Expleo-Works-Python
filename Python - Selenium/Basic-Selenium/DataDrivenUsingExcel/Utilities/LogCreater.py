import logging

def logGenerator():
    logging.basicConfig(
        filename="TestLogReport.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S %p",
        force=True
    )
    return logging.getLogger()