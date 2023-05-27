import json

def preprocess_jsonl(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for line in file:
                data = json.loads(line)
                text = data["full_text"]
                # 不要な要素の削除
                text = text.replace("full_text", "")
                text = ' '.join(word for word in text.split() if not word.startswith('http'))
                text = ' '.join(word for word in text.split() if not word.startswith('#'))
                # 必要なデータのみを含む辞書を作成
                processed_data = {"text": text.strip()}
                # 出力ファイルに書き込み
                outfile.write(json.dumps(processed_data, ensure_ascii=False) + '\n')

# ファイルパスを指定してプリプロセスを実行
preprocess_jsonl('tweetarchiveext/output.jsonl', 'output_cleaned.jsonl')