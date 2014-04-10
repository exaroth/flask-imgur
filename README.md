# Flask-Imgur

## Not usable yet dont download it

A simple module implementing automatic image upload into Imgur file sharing service. Imgur does have rather big and convoluted API, this library is meant for those who simply want to upload and delete images from their service with no additional hassle.

For Flask-Imgur to work properly you need `client_id` API key optainable

`user id` can either be provided via Flask config file (with `IMGUR_ID` key) or passed during Imgur class initialization


Usage:

``` python
from flask_imgur import Imgur

app = Flask(__name__)

imgur_handler = Imgur(app, client_id ="xyz")
```

Then inside a function:


``` python
@app.route("/image_upload", methods=["GET","POST"])
def get_img():
	if request.method == "POST":
		image = request.files.get("my_image")
		image_data = imgur_handler.send_image({
				"image": image,
				"name": "kittens" # optional
				"description": "cute and cuddly" # optional
				})

		image_data["success"] # True
		image_data["data"]["title"]  # "kittens"
		image_data["data"]["height"] # 200
		image_data["data"]["link"] # "http://imgur.com/SbBGk.jpg"
		image_data["data"]["deletehash"] # "eYZd3NNJHsbreD1"
```

Refer to [Official model reference](https://api.imgur.com/models/image) for info about available fields.


Another thing you might wanna do is to delete the image, this requires `deletehash` created when image been uploaded. Example:

``` python
	delete_info = imgur_handler.delete_image(delete_hash="eYZd3NNJHsbreD1")
	delete_info["success"] # True
```


#### send_image(image_data, send_params, additionale_headers)

Send Werkzeug file object containing image into imgut

* image_data (dict) -- Dictionary containing image object aswell as optional title and description
* send_params (dict) -- Any additional data to be added to POST request (optional)
* additional_headers (dict) -- Additional headers to be passed along with request (optional)

#### delete_image(delete_hash, additional_headers)

Delete the image

* delete_hash (string) -- Pass `deletehash` obtained when sending image to Imgur
* additional_headers (dict) -- any additional headers to be added to request

