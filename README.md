# traefik-boostrap



## Rootless setup

```bash
sudo setcap cap_net_bind_service=ep $(which rootlesskit)
systemctl --user restart docker
```
