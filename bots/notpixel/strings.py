URL_INIT = "https://app.notpx.app/?tgWebAppStartParam=f817809361"
URL_ME = "https://notpx.app/api/v1/users/me"
URL_STATUS = "https://notpx.app/api/v1/mining/status"
URL_REPAINT = "https://notpx.app/api/v1/repaint/start"
URL_CLAIM = "https://notpx.app/api/v1/mining/claim"
URL_CHECK_PXL = "https://notpx.app/api/v1/image/get/{pixel_id}"
URL_NOTCOIN_LOGIN = "https://api.notcoin.tg/auth/login"
URL_SQUAD = "https://api.notcoin.tg/squads/cryptoofficeteam/join"
URL_UPGRADE = "https://notpx.app/api/v1/mining/boost/check/{name}"
URL_TEMPLATE = "https://notpx.app/api/v1/image/template/my"
URL_SUBS_TMPLT = "https://notpx.app/api/v1/image/template/subscribe/{target_id}"


HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 9; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36 Telegram-Android/11.2.1 (Samsung SM-G973N; Android 9; SDK 28; AVERAGE)",
    "Origin": "https://app.notpx.app",
    "X-Requested-With": "org.telegram.messenger.web",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://app.notpx.app/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
    "sec-ch-ua": '"Chromium";v="91", " Not;A Brand";v="99", "Google Chrome";v="91"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "priority": "u=1, i"
}

HEADERS1 = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 9; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36 Telegram-Android/11.2.1 (Samsung SM-G973N; Android 9; SDK 28; AVERAGE)",
    "Origin": "https://webapp.notcoin.tg",
    "Sec-Fetch-Site": "same-site",
    "bypass-tunnel-reminder": "x",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://webapp.notcoin.tg/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
}