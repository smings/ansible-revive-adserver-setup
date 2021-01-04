#!/usr/bin/env python3

dev = {"app-servers": ["lmwr-application01.test-server.ag"],
       "app-rsync-module": "content",
       "file-servers": ["lmwr-edge01.test-server.ag"],
       "fileserver-rsync-module": "files",
       # used for auth against app-servers and file-servers
       "user": "webapp",
       "solr-indexer":
              {"server": "lmwr-search01.test-server.ag",
               "content-module": "content",
               "content-endpoint": "http://lmwr-search01.test-server.ag:8080/firstSpiritContent",
               "datasources-module": "datasources",
               "datasources-endpoint": "http://lmwr-search01.test-server.ag:8080/firstSpiritDatasources",
               "user": "webapp"},
        "consul-server": "http://lmwr-search01.test-server.ag:8500"}

environments = {"dev": dev}