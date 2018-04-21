url=192.168.0.248
url=battlefield1408.tk
while true; do
  curl ${url}:5000/all_lights/on
  curl ${url}:5000/all_lights/off
  sleep 2.5
done
