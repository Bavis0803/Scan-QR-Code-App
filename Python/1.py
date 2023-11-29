from flask import Flask, request,jsonify
import werkzeug
from qr import qr
app = Flask(__name__)
@app.route('/')
def home():
    return 'Hello'
@app.route('/upload', methods=['GET','POST'])
def upload_image():
    if(request.method == "POST"):
        imagefile = request.files['image']
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        imagefile.save("./uploadedimages/" + filename)
        data = qr(f"uploadedimages/{filename}")
        print(data)
        return jsonify({
            "message": "Image uploaded Successfully"
        })
    elif(request.method == "GET"):
        data_for_get = {"data": data}
        return jsonify(data_for_get)
if __name__ == '__main__':
    app.run(debug=True,port=4000)
