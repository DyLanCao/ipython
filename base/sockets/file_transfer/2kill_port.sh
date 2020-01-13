port=8080
lsof -t -i tcp:$port | xargs kill -9
