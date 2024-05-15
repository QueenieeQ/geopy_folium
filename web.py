from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def map():
    # province = request.args.get('province')
    # return render_template('map.html', province=province)
    return render_template('map.html')

# Validate the province name
@app.route('/validate_province', methods=['POST'])
def validate_province():
    data = request.json
    province = data['province']

    # Add your validation logic here (e.g., check if the province name is correct)

    # For demonstration purposes, let's assume the province name is "Hanoi"
    valid = (province.lower() == 'hanoi')

    return jsonify({'valid': valid})

if __name__ == '__main__':
    app.run(debug=True)