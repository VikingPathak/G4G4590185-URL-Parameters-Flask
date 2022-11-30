'''
How to Handle Missing Parameters in URL with Flask - Example 1 (try-except)
'''

## Importing required functions --------------------------------
from flask import Flask, request

## Flask constructor -------------------------------------------
app = Flask(__name__)

## Root endpoint -----------------------------------------------
@app.route('/profile')
def profile():

    ### Extract the URL parameters ###
    url_params = request.args

    ### Retrieve parameters which are present ###
    user_id  = url_params['userid']
    username = url_params['name']

    ### Retrieve parameters that is not present ###
    try:
        contact = url_params['contact']
    except KeyError:
        contact = None

    ### Return the components to the HTML template ###
    return {
        'userId': user_id,
        'userName': username,
        'userContact': contact
    }

## Main Driver Function ----------------------------------------
if __name__ == '__main__':
    ## Run the application on the local development server ##
    app.run(debug=True)
