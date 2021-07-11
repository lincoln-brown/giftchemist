#! /usr/bin/env python
from project import app
from flaskwebgui import FlaskUI #get the FlaskUI class
ui = FlaskUI(app)
# ui.run()
app.run(debug=True, host="0.0.0.0", port=8080)
