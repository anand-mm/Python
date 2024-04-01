from flask import Flask, send_file
import yaml

app = Flask(__name__)

@app.route('/generate_yaml')
def generate_yaml():
    # Define the new data to append
    new_data = {
        'getTenderSearchResult': {
            'method': 'GET',
            'inputs': {
                'rowNo': 'INTEGER'
            },
            'opinputs': {
                'keyword': 'VARCHAR',
                'tenderRefNo': 'VARCHAR',
                'tenderStage': 'VARCHAR',
                'tenderId': 'VARCHAR',
                'tenderStatus': 'VARCHAR'
            },
            'query': 'SELECT * from fkdjhalkfjhdsa;',
            'apiKey': '*apikey'
        }
    }

    try:
        # Load existing YAML content from application.yaml
        with open('dummyyaml.yaml', 'r') as file:
            existing_data = yaml.safe_load(file)
    except FileNotFoundError:
        # If file does not exist, initialize with an empty dictionary
        existing_data = {}

    # Append the new data to existing data
    existing_data.update(new_data)

    # Write the combined data back to the file
    with open('dummyyaml.yaml', 'a') as file:
        yaml.dump(new_data, file, default_flow_style=False)

    # Return the updated YAML file as a response
    return send_file('dummyyaml.yaml', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
