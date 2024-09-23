VERSION=$(shell cat version)
ARTIFACT=telecripto
REPO=rodrigorootrj/service
TAG=${REPO}:${ARTIFACT}-${VERSION}
LABEL=work-py
DIR=$(shell pwd -P)

echo:
	@echo ${TAG}
	@echo ${LABEL}
	@echo ${DIR}
build:
	@docker build . -t ${TAG}
push:
run:
shell:
	@docker run -it --rm --name ${LABEL} --mount type=bind,source=${DIR}/src,target=/app/ -e TELECRIPTO_TELEGRAM_TOKEN=$$TELECRIPTO_TELEGRAM_TOKEN -e TELECRIPTO_TELEGRAM_GROUP=$$TELECRIPTO_TELEGRAM_GROUP --entrypoint /bin/bash ${TAG}
## deploy	
compose:
	@docker compose up -d
compose_down:
	@docker compose down
app:
	@docker-compose exec app bash	
##
fiat:
	@mv etcd/ src/ && mv lib src/ && mv __init__.py src/ && mv main.py src/
	@mv doc/asset/Dockerfile . && mv doc/asset/docker-compose.yaml . && mv doc/version .