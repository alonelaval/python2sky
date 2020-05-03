# -*- coding:utf-8 -*-
# author：huawei


# ENTRY = 0
# EXIT = 1
# LOCAL = 2
#
# CROSS_PROCESS = 0
# CROSS_THREAD = 1
#
# UNKNOWN = 0
# DATABASE = 1
# RPCFRAMEWORK = 2
# HTTP = 3
# MQ = 4
# CACHE = 5

COMPONENT_ID_2_NAME = {"0": "N/A", "1": "Tomcat", "2": "HttpClient", "3": "Dubbo", "4": "H2", "5": "Mysql",
                       "6": "ORACLE",
                       "7": "Redis", "8": "Motan", "9": "MongoDB", "10": "Resin", "11": "Feign", "12": "OKHttp",
                       "13": "SpringRestTemplate", "14": "SpringMVC", "15": "Struts2", "16": "NutzMVC",
                       "17": "NutzHttp",
                       "18": "JettyClient", "19": "JettyServer", "20": "Memcached", "21": "ShardingJDBC",
                       "22": "PostgreSQL", "23": "GRPC", "24": "ElasticJob", "25": "RocketMQ", "26": "httpasyncclient",
                       "27": "Kafka", "28": "ServiceComb", "29": "Hystrix", "30": "Jedis", "31": "SQLite",
                       "32": "h2-jdbc-driver", "33": "mysql-connector-java", "34": "ojdbc", "35": "Spymemcached",
                       "36": "Xmemcached", "37": "postgresql-jdbc-driver", "38": "rocketMQ-producer",
                       "39": "rocketMQ-consumer", "40": "kafka-producer", "41": "kafka-consumer",
                       "42": "mongodb-driver",
                       "43": "SOFARPC", "44": "ActiveMQ", "45": "activemq-producer", "46": "activemq-consumer",
                       "47": "Elasticsearch", "48": "transport-client", "49": "http", "50": "rpc", "51": "RabbitMQ",
                       "52": "rabbitmq-producer", "53": "rabbitmq-consumer", "54": "Canal", "55": "Gson",
                       "56": "Redisson",
                       "57": "Lettuce", "58": "Zookeeper", "59": "Vertx", "60": "ShardingSphere",
                       "61": "spring-cloud-gateway", "62": "RESTEasy", "63": "SolrJ", "64": "Solr", "65": "SpringAsync",
                       "66": "JdkHttp", "67": "spring-webflux", "68": "Play", "69": "cassandra-java-driver",
                       "70": "Cassandra", "71": "Light4J", "72": "Pulsar", "73": "pulsar-producer",
                       "74": "pulsar-consumer", "75": "Ehcache", "76": "SocketIO", "77": "rest-high-level-client",
                       "78": "spring-tx", "79": "Armeria", "80": "JdkThreading", "5001": "ServiceCombMesher",
                       "5002": "ServiceCombServiceCenter", "4001": "HttpServer", "4002": "express", "4003": "Egg",
                       "4004": "Koa", "3001": "AspNetCore", "3002": "EntityFrameworkCore", "3003": "SqlClient",
                       "3004": "CAP", "3005": "StackExchange.Redis", "3006": "SqlServer", "3007": "Npgsql",
                       "3008": "MySqlConnector", "3009": "EntityFrameworkCore.InMemory",
                       "3010": "EntityFrameworkCore.SqlServer", "3011": "EntityFrameworkCore.Sqlite",
                       "3012": "Pomelo.EntityFrameworkCore.MySql", "3013": "Npgsql.EntityFrameworkCore.PostgreSQL",
                       "3014": "InMemoryDatabase", "3015": "AspNet", "3016": "SmartSql"}
