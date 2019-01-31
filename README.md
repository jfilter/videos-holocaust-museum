# Videos Holocaust Museum

Scrape videos from the [United States Holocaust Memorial Museum](https://www.ushmm.org/).

## Requirements

- [pipenv](https://en.wikipedia.org/wiki/Wget)
- [wget](https://en.wikipedia.org/wiki/Wget)
- a modern Python version

## Install

```bash
git clone https://github.com/jfilter/videos-holocaust-museum && cd videos-holocaust-museum && pipenv install
```

## Usage

```bash
pipenv run python get.py && wget -i urls.txt -P videos
```

## License

MIT.
