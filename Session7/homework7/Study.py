from flask import Flask,redirect
app = Flask(__name__)

@app.route('/about-me')
def about_me():
    return """Name: Thắng 
    Work: Video Producer 
    School: FTU 
    Hobbies: Games, football, movies, musics
    """

@app.route('/school')
def school_redirect():
    return redirect('http://techkids.vn')
    
if __name__ == "__main__":
    app.run(debug=True)