训练前
===
    \hover_net\models\hovernet\opt.py
    1.修改返回字典["phase_list"][0]["run_info"]["net"]["pretrained"] -> pretrained模型的路径
    2.["phase_list"][0]["run_info"]["batch_size"]["train"]和["vaild"] -> 8, 8
    3.["run_engine"]["train"]["nr_procs"] -> 0
    4.["run_engine"]["vaild"]["nr_procs"] -> 0

    \hover_net\config.py
    1.修改class Config的__init__函数属性log_dir
    2.train_dir_list和vaild_dir_list
