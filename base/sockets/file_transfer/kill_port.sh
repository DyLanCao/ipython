port=21567

lsof -i:$port | awk '{if (NR>1){print $2}}' | xargs kill -9

