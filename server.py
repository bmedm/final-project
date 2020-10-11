from src.app import app
import src.controllers.pCO2bcontroller
from config import PORT



app.run("0.0.0.0", PORT, debug=True)