#!/usr/bin/env bash

echo $ZOO_NODE > /opt/zookeeper/data/myid && \
/opt/zookeeper/bin/zkServer.sh start /opt/zookeeper/data/zoo.cfg && \
/opt/solr/bin/solr -c -force -f