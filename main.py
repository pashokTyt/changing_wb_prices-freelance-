import requests

Authorization_token = "some_token"

market_price = {
    "prices": {
        98486: {1000},
        123456: {1500},
        789012: {900},
    }
}

response = {
    "data": {
        "listGoods": [
            {
                "nmID": 98486,
                "vendorCode": "07326060",
                "sizes": [
                    {
                        "sizeID": 3123515574,
                        "price": 500,
                        "discountedPrice": 350,
                        "clubDiscountedPrice": 332.5,
                        "techSizeName": "42",
                        "currencyIsoCode4217": "RUB",
                        "discount": 30,
                        "clubDiscount": 5,
                        "editableSizePrice": True
                    },
                    {
                        "sizeID": 3123515575,
                        "price": 520,
                        "discountedPrice": 400,
                        "clubDiscountedPrice": 380,
                        "techSizeName": "44",
                        "currencyIsoCode4217": "RUB",
                        "discount": 23,
                        "clubDiscount": 5,
                        "editableSizePrice": True
                    }
                ]
            },
            {
                "nmID": 123456,
                "vendorCode": "A12345",
                "sizes": [
                    {
                        "sizeID": 4123515574,
                        "price": 1500,
                        "discountedPrice": 1200,
                        "clubDiscountedPrice": 1140,
                        "techSizeName": "M",
                        "currencyIsoCode4217": "RUB",
                        "discount": 20,
                        "clubDiscount": 5,
                        "editableSizePrice": False
                    }
                ]
            },
            {
                "nmID": 789012,
                "vendorCode": "B98765",
                "sizes": [
                    {
                        "sizeID": 5123515574,
                        "price": 800,
                        "discountedPrice": 720,
                        "clubDiscountedPrice": 684,
                        "techSizeName": "L",
                        "currencyIsoCode4217": "RUB",
                        "discount": 10,
                        "clubDiscount": 5,
                        "editableSizePrice": True
                    },
                    {
                        "sizeID": 5123515575,
                        "price": 850,
                        "discountedPrice": 765,
                        "clubDiscountedPrice": 726.75,
                        "techSizeName": "XL",
                        "currencyIsoCode4217": "RUB",
                        "discount": 10,
                        "clubDiscount": 5,
                        "editableSizePrice": True
                    }
                ]
            }
        ]
    },
    "error": False,
    "errorText": "",
    "additionalErrors": None
}

# imitation API


def parse_wildberries(limit, offset, filterNmID, Authorization):
    url = "https://discounts-prices-api.wildberries.ru/api/v2/list/goods/filter"
    headers = {"Authorization": Authorization}
    params = {
        "limit": limit,
        "offset": offset,
        "filterNmID": filterNmID,
    }
    response = requests.get(url=url, headers=headers, params=params)
    return response.json()


# response = parse_wildberries( ... )
# market_price from table( excel, DB etc... )


def update_price_wildberries(nmID, price, discount, Authorization):
    url = "https://discounts-prices-api.wildberries.ru/api/v2/upload/task"
    headers = {"Authorization": Authorization}
    params = {
        "nmID": nmID,
        "price": price,
        "discount": discount,
    }
    response = requests.get(url=url, headers=headers, params=params)
    return response.json()


def get_wildberries_product_name(nmID, Authorization):
    url = "https://content-api.wildberries.ru/content/v2/get/cards/list"

    params = {
        "Authorization": Authorization,
        "settings": {
            "sort": {
                "ascending": "true",  # по возрастанию
            },
            "filter": {
                "textSearch": nmID,
            },
        },
    }

    # response = requests.get(url=url, params=params)

    response = {

        "cards":

        [

            {

                "nmID": 12345678,
                "imtID": 123654789,
                "nmUUID": "01bda0b1-5c0b-736c-b2be-d0a6543e9be",
                "subjectID": 7771,
                "subjectName": "AKF системы",
                "vendorCode": "wb7f6mumjr1",
                "brand": "Тест",
                "title": "Тест-система",
                "description": "Тестовое описание",
                "needKiz": False,
                "photos":

                [

                    {
                        "big": "https://basket-10.wbbasket.ru/vol1592/part159206/159206280/images/big/1.webp",
                        "c246x328": "https://basket-10.wbbasket.ru/vol1592/part159206/159206280/images/c246x328/1.webp",
                        "c516x688": "https://basket-10.wbbasket.ru/vol1592/part159206/159206280/images/c516x688/1.webp",
                        "square": "https://basket-10.wbbasket.ru/vol1592/part159206/159206280/images/square/1.webp",
                        "tm": "https://basket-10.wbbasket.ru/vol1592/part159206/159206280/images/tm/1.webp"
                    }

                ],
                "video": "https://videonme-basket-12.wbbasket.ru/vol137/part22557/225577433/hls/1440p/index.m3u8",
                "dimensions":
                {

                    "length": 55,
                    "width": 40,
                    "height": 15,
                    "weightBrutto": 6.24,
                    "isValid": False

                },
                "characteristics":
                [

                    {

                        "id": 14177449,
                        "name": "Цвет",
                        "value":

                        [
                            "красно-сиреневый"
                        ]
                    }

                ],
                "sizes":
                [

                    {

                        "chrtID": 316399238,
                        "techSize": "0",
                        "skus":

                        [
                            "987456321654"
                        ]
                    }

                ],
                "tags":
                [

                    {
                        "id": 592569,
                        "name": "Популярный",
                        "color": "D1CFD7"
                    }
                ],
                "createdAt": "2023-12-06T11:17:00.96577Z",
                "updatedAt": "2023-12-06T11:17:00.96577Z"
            }

        ],
        "cursor":

        {
            "updatedAt": "2023-12-06T11:17:00.96577Z",
            "nmID": 123654123,
            "total": 1
        }

    }
    name = response.get("cards", []).get("title")
    return name


def telegram_notification(marketplace, product_name):
    message = f"Маркетплейс: {marketplace}/n {product_name}"
    

def price_comparation(market_price, response):
    market_prices = market_price.get("prices", {})
    list_goods = response.get("data", {}).get("listGoods", [])

    for product in list_goods:
        nmID = product.get("nmID")
        if nmID not in market_prices:
            print(
                f"Товар с nmID={nmID} отсутствует в эталонных ценах, пропускаем")
            continue

        ref_prices = market_prices[nmID]

        for size in product.get("sizes", []):
            current_price = size.get("price")
            price_differs = any(abs(current_price - ref_price)
                                > 1 for ref_price in ref_prices)

            if price_differs:
                print(
                    f"nmID={nmID}, размер={size.get('techSizeName')}: цена {current_price} отличается от эталонных {ref_prices}. Нужно обновить.")
                # new_price = min(ref_prices)  # или логика выбора цены
                # discount = size.get("discount", 0)
                # update_price_wildberries(nmID, new_price, discount, Authorization_token)
            else:
                print(
                    f"nmID={nmID}, размер={size.get('techSizeName')}: цена {current_price} соответствует эталонной.")


def main():
    price_comparation(market_price, response)


if __name__ == "__main__":
    main()
