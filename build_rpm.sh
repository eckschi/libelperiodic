#!/bin/bash
TOPDIR=`pwd`/package

mkdir -p ${TOPDIR}/{BUILD,BUILDROOT,RPMS,SPECS,SRPMS,SOURCES}
tar --exclude=package \
    --exclude=build_rpm.sh \
    -cjf ${TOPDIR}/SOURCES/elperiodic.tar.bz2  *  --transform 's,^,elperiodic/,S'

rpmbuild --define "_topdir $TOPDIR" -bb elperiodic.spec

