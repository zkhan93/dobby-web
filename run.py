import web

app = web.create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8011, debug=True)

