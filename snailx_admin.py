import sys
sys.path.insert(0, '/vagrant/repos/snailx_admin_panel')
import os
from flask import render_template
from globals.globals import app


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
