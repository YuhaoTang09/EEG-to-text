import json

def create_sst_ternary_dataset(dataset_sentences_path, dictionary_path, sentiment_labels_path, output_path):
    """
    从 Stanford Sentiment Treebank 数据中生成 ternary_dataset.json。
    参数:
        dataset_sentences_path: str，datasetSentences.txt 文件路径。
        dictionary_path: str，dictionary.txt 文件路径。
        sentiment_labels_path: str，sentiment_labels.txt 文件路径。
        output_path: str，生成的 JSON 文件路径。
    """
    # 加载 datasetSentences.txt
    print(f"加载句子数据: {dataset_sentences_path}")
    sentences = {}
    with open(dataset_sentences_path, 'r', encoding='utf-8') as f:
        next(f)  # 跳过标题行
        for line in f:
            sentence_index, sentence = line.strip().split('\t')
            sentences[int(sentence_index)] = sentence

    # 加载 dictionary.txt
    print(f"加载字典数据: {dictionary_path}")
    phrase_to_id = {}
    with open(dictionary_path, 'r', encoding='utf-8') as f:
        for line in f:
            phrase, phrase_id = line.strip().split('|')
            phrase_to_id[phrase] = int(phrase_id)

    # 加载 sentiment_labels.txt
    print(f"加载情感标签数据: {sentiment_labels_path}")
    phrase_id_to_sentiment = {}
    with open(sentiment_labels_path, 'r', encoding='utf-8') as f:
        next(f)  # 跳过标题行
        for line in f:
            phrase_id, sentiment = line.strip().split('|')
            phrase_id_to_sentiment[int(phrase_id)] = float(sentiment)

    # 构建三分类数据集
    print("构建 ternary_dataset.json...")
    ternary_dataset = {}
    for sentence_index, sentence in sentences.items():
        if sentence in phrase_to_id:
            phrase_id = phrase_to_id[sentence]
            sentiment_score = phrase_id_to_sentiment.get(phrase_id, None)
            if sentiment_score is not None:
                # 根据情感分数划分为三分类
                if sentiment_score <= 0.4:
                    sentiment = "negative"
                elif sentiment_score >= 0.6:
                    sentiment = "positive"
                else:
                    sentiment = "neutral"
                ternary_dataset[sentence] = sentiment

    # 保存为 JSON 文件
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(ternary_dataset, f, indent=4, ensure_ascii=False)

    print(f"SST 三分类数据集已保存到: {output_path}")


# 示例运行
if __name__ == "__main__":
    dataset_sentences_path = 'F:/dataset/stanfordsentiment/datasetSentences.txt'
    dictionary_path = 'F:/dataset/stanfordsentiment/dictionary.txt'
    sentiment_labels_path = 'F:/dataset/stanfordsentiment/sentiment_labels.txt'
    output_path = 'F:/dataset/stanfordsentiment/ternary_dataset.json'

    create_sst_ternary_dataset(dataset_sentences_path, dictionary_path, sentiment_labels_path, output_path)
