from flask import Flask, render_template, send_from_directory, url_for
import os

app = Flask(__name__)


home_directory = os.path.expanduser("~")
shared_space = os.path.join(home_directory, 'Downloads')

#import getpass
#username = getpass.getuser() #current username
#shared_space = 'C:\\Users\\{}\\Downloads'.format(username) #Shared folder location. customize it on your need. 

@app.route('/')
@app.route('/<path:folder>/')


def index(folder=''):
	folder_path = os.path.join(shared_space, folder)
	files = get_file_list(folder_path)
	return render_template('index.html', files=files, current_folder=folder)

@app.route('/download/<path:folder>/<filename>')
def download_file(folder, filename):
	
	folder_path = os.path.join(shared_space, folder)
	return send_from_directory(folder_path, filename)

def get_file_list(folder_path):
	items = []
	for item in os.listdir(folder_path):
		item_path = os.path.join(folder_path, item)
		if os.path.isfile(item_path):
			items.append({'name': item, 'type': 'file'})
		elif os.path.isdir(item_path):
			items.append({'name': item, 'type': 'folder'})
	return items

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=8000)
