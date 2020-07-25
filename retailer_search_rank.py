import json
import requests

headers = {
    "accept": "application/json",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}

base_url = 'https://www.myntra.com/'


def data_parse(response, site_brand_list):
    data_text = response.text
    json_data_text = json.loads(data_text)
    total_count = json_data_text.get('totalCount')
    products = json_data_text.get('products', '')
    for product in products:
        brand = product.get('brand')
        site_brand_list.append(brand)
    return site_brand_list


def rank_set(search_brand_list, site_brand_list):
    search_brand_list_lower = [x.lower() for x in search_brand_list]
    site_brand_list_lower = [x.lower() for x in site_brand_list]
    rank_dict = {}
    for search_brand in search_brand_list_lower:
        counter = 0
        for site_brand in site_brand_list_lower:
            counter = counter + 1
            if search_brand in site_brand:
                rank_dict[search_brand.capitalize()] = counter
                break
        if search_brand.capitalize() not in rank_dict:
            rank_dict[search_brand.capitalize()] = ''
    return rank_dict


if __name__ == "__main__":
    keyword_items = input('Enter the Keywords seperated by comma: ')
    print('\n')
    keyword_list = keyword_items.split(',')
    # keyword_list = ['Hair Fall Shampoo', 'Conditioner', 'Shampoo']  ##Sample keyword_list
    search_brand_list = ["WOW", "Loreal", "Biotique"]
    output_list = []
    for keyword in keyword_list:
        site_brand_list = []
        keyword = keyword.strip().replace(' ', '-')
        keyword = keyword.lower()
        url = 'https://www.myntra.com/web/v2/search/'+keyword+'?p=1&rows=100&o=0'
        response = requests.get(url, headers=headers)
        if response:
            brand_list = data_parse(response, site_brand_list)
        if site_brand_list:
            rank_dict = rank_set(search_brand_list, brand_list)
            keyword_rank_dict = {'keyword': keyword.replace(
                '-', ' '), 'position': rank_dict}
            output_list.append(keyword_rank_dict)
    output_dict = {'result': output_list}
    print(output_dict, '\n')
