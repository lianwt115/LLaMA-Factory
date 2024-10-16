#SDK模型下载
from modelscope import snapshot_download
#model_dir0 = snapshot_download('OpenBuddy/openbuddy-llama3.1-8b-v22.1-131k')
#model_dir2 = snapshot_download('Qwen/Qwen2-7B-Instruct-AWQ',cache_dir='./')
#model_dir1 = snapshot_download('Qwen/Qwen2-7B-Instruct',cache_dir='./')
model_dir1 = snapshot_download('Qwen/Qwen2.5-3B-Instruct')
#model_dir3 = snapshot_download('Qwen/Qwen2-1.5B')
#训练模型  使用qlora 训练
#model_dir = snapshot_download('Qwen/Qwen2-7B-Instruct-GPTQ-Int4')