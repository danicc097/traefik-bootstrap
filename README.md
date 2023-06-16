# traefik-boostrap

Edit ``dynamic_conf.yaml.example`` and append your own service certificates as
required. Then `./mkcert-certificates` followed by `./compose-up`

## Rootless setup

```bash
sudo setcap cap_net_bind_service=ep $(which rootlesskit)
systemctl --user restart docker
```
