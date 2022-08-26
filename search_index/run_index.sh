docker run -it --env-file=.env -e "CONFIG=$(cat index_config.json | jq -r tostring)" algolia/docsearch-scraper
