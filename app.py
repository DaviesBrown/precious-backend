from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Koyeb'

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.json  # Assuming the data is sent as JSON
    submitted_at = data.get('Submitted at')
    name = data.get('What is the name of the Product / Service')
    product_description = data.get('What is the product / service')
    product_purpose = data.get('What does this product / service do')
    features = data.get('What are the main features / benefits / What is included')
    extra_info = data.get('Any extra description / info you would want in')
    product_link = data.get('Product / Service Link')
    product_images = data.get('Product / Service Images')
    link_field = data.get('Untitled link field')
    file_upload_field = data.get('Untitled file upload field')

    # Here you can process the data as per your requirements
    # For now, let's just print it
    print("Submitted at:", submitted_at)
    print("Name:", name)
    print("Product Description:", product_description)
    print("Product Purpose:", product_purpose)
    print("Features:", features)
    print("Extra Info:", extra_info)
    print("Product Link:", product_link)
    print("Product Images:", product_images)
    print("Link Field:", link_field)
    print("File Upload Field:", file_upload_field)

    # You can add your business logic here, like saving the data to a database

    return 'OK', 200

if __name__ == "__main__":
    app.run()
