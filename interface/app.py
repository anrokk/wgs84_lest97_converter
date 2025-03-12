from flask import Flask, request, render_template
from converter.transformations import wgs84_to_lest97, lest97_to_wgs84

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            coord1 = float(request.form['coord1'])
            coord2 = float(request.form['coord2'])
            conversion_type = request.form['conversion_type']

            if conversion_type == 'wgs84_to_lest97':
                result = wgs84_to_lest97(coord1, coord2)
            else:
                result = lest97_to_wgs84(coord1, coord2)
        except ValueError:
            result = "Invalid input. Enter numeric values."

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)

