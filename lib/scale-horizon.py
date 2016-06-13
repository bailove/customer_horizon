import horizon

project = horizon.get_dashboard('project')
project.default_panel = "instances"
overview = project.get_panel('overview')
project.unregister(overview.__class__)

images_panel = project.get_panel('images')
project.unregister(images_panel.__class__)

volumes_panel = project.get_panel('volumes')
project.unregister(volumes_panel.__class__)

accessandsecurity_panel = project.get_panel('access_and_security')
project.unregister(accessandsecurity_panel.__class__)

networks_panel = project.get_panel('networks')
project.unregister(networks_panel.__class__)

network_topology_panel = project.get_panel('network_topology')
project.unregister(network_topology_panel.__class__)

routers_panel = project.get_panel('routers')
project.unregister(routers_panel.__class__)

# remove the 'change password panel'
settings_dashboard = horizon.get_dashboard("settings")
password_panel = settings_dashboard.get_panel("password")
settings_dashboard.unregister(password_panel.__class__)
