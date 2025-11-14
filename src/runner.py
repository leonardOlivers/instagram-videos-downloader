thonpython
import json
import logging
from pathlib import Path
from extractors.instagram_parser import InstagramParser
from outputs.exporters import Exporter

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")

def load_input_urls(file_path: str):
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Instagram Videos Downloader")
    parser.add_argument("--input", required=True, help="Path to input text file with URLs")
    parser.add_argument("--output", required=True, help="Path to output JSON file")
    args = parser.parse_args()

    urls = load_input_urls(args.input)
    logging.info(f"Loaded {len(urls)} URLs")

    parser = InstagramParser()
    results = []

    for url in urls:
        logging.info(f"Processing {url}")
        data = parser.extract(url)
        results.append(data)

    Exporter.save_json(results, args.output)
    logging.info(f"Saved output to {args.output}")

if __name__ == "__main__":
    main()