"""Bilibili Scraper: run it from Python and save the results to a CSV file.

Store page: https://apify.com/pipiagent/bilibili-scraper
Setup: pip install apify-client
       set APIFY_TOKEN to your API token from https://console.apify.com/settings/integrations
Run:   python example.py [input.json]
"""
import json
import os
import sys

from apify_client import ApifyClient

ACTOR = 'pipiagent/bilibili-scraper'


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.json')
    with open(path, encoding='utf-8') as f:
        run_input = json.load(f)
    client = ApifyClient(os.environ['APIFY_TOKEN'])
    print(f'Running {ACTOR} ...')
    run = client.actor(ACTOR).call(run_input=run_input)
    dataset = client.dataset(run.default_dataset_id)
    items = list(dataset.iterate_items())
    print(f'{len(items)} results, status {run.status}')
    if items:
        print(json.dumps(items[0], indent=2, ensure_ascii=False)[:1500])
    # The BOM lets Excel open the file with the right encoding.
    with open('bilibili-scraper.csv', 'wb') as f:
        f.write(dataset.get_items_as_bytes(item_format='csv', clean=True, bom=True))
    print('Saved bilibili-scraper.csv')


if __name__ == '__main__':
    main()
