from flask import Flask, rendering_template 
app = Flask(__name__)   

@app.route('/')      
def render_lists():


    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

    return rendering_template('list.html', users = users)



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    


    app.run(debug=True, port=5005)    # Run the app in debug mode.

