from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Koyeb'

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.json  # Assuming the data is sent as JSON
    event_id = data.get('eventId')
    event_type = data.get('eventType')
    created_at = data.get('createdAt')
    form_data = data.get('data')

    response_id = form_data.get('responseId')
    submission_id = form_data.get('submissionId')
    respondent_id = form_data.get('respondentId')
    form_id = form_data.get('formId')
    form_name = form_data.get('formName')
    form_created_at = form_data.get('createdAt')
    fields = form_data.get('fields', [])

    parsed_data = {}
    for field in fields:
        key = field.get('key')
        label = field.get('label')
        value = field.get('value')
        parsed_data[key] = value

    # Extracting specific fields
    name = parsed_data.get('question_8NjYQo')
    product_description = parsed_data.get('question_0VoY6Q')
    product_purpose = parsed_data.get('question_zEWADE')
    features = parsed_data.get('question_5XEY1b')
    extra_info = parsed_data.get('question_dbQoxN')
    product_link = parsed_data.get('question_YjVbW0')
    product_images = parsed_data.get('question_Dq0odp')
    link_field = parsed_data.get('question_laVjd6')
    file_upload_field = parsed_data.get('question_RW8Q5P')

    # Here you can process the data as per your requirements
    # For now, let's just print it
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
