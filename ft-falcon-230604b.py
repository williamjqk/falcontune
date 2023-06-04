'''
!git clone https://github.com/williamjqk/falcontune.git

%cd falcontune/

!pip install -r requirements.txt

!python setup.py install

!wget https://github.com/gururise/AlpacaDataCleaned/raw/main/alpaca_data_cleaned.json

!wandb login $personal_key_for_api

!falcontune finetune \
    --model=falcon-7b \
    --weights=tiiuae/falcon-7b \
    --dataset=./alpaca_data_cleaned.json \
    --data_type=alpaca \
    --lora_out_dir=./falcon-7b-alpaca/ \
    --mbatch_size=1 \
    --batch_size=2 \
    --epochs=3 \
    --lr=3e-4 \
    --cutoff_len=256 \
    --lora_r=8 \
    --lora_alpha=16 \
    --lora_dropout=0.05 \
    --warmup_steps=5 \
    --save_steps=50 \
    --save_total_limit=3 \
    --logging_steps=5 \
    --target_modules='["query_key_value"]'

'''