# ts-v2-catalog-backport

Conversion of d43-catalog's ts_v2_catalog_handler lambda function in to Python 3 &amp; Docker

## To Run:

### Development:

`docker run -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_DEFAULT_REGION=us-west-2 PREFIX='dev-' unfoldingword/ts_v2_catalog_backport:develop`


#### Production:

`docker run -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_DEFAULT_REGION=us-west-2 PREFIX='' unfoldingword/ts_v2_catalog_backport:master`
