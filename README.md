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



## Reference:

`Imgur` (class) -- Base class for handling Imgur interaction, contructor takes following arguments:

	`app` - Flask app object
	`client_id` (optional) -- Imgur client id
	`api` -- Api endpoint to by used, default one is: `https://api.imgur.com/3/image` (optional)


`Imgur.send_image` (method) - Sends image via POST request. Available arguments:

	`image_data` (dict) -- dictionary containing image data to be sent to the server:
			`image` -- Werkzeug file object containing image, received through file upload (required)
			`name` -- image name (optional)
			`description` -- image description (optional)

	`send_params` (dict) -- any additional parameters to be added to POST request (optional)
	`additional_headers` (dict) -- any headers you would like to add to request (optional)

`Imgur.delete_image` (method) -- delete image. Available arguments:
	`delete_hash` (string) -- unique string obtained when sending image to Imgur (required)
	`additional_headers` (dict) -- any additional headers to be added to request

