import requests

def search_japanese_word(word):
    search_result = api_search_word(word)  # Replace with your Japanese word of interest

    if search_result:
        # Print basic information about the word

            first_entry = search_result["data"][0]  # Get the first entry from the data
            japanese_word = first_entry["japanese"][0]["word"]
            print(f"Japanese Word : {japanese_word}")
            # Print English meanings
            meanings = first_entry["senses"][0]["english_definitions"]
            print("English Meanings:")
            for idx, meaning in enumerate(meanings, start=1):
                print(f"{idx}. {meaning}")

            print("----------------------")

    else:
        print("No data fetched from Jisho API.")


def api_search_word(word):
    url = f"https://jisho.org/api/v1/search/words?keyword={word}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Process the JSON response as needed
        return data
    else:
        print(f"Failed to fetch data from Jisho API: {response.status_code}")
        return None