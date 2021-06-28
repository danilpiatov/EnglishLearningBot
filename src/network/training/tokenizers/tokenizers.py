import pickle

from src.bot.constants import main_tokenizer_path, yes_no_tokenizer_path

with open(main_tokenizer_path, 'rb') as main_token:
    tokenizer = pickle.load(main_token)

with open(yes_no_tokenizer_path, 'rb') as yes_no_token:
    tokenizer_yn = pickle.load(yes_no_token)
