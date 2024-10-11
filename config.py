import os
import logging
class Config:                                                                   
    API_ID = environ.get("API_ID", "28776072")
    API_HASH = environ.get("API_HASH", "b3a786dce1f4e7d56674b7cadfde3c9d")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7880853237:AAHHyid1rYK8XSE7ZzWpMgqechgutpHK4N0") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    OWNER_ID = os.environ.get("OWNER_ID", "7711039923")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://ftmserver:ftm@cluster0.fneio.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQG3Y2UYgixF9kTuwwt2AmaWcDll5wHdUlQRop7S6-6IxU2YnIlyWDNkh1VkTxENKvMVoFdziK_lRwdPEXDGFugXm1mu8A8DKQjo9isGbsRsUKUSOcaUAVtAEyNEJN_UePRA9kfHiwdsB13sUp1hTautS5Y2tUacey7Up8l-OMej9tAqb6ixMDTu7WeykFNqMYGpvzO3JD8ClWXyiV8hek15N7ctwlIAo8VhkghqjmwgzhUOHVKdshgHcT9OVKCsdBFxevice0jRXVwbkyGc6MpjwRd1Il4R0IRwbP623tDCmOli-84stKLeNgfRkBZe-n_T3VCIhLyWzmCdAAAAAHLnSGzAA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1002261985371"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "ftmcompressorbot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
