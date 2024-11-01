import time
import requests
import random
import json
from bots.base.base import BaseFarmer
from bots.base.utils import api_response
from .strings import *
from .configs import *

class BotFarmer(BaseFarmer):
    name = "notpixel"
    extra_code = "f817809361"
    init_data = None
    initialization_data = dict(peer=name, bot=name, url=URL_ME, start_param=extra_code)
    refreshable_token = True
    codes_to_refresh = (401,)

    def set_headers(self, *args, **kwargs):
        self.headers = HEADERS.copy()
        self.get = api_response(super().get)
        self.post = api_response(super().post) 

    def set_headers1(self, *args, **kwargs):
        self.headers1 = HEADERS1.copy()      

    def authenticate(self, *args, **kwargs):
        try:
            init_data = self.initiator.get_auth_data(**self.initialization_data)
            self.auth_data = init_data["authData"]
            self.headers["Authorization"] = f"initData {self.auth_data}"
            self.get(URL_ME, headers=self.headers, json={'tg_data': self.auth_data})
        except Exception as e:
            self.error(f"Ошибка во время аутентификации: {e}")
            raise

    def refresh_token(self, *args, **kwargs):
        self.initiator.connect()
        self.authenticate()
        self.initiator.disconnect()

    def set_start_time(self):
        self.start_time = time.time() + random.randint(MIN_WAIT, MAX_WAIT) * 60

    def get_balance(self):
        try:
            response = self.get(URL_STATUS, headers=self.headers)
            data = response

            user_balance = round(data.get("userBalance", 0), 3)
            charges = data.get("charges", 0)
            max_charges = data.get("maxCharges", 0)
            league = data.get("league", "").upper()

            balance_info = f'Balance: {user_balance} | {charges}/{max_charges} - Energy | League: {league}'

            self.log(balance_info)
            return balance_info
        except Exception as error:
            self.error(f"Unknown error during processing balance: {error}")
            return None
        
    def get_squad(self):
        try:
            response = requests.get(URL_ME, headers=self.headers)
            response.raise_for_status()
            data = response.json()

            if 'squad' in data and data['squad']['id'] == 645506:
                return True
            else:
                self.authenticate_and_join_squad()
                return False
        except Exception:
            return False

    def authenticate_and_join_squad(self):
        try:
            self.initiator.connect()
            self.set_headers1()
            name = 'notgames_bot'
            self.initialization_data1 = dict(peer=name, bot=name, url=URL_NOTCOIN_LOGIN)
            init_data = self.initiator.get_auth_data(**self.initialization_data1)
            self.auth_data = init_data["authData"]
            response = requests.post(URL_NOTCOIN_LOGIN, headers=self.headers1, json={'webAppData': self.auth_data})
            
            if response.status_code == 201:
                self.token = response.json()
                if 'data' in self.token and 'accessToken' in self.token['data']:
                    access_token = self.token['data']['accessToken']
                    if access_token:
                        self.headers1["X-Auth-Token"] = f"Bearer {access_token}"
                        response_join = requests.post(URL_SQUAD, headers=self.headers1)
                        if response_join.status_code not in [201, 400]:
                            raise Exception("Failed to join squad")
            self.initiator.disconnect()
        except Exception:
            pass

    def my_template(self):
        target_id = 1972552043
        for attempt in range(3):  # Попытки до 3 раз
            try:
                response = requests.get(URL_TEMPLATE, headers=self.headers)
                response.raise_for_status()
                data = response.json()

                current_id = data.get("id")

                if current_id != target_id:
                    subscribe_response = requests.put(URL_SUBS_TMPLT.format(target_id=target_id), headers=self.headers)
                    subscribe_response.raise_for_status()
                    if subscribe_response.status_code == 204:
                        pass
                break 
            except requests.exceptions.HTTPError:
                if attempt < 2:
                    time.sleep(2)
                else:
                    pass
        
    def check_pixel_color(self, x, y):
        pixel_id = int(f'{y}{x}') + 1
        url = f"https://notpx.app/api/v1/image/get/{pixel_id}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            current_color = data.get("pixel", {}).get("color")
            return current_color
        except Exception as error:
            self.error(f"Error checking pixel color at ({x}, {y}): {error}")
            return None

    def select_pixel_to_paint(self, x_diaposon, y_diaposon, color):
        for _ in range(50):  # Максимум попыток найти пиксель для закрашивания
            x = random.randint(x_diaposon[0], x_diaposon[1])
            y = random.randint(y_diaposon[0], y_diaposon[1])
            current_color = self.check_pixel_color(x, y)
            if current_color != color:
                return x, y
        return None, None

    def draw(self):
        while True:
            try:
                response = requests.get(URL_STATUS, headers=self.headers)
                response.raise_for_status()
                data = response.json()
                charges = data['charges']

                if charges == 0:
                    self.log(f"No energy")
                    break 

                for _ in range(charges):
                    diaposons_with_colors = list(zip(DRAW_X_DIAPOSON, DRAW_Y_DIAPOSON, DRAW_COLORS))
                    x_diaposon, y_diaposon, color = random.choice(diaposons_with_colors)

                    x, y = self.select_pixel_to_paint(x_diaposon, y_diaposon, color)
                    if x is None or y is None:
                        self.log(f"Could not find a pixel to paint with color {color}. Skipping.")
                        continue

                    pixel_id = int(f'{y}{x}') + 1
                    payload = {
                        "pixelId": pixel_id,
                        "newColor": color
                    }

                    draw_request = requests.post(URL_REPAINT, headers=self.headers, json=payload)
                    draw_request.raise_for_status()
                    if draw_request.status_code == 400:
                        self.log(f"Received 400 error during painting. Restarting draw function.")
                        break

                    data = draw_request.json()
                    self.log(f"Painted (X: {x}, Y: {y}) with color {color} | Balance {'{:,.3f}'.format(data.get('balance', 'unknown'))}")
                    time.sleep(random.randint(5, 10))

            except Exception as error:
                self.error(f"Unknown error during painting: {error}")
                break

    def upgrade(self):
        try:
            while True:
                response = requests.get(URL_STATUS, headers=self.headers)
                response.raise_for_status()
                data = response.json()

                boosts = data['boosts']

                self.log(f"Boosts Levels: Energy Limit - {boosts['energyLimit']} | Paint Reward - {boosts['paintReward']} | Recharge Speed - {boosts['reChargeSpeed']}")

                if boosts['energyLimit'] >= ENERGY_LIMIT_LVL and boosts['paintReward'] >= PAINT_REWARD_LVL and boosts['reChargeSpeed'] >= RE_CHARGE_SPEED_LVL:
                    return

                for name, level in sorted(boosts.items(), key=lambda item: item[1]):
                    if name == 'energyLimit' and level >= ENERGY_LIMIT_LVL:
                        continue

                    if name == 'paintReward' and level >= PAINT_REWARD_LVL:
                        continue

                    if name == 'reChargeSpeed' and level >= RE_CHARGE_SPEED_LVL:
                        continue

                    try:
                        res = requests.get(URL_UPGRADE.format(name=name), headers=self.headers)
                        res.raise_for_status()

                        self.log(f"Upgraded boost: {name}")

                        time.sleep(random.randint(2, 5))
                    except Exception as error:
                        self.log(f"Not enough PX to keep upgrading")

                        time.sleep(random.randint(5, 10))
                        return

        except Exception as error:
            self.error(f"Unknown error during upgrading: {error}")
            time.sleep(3)


    def claim_mine(self):
        try:
            response = requests.get(URL_STATUS, headers=self.headers)
            response.raise_for_status()
            response_json = response.json()

            time.sleep(random.randint(4, 6))

            response = requests.get(URL_CLAIM, headers=self.headers)
            response.raise_for_status()
            response_json = response.json()

            claimed = response_json['claimed']
            self.log(f"Claim reward: {'{:,.3f}'.format(claimed)}")
            return claimed
        except Exception as error:
            self.log(f"Unknown error during claiming reward: {error}")
            time.sleep(3)
            return None

    def farm(self):
        self.get_balance()
        self.get_squad()
        self.my_template()
        self.draw()
        self.claim_mine()
        self.upgrade()
