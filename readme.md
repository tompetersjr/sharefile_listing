# Export ShareFile Template Folder Listings

Export a list of ShareFile template folders to a CSV file.

Pull requests are welcome.

## Install

To install run the following:

```
git clone git@github.com:tompetersjr/sharefile_listing.git
cd sharefile_listing
virtualenv -p python3 ~/envs/sharefile_listing
source ~/envs/sharefile_listing/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Sample Usage

```
python3 listing.py -u username -p password -c clientid -s secret -n hostname
```

## Parameters

Parameters | Description
---------- | -----------
-c | ShareFile ClientId *(Required if SHAREFILE_CLIENTID export is missing)*
-h | Show Help
-n | ShareFile Host Name *(Required if SHAREFILE_HOSTNAME export is missing)*
-p | ShareFile Password *(Required if SHAREFILE_PASSWORD export is missing)*
-s | ShareFile Secret Key *(Required if SHAREFILE_SECRET export is missing)*
-u | ShareFile User Name *(Required if SHAREFILE_HOSTNAME export is missing)*

## Exports

If you want to run the command without parameters export the following:

```
export SHAREFILE_HOSTNAME=""
export SHAREFILE_CLIENTID=""
export SHAREFILE_SECRET=""
export SHAREFILE_USERNAME=""
export SHAREFILE_PASSWORD=""
```
