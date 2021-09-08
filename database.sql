# 2021.09.08 部署测试环境

## superset所用的数据库
CREATE DATABASE superset CHARACTER SET utf8 COLLATE utf8_general_ci;

## 其它基础数据数据库
CREATE DATABASE lab_data CHARACTER SET utf8 COLLATE utf8_general_ci;


create table lab_course.ai_model_params
(
	id int(32) auto_increment
		primary key,
	name varchar(255) null,
	config varchar(500) not null comment '切片ID',
	checkpoint mediumblob not null comment '模型参数',
	create_time timestamp default CURRENT_TIMESTAMP not null comment '创建时间',
	update_time timestamp default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP comment '修改时间',
	is_delete tinyint default 0 null comment '是否已删除 0-未删 1-已删',
	uuid binary(16) null,
	created_by_fk int null,
	changed_by_fk int null,
	created_on datetime null,
	changed_on datetime null
)
comment '模型存储表';