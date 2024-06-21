import requests


def search_japanese_word(word):
    search_result = api_search_word(word)

    if search_result:
            first_entry = search_result["data"][0]

            japanese_word = first_entry["japanese"][0]["word"]

            meanings = first_entry["senses"][0]["english_definitions"]

            clean_meanings = ', '.join(meanings)
            complete_text = f'{japanese_word}\n\n{clean_meanings}'
            return complete_text
    else:
        print("No data fetched from Jisho API.")


def api_search_word(word):
    url = f"https://jisho.org/api/v1/search/words?keyword={word}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data from Jisho API: {response.status_code}")
        return None
