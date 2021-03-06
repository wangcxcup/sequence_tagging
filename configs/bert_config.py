import os
from pathlib import Path
BASE_DIR = Path('slot_extraction')
bert_config = {
    'data_dir':'data',
    'vocab_file':"vocab.txt",
    'slot_list_root_path':os.path.join('data','slot_pattern'),
    'slot_file_name':"base_slot_list",
    'bert_slot_file_name':"bert_basic_slot_list",
    'bert_slot_complete_file_name':"bert_complete_slot_pattern",
    'log_dir': os.path.join('output','log'),
    'data_file_name':'orig_data_train.txt',
    'train_valid_data_dir':'train_valid_data_bert_lesslabel_hascls',
    'train_data_text_name':'train_split_data_text.npy',
    'valid_data_text_name':'valid_split_data_text.npy',
    'train_data_tag_name':'train_split_data_tag.npy',
    'valid_data_tag_name':'valid_split_data_tag.npy',
    'test_data_text_name':'test_data_text.npy',
    'test_data_tag_name':'test_data_tag.npy',
    'orig_dev':'orig_data_dev.txt',
    'orig_test':'orig_data_test.txt',
    "standard_slot_description":os.path.join('data','slot_pattern','slot_description.csv'),
    "bert_pretrained_model_path":os.path.join('data','chinese_roberta_wwm_ext_L-12_H-768_A-12'),
    "bert_config_path":"bert_config.json",
    'bert_init_checkpoints':'bert_model.ckpt',
    "bert_model_dir":os.path.join('output','model','bert_model','checkpoint'),
    "bert_model_pb":os.path.join('output','model','bert_model','saved_model'),
    "bert_ce_model_dir":os.path.join('output','model','bert_ce_model','checkpoint'),
    "bert_ce_model_pb":os.path.join('output','model','bert_ce_model','saved_model'),
    "bert_crf_model_dir":os.path.join('output','model','bert_crf_model','checkpoint'),
    "bert_crf_model_pb":os.path.join('output','model','bert_crf_model','saved_model'),
    "bert_crflstm_model_dir":os.path.join('output','model','bert_crflstm_model','checkpoint'),
    "bert_crflstm_model_pb":os.path.join('output','model','bert_crflstm_model','saved_model'),
    "bert_focaldsc_model_dir":os.path.join('output','model','bert_focaldsc_model','checkpoint'),
    "bert_focaldsc_model_pb":os.path.join('output','model','bert_focaldsc_model','saved_model'),
    "bert_lstmcrf_lesslabel_model_dir":os.path.join('output','model','bert_lstmcrf_lesslabel_model','checkpoint'),
    "bert_lstmcrf_lesslabel_model_pb":os.path.join('output','model','bert_lstmcrf_lesslabel_model','saved_model'),
    "bert_dlloss_lesslabel_model_dir":os.path.join('output','model','bert_dlloss_lesslabel_model','checkpoint'),
    "bert_dlloss_lesslabel_model_pb":os.path.join('output','model','bert_dlloss_lesslabel_model','saved_model'),
    "bert_dlloss_cslesslabel_model_dir":os.path.join('output','model','bert_dlloss_cslesslabel_model','checkpoint'),
    "bert_dlloss_cslesslabel_model_pb":os.path.join('output','model','bert_dlloss_cslesslabel_model','saved_model'),
    "bert_lstmcrf_cslesslabel_model_dir":os.path.join('output','model','bert_lstmcrf_cslesslabel_model','checkpoint'),
    "bert_lstmcrf_cslesslabel_model_pb":os.path.join('output','model','bert_lstmcrf_cslesslabel_model','saved_model'),
    "bert_celoss_cslesslabel_model_dir":os.path.join('output','model','bert_celoss_cslesslabel_model','checkpoint'),
    "bert_celoss_cslesslabel_model_pb":os.path.join('output','model','bert_celoss_cslesslabel_model','saved_model'),
    "bert_dscloss_cslesslabel_model_dir":os.path.join('output','model','bert_dscloss_cslesslabel_model','checkpoint'),
    "bert_dscloss_cslesslabel_model_pb":os.path.join('output','model','bert_dscloss_cslesslabel_model','saved_model'),

}
# print(os.path.join(config.get("train_valid_data_dir"),config.get("train_data_text_name")))
