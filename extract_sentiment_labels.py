import json
import scipy.io

def extract_sentiment_labels(mat_file_paths, output_path):
    """
    从多个 ZuCo task1-SR 的 .mat 文件中提取情感标签，保存为 sentiment_labels.json。
    参数:
        mat_file_paths: list，ZuCo task1-SR 的 .mat 文件路径列表。
        output_path: str，生成的 sentiment_labels.json 文件路径。
    """
    sentiment_labels = {}

    for mat_file_path in mat_file_paths:
        print(f"正在处理 {mat_file_path}...")
        # 加载 .mat 文件
        mat_data = scipy.io.loadmat(mat_file_path)
        # 提取 sentenceData 字段（句子数据）
        sentence_data = mat_data['sentenceData']

        # 遍历每个句子，提取句子内容和情感标签
        for sentence in sentence_data:
            # 提取句子内容（content）和情感标签（label）
            content = sentence['content'][0][0] if 'content' in sentence.dtype.names else None
            label = sentence['label'][0][0] if 'label' in sentence.dtype.names else None

            # 仅在内容和标签均存在时添加到字典中
            if content and label is not None:
                sentiment_labels[content] = int(label)  # 将标签转为整数

    # 将结果保存为 JSON 文件
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(sentiment_labels, f, indent=4, ensure_ascii=False)

    print(f"情感标签已保存到 {output_path}")

# 示例运行
if __name__ == "__main__":
    # 修改为你的 .mat 文件路径列表
    mat_file_paths = [
        'F:/dataset/ZuCo/task1-SR/Matlab_files/resultsZAB_SR.mat',
        'F:/dataset/ZuCo/task1-SR/Matlab_files/resultsZDM_SR.mat',
        'F:/dataset/ZuCo/task1-SR/Matlab_files/resultsZJN_SR.mat',
        'F:/dataset/ZuCo/task1-SR/Matlab_files/resultsZDN_SR.mat',
        'F:/dataset/ZuCo/task1-SR/Matlab_files/resultsZGW_SR.mat',
        'F:/dataset/ZuCo/task1-SR/Matlab_files/resultsZJM_SR.mat',
        'F:/dataset/ZuCo/task1-SR/Matlab_files/resultsZJS_SR.mat',
        'F:/dataset/ZuCo/task1-SR/Matlab_files/resultsZKB_SR.mat',
        'F:/dataset/ZuCo/task1-SR/Matlab_files/resultsZKH_SR.mat',
        'F:/dataset/ZuCo/task1-SR/Matlab_files/resultsZKW_SR.mat',
        'F:/dataset/ZuCo/task1-SR/Matlab_files/resultsZMG_SR.mat',
        'F:/dataset/ZuCo/task1-SR/Matlab_files/resultsZPH_SR.mat',

        # 添加其他受试者的 .mat 文件路径
    ]

    # 修改为你的输出文件路径
    output_path = 'F:/dataset/ZuCo/task1-SR/sentiment_labels/sentiment_labels.json'

    # 提取情感标签
    extract_sentiment_labels(mat_file_paths, output_path)
