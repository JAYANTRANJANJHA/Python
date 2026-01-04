import json

def csv_to_json(input_file, output_file):
    """
    Converts CSV file to JSON format
    Assumes first line contains headers
    """
    try:
        with open(input_file, 'r') as csv_file:
            # Read headers from first line
            headers = csv_file.readline().strip().split(',')
            
            data = []
            for line in csv_file:
                values = line.strip().split(',')
                if len(values) == len(headers):
                    entry = {headers[i]: values[i] for i in range(len(headers))}
                    data.append(entry)
            
        with open(output_file, 'w') as json_file:
            json.dump(data, json_file, indent=4)
            
        print(f"Successfully converted {input_file} to {output_file}")
    
    except FileNotFoundError:
        print("Error: Input file not found")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
csv_to_json('input.csv', 'output.json')
