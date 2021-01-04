FROM openjdk:8-jdk-slim-stretch

ENV SOLR_VERSION="8.0.0" \
    SOLR_DOWNLOAD_SERVER="https://archive.apache.org/dist/lucene/solr" \
    ZOO_VERSION="3.4.14" \
    ZOO_DOWNLOAD_SERVER="https://archive.apache.org/dist/zookeeper"

RUN apt-get update && \
    apt-get install -y procps lsof less wget


# download Zookeeper
RUN mkdir -p /tmp/zookeeper && \
    cd /tmp/zookeeper && \
    echo "downloading zookeeper-$ZOO_VERSION.tgz ..." && \
    wget -nv $ZOO_DOWNLOAD_SERVER/zookeeper-$ZOO_VERSION/zookeeper-$ZOO_VERSION.tar.gz


# install Zookeeper
RUN mkdir -p /opt/zookeeper/data
RUN cd /tmp/zookeeper && \
    echo "installing zookeeper ..." && \
    tar -zxvf zookeeper-$ZOO_VERSION.tar.gz -C /opt/zookeeper --strip-components=1

COPY ./conf/zookeeper-env.sh /opt/zookeeper/conf/
COPY ./conf/zoo.cfg /opt/zookeeper/data/


# download Solr
RUN mkdir -p /tmp/solr && \
    cd /tmp/solr && \
    echo "downloading solr-$SOLR_VERSION.tgz ..." && \
    wget -nv $SOLR_DOWNLOAD_SERVER/$SOLR_VERSION/solr-$SOLR_VERSION.tgz

# install Solr
RUN mkdir -p /opt/solr/data
RUN cd /tmp/solr && \
    echo "installing solr ..." && \
    tar -zxvf solr-$SOLR_VERSION.tgz -C /opt/solr --strip-components=1

COPY ./conf/solr.in.sh /opt/solr/bin/solr.in.sh
COPY ./conf/solr.xml /opt/solr/data/
COPY ./conf/log4j2.xml /opt/solr/server/resources/log4j2.xml

#cleanup
RUN rm -r /tmp/solr /tmp/zookeeper

EXPOSE 8983
EXPOSE 2181


COPY ./start.sh /opt/
CMD ["/opt/start.sh"]