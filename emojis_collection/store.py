from .defines import DataPaths
from .utils import EmojiParser
from .utils import _create_emojis_data_struct

#EmojiParser.from_file(DataPaths.TEXT_PATH).to_json(DataPaths.JSON_PATH)
#a = EmojiParser.from_url('https://www.unicode.org/Public/emoji/12.0/emoji-test.txt')
EMOJIS = _create_emojis_data_struct(EmojiParser.from_json(DataPaths.JSON_PATH).data)
