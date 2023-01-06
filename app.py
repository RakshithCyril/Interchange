import requests
import os
from bs4 import BeautifulSoup
from flask import *
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# picFolder = os.path.join('static','images')
# app.config['UPLOAD_FOLDER'] = picFolder
# print('Enter Year:')
# year = input()
# print('Enter Make:')
# make = input()
# print('Enter Model:')
# model = input()
# print('Enter part:')
# part = input()


# ui = '{}/{}/{}/{}/{}'.format(year, make, model, part, part1)
#

# url = 'https://www.hollanderparts.com/used-auto-parts/2006/honda/civic/engine/300-engine'


test1 = []
test2 = []


@app.route('/', methods=['get', 'post'])
def form():
    # back = os.path.join(app.config['UPLOAD_FOLDER'],'background.png')
    return render_template("index.html")


@app.route('/post', methods=['POST', 'get'])
@cross_origin()
def req():
    test = []
    year = request.form['year']
    # print(year)
    make = request.form['make']
    # print(make)
    model = request.form['model']
    # print(model)
    part = request.form['part'].replace(" ","-").lower()
    # print(part)
    category = request.form['cat'].replace(" ","-").lower()
    # print(category)

    ui = '{}/{}/{}/{}/{}'.format(year, make, model, category, part)
    url = "https://www.hollanderparts.com/used-auto-parts/" + ui
    print(url)
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')

    if soup == " ":
        print("Invalid")
    else:

        for div in soup.findAll('div', attrs={'class': 'ymmSelection'}):
            v = (div.find('a')['href'])
            v1 = (v.split('/', 7)[7])
            code = v1.split('-')[0]
            dash = code + '-'

            test1.append(dash)

            code_ext = v1.split('-')[1].upper()
            test2.append(code_ext)

            spec = v1.split('-', 2)
            ren = spec[2].replace('-'," ").upper()
            spec[-1] = ren


            # print(spec)
            test.append(spec)

    test = test[:-1]

    # print(tabulate(test))

    return render_template("result.html", phoe=test)
    # return jsonify(test)

# @app.route('/', methods=['GET'])
# def display_dat():
#     # data_set = {'Specs': f'{test}'}
#     # data_set = {'S': str(dev)}
#     # json_dump = json.dumps(data_set)
#     # return jsonify(data_set)
#     # print('Intr: %s-%s\nSpec: %s' % (code, code_ext, spec))
#     return render_template("display_dat.html")


if __name__ == '__main__':
    app.run()
