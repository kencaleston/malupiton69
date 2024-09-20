from flask import Flask, render_template

app = Flask("sample")  # App name is "sample"

@app.route('/')
def home():
    # Set hex color to green
    hex_color = "#00FF00"  
    return render_template('index.html', color=hex_color)

if __name__ == '__main__':
    app.run(debug=True)
