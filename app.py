from flask import Flask, render_template, request
from foo import just_do_it
app = Flask(__name__)

@app.route("/")
def homepage():
	html = render_template('index.html')
	return html

@app.route("/results")
def results():
    reqargs = request.args
    _sortby =  reqargs.get('sortby')
    _city = reqargs.get('city')
    _county = reqargs.get('county')


    if not _city and not _county:
        return """
            <h1>Error</h1>
            <p>Must have either a city or county</p>
            <p>Go <a href="{url}">back</a></p>
        """.format(url=request.referrer)


    elif request.args.get('city'):
        search_type = 'city'
        search_val = request.args.get('city')
        peeps = just_do_it(city=search_val, sortby=_sortby)

    elif request.args.get('county'):
        search_type = 'county'
        search_val = request.args.get('county')
        peeps = just_do_it(county=search_val, sortby=_sortby)

    if len(peeps)==0:
        avg_lat=[34.055] 
        avg_lon=[-118.35];

    xlat = 0
    for p in peeps:
            xlat += float(p['latitude'])
            avg_lat = xlat / len(peeps)

    xlon = 0
    for p in peeps:
            xlon += float(p['longitude'])
            avg_lon = xlon / len(peeps)

    html = render_template('results.html', facilities=peeps, sortby=_sortby,
                            search_type=search_type, search_value=search_val,
                            center_lat=avg_lat, center_lng=avg_lon)
    return html

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
