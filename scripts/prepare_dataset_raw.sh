echo "This scirpt construct .pickle files from .mat files from ZuCo dataset with raw EEG signals."
echo "This script also generates tenary sentiment_labels.json file for ZuCo task1-SR v1.0 and ternary_dataset.json from filtered StanfordSentimentTreebank"
echo "Note: the sentences in ZuCo task1-SR do not overlap with sentences in filtered StanfordSentimentTreebank "
echo "Note: This process can take time, please be patient..."

echo "正在处理 task1-SR..."
python ./util/construct_dataset_mat_to_pickle_v1_withRaw.py -t task1-SR || echo "task1-SR 处理失败！"

echo "正在处理 task2-NR..."
python ./util/construct_dataset_mat_to_pickle_v1_withRaw.py -t task2-NR || echo "task2-NR 处理失败！"

echo "正在处理 task3-TSR..."
python ./util/construct_dataset_mat_to_pickle_v1_withRaw.py -t task3-TSR || echo "task3-TSR 处理失败！"

echo "正在处理 task2-NR-2.0..."
python ./util/construct_dataset_mat_to_pickle_v2_withRaw.py -t task2-NR-2.0 || echo "task2-NR-2.0 处理失败！"

echo "正在处理 task3-TSR-2.0..."
python ./util/construct_dataset_mat_to_pickle_v2_withRaw.py -t task3-TSR-2.0 || echo "task3-TSR-2.0 处理失败！"

python ./util/get_sentiment_labels.py
python ./util/get_SST_ternary_dataset.py
