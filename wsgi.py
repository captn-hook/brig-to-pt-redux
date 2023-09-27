from server import app
print("running", __name__)
if __name__ == '__main__':
    print("running2")
    app.run(host='localhost', port=6743, debug=True)