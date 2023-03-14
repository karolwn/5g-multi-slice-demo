
# 5G multi-slice demo
 Part of master thesis, AGH University of Sicience and Technology 2023
 Based on [free5gc](https://github.com/free5gc/free5gc-compose) and [UERANSIM](https://github.com/aligungr/UERANSIM)
## How to run
1. install docker [Ubuntu tutorial](https://docs.docker.com/engine/install/ubuntu/)
2. install [GTP5G kernel module](https://github.com/free5gc/gtp5g)
3. prepare docker images
```bash
# Clone this repo
git clone https://github.com/karolwn/5g-multi-slice-demo.git
cd 5g-multi-slice-demo

# Build the images
sudo make all
sudo docker compose -f docker-compose-build.yaml build
```
4. run test environment
```bash
sudo ./run_network start
# flags:
# 	* start
# 	* stop
#	* status
# 	* delete - remove containers
# logs are saved in app.log
# alternatively, one can use sudo docker compose up
```
5. web console: http://127.0.0.1:5000, user:pass = admin:free5gc
6. simple http server: http://127.0.0.1:8080

## About
free5gc + UERANSIM: 
* 1 x gNodeB
* 3 x UE
* 1 x each NF
* 1 x simple python + flask http server

## Useful links
* https://www.free5gc.org
* https://docs.docker.com/compose/networking/
* https://docs.docker.com/compose/gettingstarted/
* https://github.com/emmericp/MoonGen
* https://nickvsnetworking.com/my-first-5g-core-open5gs-and-ueransim/
