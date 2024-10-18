# BotFarmFactory
Небольшой "фрейемворк" для создания ферм по прокачке телеграм "тапалок"

Для донатов:  
Metamask (ETH/BNB/TRX/ARB/OP): 0xd0d94B12738E627441878710FB9520f18A33B019  
SOL: GfpbfYZxsVrC3qx9S5KAtiZby5BxX3tF9wDQBAYVFfxR  
TON: UQC4PFXSqlTlrQOnnjDj8EQg8gWHNSNEyn2mv3r_kGKPCwTz  

USDT TRC20: TTTMM1PXxNS7d3tAcruamT6GE8ye5BrZ4w (автор скрипта @TotalAwesome)

Примерынй алгоритм действий:
1. В `config.py` находится конфигурация клиента Telegram, ее желательно не трогать. Так же есть флаг DEBUG. (при значении True будет писать диагностическую информацию в файл debug.log)
2. Заполнить файл `accounts.py` (`accounts_local.py`) здесь нужен номер телефона на котором висит телеграм аккаунт и прокси, через который будут ходить все тапалки на этом аккаунте
3. Устновить python 3 (если вдруг не установлен, инструкции есть в интернете)
4. Установить зависимости выполнив команду в терминале `pip install -r requirements.txt` (если перекачали скрипт, стоит каждый раз это выполнять. может измениться набор пакетов)
5. Запустить фарминг `python3 factory.py`

После запуска, бот аутентифицируется в учетках телеграма и под каждой учеткой получает токены и прочие кредсы для доступа к ботам, с которыми бот умеет работать.

В данный момент реализованы боты:

- [cellcoin_bot](https://t.me/cellcoIn_bot/app?startapp=817809361)
- [simple_tap_bot](https://t.me/Simple_Tap_Bot/app?startapp=1722504074321)
- [blum](https://t.me/blum/app?startapp=ref_SwjcZgNUK7)
- [iceberg](https://t.me/IcebergAppBot?start=referral_817809361)
- [MDAO Wallet (ZAVOD)](https://t.me/Mdaowalletbot?start=817809361)
- [anon](https://t.me/AnonEarnBot) (Если не регается, ищем рефки в интернете)
- [timeton](https://t.me/TimeTONbot?start=soloway911)
- [Solstone](https://t.me/solstonebot?start=102796269)
- [Race meme](https://t.me/Racememe_bot?start=r_817809361)
- [TapCoinsBot](https://t.me/tapcoinsbot/app?startapp=ref_jWbjCF)
- [HEXN](https://t.me/hexn_bot/app?startapp=8ea0d954-5b4b-46fe-84c4-76727ce81eb2)
- [AltOOshka](https://t.me/altooshka_bot?start=inwS2EPx37k)

Боты начнут последовательно фармить на каждом аккаунте

Если все выполнено правильно, вы увидите примерно следующую картину:
![image](https://github.com/TotalAwesome/BotFarmFactory/assets/39047158/a0e77b95-5ae1-4f64-b68d-cb904c0866b7)

Ответы почти на все вопросы уже есть в канале или в чате и в закрепе: https://t.me/cryptoearnfactory
