URL_WEBAPP_INIT = "https://telegram.blum.codes/"
URL_ME = "https://user-domain.blum.codes/api/v1/user/me"
URL_NOW = "https://game-domain.blum.codes/api/v1/time/now"
URL_AUTH = "https://user-domain.blum.codes/api/v1/auth/provider/PROVIDER_TELEGRAM_MINI_APP"
URL_REFRESH_TOKEN = "https://user-domain.blum.codes/api/v1/auth/refresh"
URL_BALANCE = "https://game-domain.blum.codes/api/v1/user/balance"
URL_TASKS = "https://earn-domain.blum.codes/api/v1/tasks" 
URL_TASK_START = "https://earn-domain.blum.codes/api/v1/tasks/{id}/start"
URL_TASK_VALIDATE = "https://earn-domain.blum.codes/api/v1/tasks/{id}/validate"
URL_TASK_CLAIM = "https://earn-domain.blum.codes/api/v1/tasks/{id}/claim" 
URL_FARMING_CLAIM = "https://game-domain.blum.codes/api/v1/farming/claim"  
URL_FARMING_START = "https://game-domain.blum.codes/api/v1/farming/start"  
URL_PLAY_START = "https://game-domain.blum.codes/api/v2/game/play"  
URL_PLAY_CLAIM = "https://game-domain.blum.codes/api/v2/game/claim" 
URL_DAILY_REWARD = "https://game-domain.blum.codes/api/v1/daily-reward?offset=-180"
URL_FRIENDS_BALANCE = "https://user-domain.blum.codes/api/v1/friends/balance"
URL_FRIENDS_CLAIM = "https://user-domain.blum.codes/api/v1/friends/claim"
URL_CHECK_NAME = "https://user-domain.blum.codes/api/v1/user/username/check"
URL_TASKS_CODES = "https://gist.githubusercontent.com/SoloWay9/241c1666ad8fea3c8e93dc074e99a401/raw/29fdf3d73e3bf6910fc1b71dcaf1b02fe6cfef92/blum_codes.json"

MSG_AUTH = "Получение токена"
MSG_REFRESH = "Обновление токена"
MSG_BALANCE_UPDATE = "Обновление баланса"
MSG_BALANCE_INFO = "Баланс: {balance} Количество игр: {play_passes}"
MSG_START_FARMING = "Начал фармить"
MSG_CLAIM_FARM = "Собрал нафармленное: {amount}"
MSG_FARMING_WAIT = "Ожидание завершения фарминга {} секунд"
MSG_BEGIN_GAME = "Начинаем тапать звездочки. Количество игр: {})"
MSG_PLAYED_GAME = "Натапал: {result}"
MSG_GAME_OFF = "Мини-игра в звездочки отключена"
MSG_DAILY_REWARD = "Ежедневная награда. День: {days} игры: {passes} монеты: {points}"
MSG_FRIENDS_CLAIM = "Друзья нафармили: {points}"
MSG_INPUT_USERNAME = "Введи имя для Blum: "
MSG_TASK_STARTED = "Начал выполнять таску {title}"
MSG_TASK_CLAIMED = "Выполнил таску {title} на {reward} монет"

HEADERS = {
    "Accept": 'application/json',
    "Accept-Encoding": 'gzip, deflate, br, zstd',
    "Accept-Language": 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    "Origin": 'https://telegram.blum.codes',
    "Referer": 'https://telegram.blum.codes/',
    "Sec-Ch-Ua-Mobile": '?1',
    "Sec-Ch-Ua-Platform": 'Android"',
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

TOKEN_FILE = "token.json"

TASK_CODES = {
    "Secure your Crypto!": "BEST PROJECT EVER",
    "Backing from Binance Labs": "VALUE",
    "Forks Explained": "GO GET",
    "Navigating Crypto": "HEYBLUM",
    "What are Telegram Mini Apps?": "CRYPTOBLUM",
    "Say No to Rug Pull!": "superblum",
    "What Are AMMs?": "CRYPTOSMART",
    "Liquidity Pools Guide": "BLUMERSSS",
    "$2.5M+ DOGS Airdrop": "HAPPYDOGS",
    "Doxxing? What's that?": "NODOXXING",
}
