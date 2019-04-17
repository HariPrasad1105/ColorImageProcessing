from flask import Flask, render_template, request
import os
import cv2
import numpy as np


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('main.html')


@app.route('/color-slicing/')
def return_color_slicing_page():
    return render_template('color_slicing.html')


@app.route('/color-slicing-output/', methods=['GET', 'POST'])
def color_slicing():
    color_component, w = [int(float(request.form['red'])), int(float(request.form['green'])), int(float(request.form['blue']))], int(float(request.form['width']))
    image = request.files.get('file')
    print(image.filename, color_component, w)
    img = cv2.imread(image.filename)
    cv2.imshow('image', img)
    height, width = img.shape[0], img.shape[1]
    s = np.zeros(img.shape)
    for i in range(height):
        for j in range(width):
            pixel = img[i][j]
            s[i][j] = [128 if abs(color_component[index] - pixel[index]) > w / 2 else pixel[index] for index in range(3)]

    cv2.imwrite('E:\\Class Notes\\DIP\\ColourImageProcessing\\static\\images\\output.png', s)
    return render_template('color_slicing_output.html', filename='output.png')


if __name__ == '__main__':
    UPLOAD_FOLDER = "E:\\Class Notes\\DIP\\ColourImageProcessing\\"
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.debug = True
    app.run()
