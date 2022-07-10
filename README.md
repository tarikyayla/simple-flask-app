# Installation

## _This is a development version. Both client and api runs in different ports. To have a release, you have to add an endpoint renders client build._
<br>

## Server runs on localhost:5000


## Client runs on localhost:3000 
<br> 

![ui](https://user-images.githubusercontent.com/29834197/178162305-5c8d2202-54b7-43e6-9bc3-547f60ada057.jpg)

![image](https://user-images.githubusercontent.com/29834197/178162344-5eb18d39-5502-4273-9024-62e42ede2c6a.png )


<br>

```
docker-compose up -d # should run db with seed data and services.
```

# API

```json
[
  {
    "name": "GET Locations",
    "request": {
      "method": "GET",
      "header": [],
      "url": {
        "raw": "http://localhost:5000/api/locations/?page=1&items-per-page=2",
        "protocol": "http",
        "host": ["localhost"],
        "port": "5000",
        "path": ["api", "locations", ""],
        "query": [
          {
            "key": "page",
            "value": "1"
          },
          {
            "key": "items-per-page",
            "value": "2"
          }
        ]
      }
    },
    "response": [
      {
        "city": "Budapest",
        "country": "Hungary",
        "country_code": "HU",
        "id": 1
      },
      {
        "city": "Yiliu",
        "country": "China",
        "country_code": "CN",
        "id": 2
      }
    ]
  },
  {
    "name": "GET Location",
    "request": {
      "method": "GET",
      "header": [],
      "url": {
        "raw": "http://localhost:5000/api/locations/3",
        "protocol": "http",
        "host": ["localhost"],
        "port": "5000",
        "path": ["api", "locations", "3"]
      }
    },
    "response": {
      "city": "El Real",
      "country": "Venezuela",
      "country_code": "VE",
      "id": 3
    }
  },
  {
    "name": "GET Switches",
    "request": {
      "method": "GET",
      "header": [],
      "url": {
        "raw": "http://localhost:5000/api/locations/2/switches?page=1&items-per-page=10",
        "protocol": "http",
        "host": ["localhost"],
        "port": "5000",
        "path": ["api", "locations", "2", "switches"],
        "query": [
          {
            "key": "page",
            "value": "1"
          },
          {
            "key": "items-per-page",
            "value": "10"
          }
        ]
      }
    },
    "response": [
      {
        "alias": "dnajafiang",
        "id": 17,
        "location": 2,
        "port_count": 123
      },
      {
        "alias": "ggranham5b",
        "id": 192,
        "location": 2,
        "port_count": 90
      }
    ]
  },
  {
    "name": "GET Switch",
    "request": {
      "method": "GET",
      "header": [],
      "url": {
        "raw": "http://localhost:5000/api/switches/4",
        "protocol": "http",
        "host": ["localhost"],
        "port": "5000",
        "path": ["api", "switches", "4"]
      }
    },
    "response": {
      "alias": "pgreenless3",
      "id": 4,
      "location": {
        "city": "Zhougang",
        "country": "China",
        "country_code": "CN",
        "id": 140
      },
      "port_count": 42
    }
  },
  {
    "name": "GET Ports",
    "request": {
      "method": "GET",
      "header": [],
      "url": {
        "raw": "http://localhost:5000/api/switches/2/ports?page=1&items-per-page=10",
        "protocol": "http",
        "host": ["localhost"],
        "port": "5000",
        "path": ["api", "switches", "2", "ports"],
        "query": [
          {
            "key": "page",
            "value": "1"
          },
          {
            "key": "items-per-page",
            "value": "10"
          }
        ]
      }
    },
    "response": [
      {
        "creation_time": "Sun, 10 Jul 2022 19:45:49 GMT",
        "id": 105,
        "interface_name": "tcluckie2w",
        "ipv6": "527b:2f32:3521:41a9:5c44:b6f1:fe06:9460/81",
        "port": 17,
        "switch": 2
      },
      {
        "creation_time": "Sun, 10 Jul 2022 19:45:51 GMT",
        "id": 315,
        "interface_name": "efredi8q",
        "ipv6": "22ce:93d8:bc2a:8923:d7ce:e673:b9e5:a238/93",
        "port": 28,
        "switch": 2
      },
      {
        "creation_time": "Sun, 10 Jul 2022 19:45:51 GMT",
        "id": 323,
        "interface_name": "hyitzhakof8y",
        "ipv6": "4557:f751:b6a6:ee6a:cf97:80e6:8784:6fcc/29",
        "port": 110,
        "switch": 2
      },
      {
        "creation_time": "Sun, 10 Jul 2022 19:45:53 GMT",
        "id": 565,
        "interface_name": "wmaylottfo",
        "ipv6": "ffa3:b961:b29:5c7e:a90:f3a0:6681:2f9a/33",
        "port": 44,
        "switch": 2
      },
      {
        "creation_time": "Sun, 10 Jul 2022 19:45:55 GMT",
        "id": 800,
        "interface_name": "qstopfordm7",
        "ipv6": "cf0f:8c62:3709:b272:d910:6f2d:a689:ac0a/92",
        "port": 37,
        "switch": 2
      }
    ]
  }
]
```
