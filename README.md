# Flask-Imgur

## Not usable yet dont download it

A simple module implementing automatic image upload into imgur

Requires `imgur user id` optainable after creating imgur account.

User id can either be provided via adding it into Flask config file (via `IMGUR_ID` key) or passed during Imgur class initialization


Usage:

``` python

from flask-imgur import Imgur

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
				image: image,
				name: "kittens" # optional
				description: "cute and cuddly" # optional
				})

		print image_data["url"] # "http://www.imgur.com/kitten.jpg"
		pint image_data["height"] 

```





