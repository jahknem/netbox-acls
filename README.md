# NetBox Access Lists Plugin

A [Netbox](https://github.com/netbox-community/netbox) plugin for Access List management.

## Features

This plugin provides the following models:

- Access Lists
- Access List to Interface Assignment
- Access List Rules (abstract model bassis for other rules)
- Access List Standard Rules
- Access List Extended Rules

## Origin

Based on the NetBox plugin tutorial by [jeremystretch](https://github.com/jeremystretch):

- [demo repository](https://github.com/netbox-community/netbox-plugin-demo)
- [tutorial](https://github.com/netbox-community/netbox-plugin-tutorial)

All credit should go to Jeremy.  Thanks Jeremy!

This project just looks to build on top of this framework and model presented.

## Compatibility

This plugin was first developed using 3.2.5, and tested with all of 3.2.

| NetBox Version | Plugin Version |
|----------------|----------------|
|       3.2      |      1.0.1     |
|       3.3      |      1.1.0     |

## Installing

For adding to a NetBox Docker setup see
[the general instructions for using netbox-docker with plugins](https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins).

While this is still in development and not yet on pypi you can install with pip:

```bash
pip install git+https://github.com/ryanmerolle/netbox-acls.git@dev
```

or by adding to your `local_requirements.txt` or `plugin_requirements.txt` (netbox-docker):

```bash
git+https://github.com/ryanmerolle/netbox-acls.git@dev
```

Enable the plugin in `/opt/netbox/netbox/netbox/configuration.py`,
 or if you use netbox-docker, your `/configuration/plugins.py` file :

```python
PLUGINS = [
    'netbox_acls'
]

PLUGINS_CONFIG = {
    "netbox_acls": {},
}
```

## Developing

### VSCode + Docker + Dev Containers

To develop this plugin further one can use the included .devcontainer configuration. This configuration creates a docker container which includes a fully working netbox installation. Currently it should work when using WSL 2. For this to work make sure you have Docker Desktop installed and the WSL 2 integrations activated.

1. In the WSL terminal, enter `code` to run Visual studio code.
1. Install the devcontainer extension "ms-vscode-remote.remote-containers"
1. Press Ctrl+Shift+P and use the "Dev Container: Clone Repository in Container Volume" function to clone this repository. This will take a while depending on your computer
1. If you'd like the netbox instance to be prepopulated run `make Makefile example_initializers` and `make Makefile load_initializers`
1. Start the netbox instance using `make Makefile all`

Your netbox instance will be served under 0.0.0.0:8000 so it should now be available under localhost:8000.

## Screenshots

Access List - List View
![Access List - List View](docs/img/access_lists.png)

Access List (Type Extended) - Individual View
![Access List Type Extended - Individual View](docs/img/access_list_type_extended.png)

Access List (Type Standard) - Individual View
![Access List Type Standard - Individual View](docs/img/access_list_type_standard.png)

Extended Access List Rules - List View
![Extended Access List Rules - List View](docs/img/acl_extended_rules.png)

Standard Access List Rules - List View
![Standard Access List Rules - List View](docs/img/acl_standard_rules.png)

Access List Interface Assignments- List View
![Access List Interface Assignments- List View](docs/img/acl_interface_assignments.png)

Host (device, virtual_chassis, virtual_machine) Access Lists - New Card
![Host Access Lists - New Card](docs/img/acl_host_view.png)

Host Interface (vminterface interface) Access Lists - New Card
![Host Interface Access Lists - New Card](docs/img/access_list_type_standard.png)
