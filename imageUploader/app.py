# Code based on pythonbuddy.com

from flask import Flask, render_template, request, jsonify, session, flash

# Configure Flask App
# Remember to change the SECRET_KEY!
app = Flask(__name__)
app.config['SECRET_KEY'] = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
app.config['DEBUG'] = True

@app.route('/')
def index():
    """Display home page
        :return: index.html
    """
    session["count"] = 0
    return render_template("index.html")

'''
BEGIN TASK 1
'''
counts = {}

# Should you use a GET or POST Request? POST
@app.route('/submit_image', methods=['POST'])
# @app.route('/submit_image', methods=['GET'])

def submit_image():
    """Adds an image to our server and adds it to our webpage. 
        Automatically refreshes our webpage so that user can see the image appended
    """
    # Setting up the necessary variables that will be used
    if session["count"] == 0:
        session["images"] = []
        session["count"] += 1
    
    # checking that the files exist
    if request.files:

        # getting the image that will be uploaded
        image = request.files["image_to_be_uploaded"]

        # getting the size of the image
        length = request.content_length

        # Checking that there is an uploaded file
        if image.filename != '' and length != 0:

            # Checking that the filename has no spaces            
            if " " not in image.filename:
                img = image.filename

                # Checking the upload size
                if length > 20 * 1024 * 1024:

                    # If the current title exist
                    if img in session["images"]:
                        counts[img] += 1
                        img = image.filename + "("+ str(counts[img]) +")"
                    else:
                        counts[img] = 0

                    # Saving the image on the servere side
                    image.save("static/" + img)

                    # updating the session variables
                    curr = session["images"]
                    curr.append(img)
                    session["images"] = curr
                    return render_template('index.html', files = session["images"])

                # Showing user a message to ask to lower the upload size
                else:
                    flash("Please don't upload an image more than 20MB")
                    return render_template('index.html', files = session["images"])

            # Showing user a message to ask to change the filename
            else:
                flash("Please remove spaces from your filename!")
                return render_template('index.html', files = session["images"])

        # If there isn't an uploaded photo, then display messagee to users
        else:
            flash("Please select a photo before you submit!")
            return render_template('index.html', files = session["images"])
            
'''
END TASK 1
'''