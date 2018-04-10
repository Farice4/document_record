### Barbican
####项目介绍:
Barbican是云应用程序的RESTful密钥管理器服务服务。
Barbican包含一个REST API（称为Barbican），用于秘密的安全存储，供应和管理。 API可以与安全设备（如HSM）进行交互。
Barbican对秘密的管理包括: 秘钥，证书，秘密，二进制数据

项目从H版本开始发起，最初由Rackspace提交比较多，

####目前支持:
支持秘钥，证书，秘密，二进制数据
典型应用场景:
cinder 创建加密卷，instance使用

url:
https://blog.csdn.net/u010774286/article/details/50384786
https://vakwetu.wordpress.com/2015/11/30/barbican-and-volume-encryption/
https://vakwetu.fedorapeople.org/encrypted_volumes.webm
####项目情况:
commit:2983
releases: 82
发布版本: Liberty(发布1.0版本)

### Blazar
项目介绍：
Blazar是OpenStack的资源预订服务。Blazar允许用户在特定的时间段内预订特定类型/数量的资源，并根据他们的预订将这些资源租给用户。

目前支持以下两种资源类型:
计算主机:与整个主机的一个单元保留和租赁。
实例:用一种黄酮的单位储备和租赁。

####项目情况:
commit:661
releases:8
发布版本: queens（发布1.0版本)

### Cloudkitty
####项目介绍
Cloudkitty 是OpenStack的计费项目。通过创建计费规则，将收集到的数据与计费规则结合，统计出计费账单，实现资源计费。

####数据来源:
fake
meta
gnocchi: ceilometer数据采集统计与api提供服务
monasca：监控服务
####计费引擎Rating
noop: 模型为空，仅供测试
hashmap: 最实用，最接近实际计费的模式
pyscripts：提供了使用python代码定制计费的接口，用户可以直接将含有计费逻辑的python脚本上传给cloudkitty实现定制化的计费模型

####项目情况
commit:659
releases:14
发布版本: mitaka(发布0.5.0-0.5.3)


### Congress
####项目介绍

Congress是一个OpenStack项目，旨在通过任何云服务集合提供政策即服务，以便为动态基础架构提供治理和合规性


####项目情况
commit:2446
releases:52
发布版本:Liberty(发布版本2.0)

### Cyborg 
####项目介绍
Cyborg（以前称为Nomad）是一个OpenStack项目，旨在为加速资源（即Crypto卡，GPU，FPGA，NVMe / NOF SSD，ODP，DPDK / SPDK等各种类型的加速器提供通用管理框架上）

####项目情况


### Designate
####项目介绍
Designate是OpenStack的DNSaaS（DNS即服务）的功能，其目标就是要赋予OpenStack提供这种云域名系统的能力，云服务商可以使用Designate就能够很容易建造一个云域名管理系统来托管租户的公有域名。

####实现方式
Designate是一套dns调用管理软件，通过调用底层bind（及其它底层dns)服务, 完成dns相关管理工作

####使用场景
- neutron 与designate结合，配置neutron external_dns_driver = designate驱动
- openstack创建一个zone(openstack zone create --email my@test.com test.org.)
- neutron 创建忘了，指定domian(neutron net-create dns-net --dns-domain test.org.)
- neutron 创建子网(neutron subnet-create --name dns-subnet dns-net 192.168.1.0/24)
- nova 创建虚拟机(nova boot --image cirros-0.3.5-x86_64-disk --flavor 1 --nic net-name=dns-net vm5)
- 为虚拟机绑定floating ip
- Designate 查看会包含zone的记录，与虚拟机解析记录

####项目情况
commit: 3728
releases: 63
发布版本: Liberty(发布版本1.0.0)

### Dragonflow
#### 项目介绍
Dragonflow是OpenStack®Neutron™的分布式SDN控制器，支持分布式交换，路由，DHCP等。
Dragonflow旨在支持大规模部署，重点关注延迟和性能，并提供可在各个计算节点上本地运行的高级创新服务，并考虑容器技术.

Dragonflow提供以下虚拟网络服务：

第2层（交换）

替换传统的Open vSwitch（OVS）代理。

第3层（路由）

本地实现支持分布式路由。在支持分布式DNAT的过程中。 SNAT集中在网络节点。

DHCP

在每个计算节点本地提供/ DHCP服务的分布式DHCP应用程序。

元数据

分布式元数据代理应用程序在每个计算节点本地运行。

DPDK

Dragonflow将支持使用OVS DPDK作为数据路径备选，这取决于OVS DPDK中支持的功能以及Neutron插件支持的VIF绑定脚本

####项目情况
commit: 3259
releases: 7
发布版本: 没有找到发版记录，在stackalytics上有看到从Liberty开始提交

### Freezer
#### 项目介绍

Freezer是OpenStack的分布式备份还原和灾难恢复。它旨在成为多操作系统（Linux，Windows，OSX，* BSD），专注于为基于块的备份，基于文件的增量备份，时间点操作，作业同步（即通过多个节点进行备份同步）提供效率和灵活性）和许多其他功能
