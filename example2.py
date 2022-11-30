'''
How to Handle Missing Parameters in URL with Flask - Example 1 (get() method)
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

    ### Retrieve parameters using get() ###
    user_id  = url_params.get('userid')
    username = url_params.get('name')
    # If contact is not present then 'NA' will be the default value
    contact  = url_params.get('contact', 'NA')

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
