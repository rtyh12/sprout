# 🌱

## Don't forget to water your plants!

Build by running ```docker build . -t sprout```, then launch the container with ```docker run -d --restart always sprout```.

The Raspberry Pi this app is currently running on is set up to restart daily:

```
sudo su -
crontab -e
[add this line:] 0 3 * * * /sbin/shutdown -r now
```