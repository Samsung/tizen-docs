#!/bin/bash -x

usage="$(basename "$0") [-h] [profile] [version] -- genernate TOC.md per profile and version.

	-h			show ehlp text
	[profile]	Tizen profile name, e.g. mobile, wearable, or tv.
	[version]	Tizen platform version, e.g. 3.0, 4.0, or etc."

PROFILE=$1
PRO_SHORT=""
PRO_LONG=""
PRO_DEL1=""
PRO_DEL2=""

if [ -z "$2" ]
then
	VERSION="4.0"
else
	VERSION="$2"
fi

if [ "$1" = "-h" ]
then
	echo "$usage"
	exit 0;
else
	if [ "$PROFILE" = "tv" ]
	then
		PRO_SHORT="_tv"
		PRO_LONG="TV"
		FILE_NAME="web_api_toc_tv_$VERSION.txt"
	else
		if [ "$PROFILE" = "wearable" ]
		then
			PRO_SHORT="_w"
			PRO_LONG="Wearable"
			PRO_DEL1="Mobile_UIComponents"
		else
			PROFILE="mobile"
			PRO_SHORT="_m"
			PRO_LONG="mobile"
			PRO_DEL1="Wearable_UIComponents"
			PRO_DEL2="wearable_widget"
		fi
		FILE_NAME="web_api_toc_$VERSION.txt"
	fi
fi

BASE_PATH="\/application\/web\/api\/$PROFILE\/$VERSION"

OPT="-e s/BASE_PATH/$BASE_PATH/g -e s/_PROFILE.html/$PRO_SHORT.html/g -e s/\/PROFILE\//\/$PROFILE\//g $FILE_NAME"
sed $OPT >&web_api_toc.md

if [ -n "$PRO_DEL1" ]
then
	OPT="!/$PRO_DEL1/ web_api_toc.md"
	awk $OPT > .web_api_toc.md
	mv .web_api_toc.md web_api_toc.md
fi

if [ -n "$PRO_DEL2" ]
then
	OPT="!/$PRO_DEL2/ web_api_toc.md"
	awk $OPT > .web_api_toc.md
	mv .web_api_toc.md web_api_toc.md
fi

mv web_api_toc.md ../$PROFILE/$VERSION/TOC.md
