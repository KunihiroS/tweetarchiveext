import json
import os

def extract_full_text(js_file, output_jsonl_file):
    with open(js_file, 'r') as f:
        content = f.read()
        json_content = content.replace('window.YTD.tweets.part0 = ', '')
        data = json.loads(json_content)
        
    with open(output_jsonl_file, 'w') as f:
        for tweet in data:
            full_text = tweet.get('tweet', {}).get('full_text', '')
            json.dump({"full_text": full_text}, f)
            f.write('\n')

# Example usage:
# Here we are using os.path.abspath to convert relative path to absolute path
# ('inputsource','outputsource')
extract_full_text(os.path.abspath('.tweets.js'), '.output.jsonl')