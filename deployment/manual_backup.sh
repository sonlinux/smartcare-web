#!/bin/bash
MYDATE=`date +%d-%B-%Y`
MONTH=$(date +%B)
YEAR=$(date +%Y)
cd /home/data/changelog.inasafe.org/deployment
MYBASEDIR=`pwd`/backups
MYBACKUPDIR=${MYBASEDIR}/${YEAR}/${MONTH}
mkdir -p ${MYBACKUPDIR}

cd ${MYBACKUPDIR}
docker exec -ti smartcare-client-db /bin/bash -c "PGPASSWORD=docker pg_dump -Fc -f /tmp/latest.dmp -h localhost -U docker gis"
docker cp smartcare-client-db:/tmp/latest.dmp PG_smartcare-client-${MYDATE}.dmp

cd -
rm backups/latest.dmp

cd backups
ln -s ${MYBACKUPDIR}/PG_smartcare-client-${MYDATE}.dmp latest.dmp

cd ..
