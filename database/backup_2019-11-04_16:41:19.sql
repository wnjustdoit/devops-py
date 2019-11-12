--
-- PostgreSQL database dump
--

-- Dumped from database version 11.5
-- Dumped by pg_dump version 11.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: wangnan
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO wangnan;

--
-- Name: git_repo; Type: TABLE; Schema: public; Owner: wangnan
--

CREATE TABLE public.git_repo (
    id integer NOT NULL,
    description character varying(128),
    ssh_url_to_repo character varying(128) NOT NULL,
    http_url_to_repo character varying(128) NOT NULL,
    web_url character varying(128) NOT NULL,
    name character varying(64) NOT NULL,
    name_with_namespace character varying(64) NOT NULL,
    path character varying(64) NOT NULL,
    path_with_namespace character varying(64) NOT NULL,
    created_at date,
    updated_at date,
    created_by character varying(32),
    updated_by character varying(32)
);


ALTER TABLE public.git_repo OWNER TO wangnan;

--
-- Name: TABLE git_repo; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON TABLE public.git_repo IS 'git仓库信息';


--
-- Name: COLUMN git_repo.id; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.git_repo.id IS '仓库id';


--
-- Name: COLUMN git_repo.description; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.git_repo.description IS '仓库描述';


--
-- Name: COLUMN git_repo.ssh_url_to_repo; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.git_repo.ssh_url_to_repo IS 'ssh仓库地址';


--
-- Name: COLUMN git_repo.http_url_to_repo; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.git_repo.http_url_to_repo IS 'http仓库地址';


--
-- Name: COLUMN git_repo.web_url; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.git_repo.web_url IS 'web访问链接';


--
-- Name: COLUMN git_repo.name; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.git_repo.name IS '项目名称';


--
-- Name: COLUMN git_repo.name_with_namespace; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.git_repo.name_with_namespace IS '带命名空间的项目名称';


--
-- Name: COLUMN git_repo.path; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.git_repo.path IS '项目路径';


--
-- Name: COLUMN git_repo.path_with_namespace; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.git_repo.path_with_namespace IS '带命名空间的项目路径';


--
-- Name: git_repo_id_seq; Type: SEQUENCE; Schema: public; Owner: wangnan
--

ALTER TABLE public.git_repo ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.git_repo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: publishment; Type: TABLE; Schema: public; Owner: wangnan
--

CREATE TABLE public.publishment (
    id integer NOT NULL,
    git_repo_id integer NOT NULL,
    git_branches character varying(32) NOT NULL,
    profile character varying(8) NOT NULL,
    to_username character varying(16) NOT NULL,
    to_ip character varying(64) NOT NULL,
    to_project_home character varying(64) NOT NULL,
    to_process_name character varying(32) NOT NULL,
    to_java_opts character varying(128),
    git_merged_branch character varying(16),
    git_tag_version character varying(16),
    git_tag_comment character varying(32),
    git_delete_temp_branch smallint DEFAULT 0,
    name character varying(64) NOT NULL,
    description character varying(64) NOT NULL,
    created_at date,
    updated_at date,
    created_by character varying(32),
    updated_by character varying(32)
);


ALTER TABLE public.publishment OWNER TO wangnan;

--
-- Name: TABLE publishment; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON TABLE public.publishment IS '发布系统信息';


--
-- Name: COLUMN publishment.id; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.id IS '主键id，自增';


--
-- Name: COLUMN publishment.git_repo_id; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.git_repo_id IS 'git仓库id，与表git_repo外键隐式关联';


--
-- Name: COLUMN publishment.git_branches; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.git_branches IS 'git分支，多个用,分隔';


--
-- Name: COLUMN publishment.profile; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.profile IS '发布环境，通常为：dev/pre/online';


--
-- Name: COLUMN publishment.to_username; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.to_username IS '目标服务器用户名';


--
-- Name: COLUMN publishment.to_ip; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.to_ip IS '目标服务器ip地址，多个以,分隔';


--
-- Name: COLUMN publishment.to_project_home; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.to_project_home IS '目标服务器上项目主目录';


--
-- Name: COLUMN publishment.to_process_name; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.to_process_name IS '目标服务器上项目进程名称关键字（用于ps检索并杀死进程）';


--
-- Name: COLUMN publishment.to_java_opts; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.to_java_opts IS '目标服务器上java应用的命令行变量';


--
-- Name: COLUMN publishment.git_merged_branch; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.git_merged_branch IS '发布完毕后git合并到的分支';


--
-- Name: COLUMN publishment.git_tag_version; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.git_tag_version IS '发布完毕后git打的标签名';


--
-- Name: COLUMN publishment.git_tag_comment; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.git_tag_comment IS '发布完毕后git打的标签注释';


--
-- Name: COLUMN publishment.git_delete_temp_branch; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.git_delete_temp_branch IS '发布完毕后git是否删除临时分支（仅在多分支发布时）';


--
-- Name: COLUMN publishment.name; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.name IS '发布名称';


--
-- Name: COLUMN publishment.description; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.description IS '发布描述';


--
-- Name: publishment_id_seq; Type: SEQUENCE; Schema: public; Owner: wangnan
--

ALTER TABLE public.publishment ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.publishment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: wangnan
--

INSERT INTO public.alembic_version VALUES ('8533c206fb80');


--
-- Data for Name: git_repo; Type: TABLE DATA; Schema: public; Owner: wangnan
--

INSERT INTO public.git_repo VALUES (318, '妈妈优选/妈妈纷享后台CMS系统（含schedule定时调度系统）', 'git@192.168.1.248:mall/youxuan-cms.git', 'http://192.168.1.248:8080/mall/youxuan-cms.git', 'http://192.168.1.248:8080/mall/youxuan-cms', 'youxuan-cms', 'mall / youxuan-cms', 'youxuan-cms', 'mall/youxuan-cms', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (317, '妈妈优选/妈妈纷享对外系统（买家端、卖家端）', 'git@192.168.1.248:mall/youxuan.git', 'http://192.168.1.248:8080/mall/youxuan.git', 'http://192.168.1.248:8080/mall/youxuan', 'youxuan', 'mall / youxuan', 'youxuan', 'mall/youxuan', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (310, '应用监控平台', 'git@192.168.1.248:mall/spring-boot-actuator-universal.git', 'http://192.168.1.248:8080/mall/spring-boot-actuator-universal.git', 'http://192.168.1.248:8080/mall/spring-boot-actuator-universal', 'spring-boot-actuator-universal', 'mall / spring-boot-actuator-universal', 'spring-boot-actuator-universal', 'mall/spring-boot-actuator-universal', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (309, '进货商城、ERP与金蝶数据交换项目', 'git@192.168.1.248:mall/schedule-kd.git', 'http://192.168.1.248:8080/mall/schedule-kd.git', 'http://192.168.1.248:8080/mall/schedule-kd', 'schedule-kd', 'mall / schedule-kd', 'schedule-kd', 'mall/schedule-kd', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (302, '星火计划CMS', 'git@192.168.1.248:mall/xinghuo-cms.git', 'http://192.168.1.248:8080/mall/xinghuo-cms.git', 'http://192.168.1.248:8080/mall/xinghuo-cms', 'xinghuo-cms', 'mall / xinghuo-cms', 'xinghuo-cms', 'mall/xinghuo-cms', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (301, '星火计划', 'git@192.168.1.248:mall/xinghuo.git', 'http://192.168.1.248:8080/mall/xinghuo.git', 'http://192.168.1.248:8080/mall/xinghuo', 'xinghuo', 'mall / xinghuo', 'xinghuo', 'mall/xinghuo', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (295, '数据大屏', 'git@192.168.1.248:mall/data-platform.git', 'http://192.168.1.248:8080/mall/data-platform.git', 'http://192.168.1.248:8080/mall/data-platform', 'data-platform', 'mall / data-platform', 'data-platform', 'mall/data-platform', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (260, '配置文件资源库', 'git@192.168.1.248:mall/config-repository.git', 'http://192.168.1.248:8080/mall/config-repository.git', 'http://192.168.1.248:8080/mall/config-repository', 'config-repository', 'mall / config-repository', 'config-repository', 'mall/config-repository', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (255, 'spring cloud网关服务', 'git@192.168.1.248:mall/gateway.git', 'http://192.168.1.248:8080/mall/gateway.git', 'http://192.168.1.248:8080/mall/gateway', 'gateway', 'mall / gateway', 'gateway', 'mall/gateway', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (213, '用户中心平台', 'git@192.168.1.248:mall/user-center-platform.git', 'http://192.168.1.248:8080/mall/user-center-platform.git', 'http://192.168.1.248:8080/mall/user-center-platform', 'user-center-platform', 'mall / user-center-platform', 'user-center-platform', 'mall/user-center-platform', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (211, '商品中心平台', 'git@192.168.1.248:mall/item-center-platform.git', 'http://192.168.1.248:8080/mall/item-center-platform.git', 'http://192.168.1.248:8080/mall/item-center-platform', 'item-center-platform', 'mall / item-center-platform', 'item-center-platform', 'mall/item-center-platform', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (197, '收银系统平台端', 'git@192.168.1.248:mall/pos-platform.git', 'http://192.168.1.248:8080/mall/pos-platform.git', 'http://192.168.1.248:8080/mall/pos-platform', 'pos-platform', 'mall / pos-platform', 'pos-platform', 'mall/pos-platform', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (196, '收银系统商户端', 'git@192.168.1.248:mall/pos-shop.git', 'http://192.168.1.248:8080/mall/pos-shop.git', 'http://192.168.1.248:8080/mall/pos-shop', 'pos-shop', 'mall / pos-shop', 'pos-shop', 'mall/pos-shop', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (195, 'Spring Cloud 监控平台', 'git@192.168.1.248:mall/spring-boot-admin-server.git', 'http://192.168.1.248:8080/mall/spring-boot-admin-server.git', 'http://192.168.1.248:8080/mall/spring-boot-admin-server', 'spring-boot-admin-server', 'mall / spring-boot-admin-server', 'spring-boot-admin-server', 'mall/spring-boot-admin-server', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (194, '收银系统商品中心', 'git@192.168.1.248:mall/pos-item-center.git', 'http://192.168.1.248:8080/mall/pos-item-center.git', 'http://192.168.1.248:8080/mall/pos-item-center', 'pos-item-center', 'mall / pos-item-center', 'pos-item-center', 'mall/pos-item-center', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (193, '收银系统销售单服务', 'git@192.168.1.248:mall/pos-order-center.git', 'http://192.168.1.248:8080/mall/pos-order-center.git', 'http://192.168.1.248:8080/mall/pos-order-center', 'pos-order-center', 'mall / pos-order-center', 'pos-order-center', 'mall/pos-order-center', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (192, '收银系统销售单服务', 'git@192.168.1.248:mall/pos-order-center-del.git', 'http://192.168.1.248:8080/mall/pos-order-center-del.git', 'http://192.168.1.248:8080/mall/pos-order-center-del', 'pos-order-center-del', 'mall / pos-order-center-del', 'pos-order-center-del', 'mall/pos-order-center-del', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (178, '', 'git@192.168.1.248:mall/hystrix-turbine.git', 'http://192.168.1.248:8080/mall/hystrix-turbine.git', 'http://192.168.1.248:8080/mall/hystrix-turbine', 'hystrix-turbine', 'mall / hystrix-turbine', 'hystrix-turbine', 'mall/hystrix-turbine', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (174, '配置中心', 'git@192.168.1.248:mall/config-server.git', 'http://192.168.1.248:8080/mall/config-server.git', 'http://192.168.1.248:8080/mall/config-server', 'config-server', 'mall / config-server', 'config-server', 'mall/config-server', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (159, '用户中心', 'git@192.168.1.248:mall/user-center.git', 'http://192.168.1.248:8080/mall/user-center.git', 'http://192.168.1.248:8080/mall/user-center', 'user-center', 'mall / user-center', 'user-center', 'mall/user-center', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (158, 'spring cloud注册中心', 'git@192.168.1.248:mall/spring-cloud-server.git', 'http://192.168.1.248:8080/mall/spring-cloud-server.git', 'http://192.168.1.248:8080/mall/spring-cloud-server', 'spring-cloud-server', 'mall / spring-cloud-server', 'spring-cloud-server', 'mall/spring-cloud-server', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (157, '商品中心', 'git@192.168.1.248:mall/item-center.git', 'http://192.168.1.248:8080/mall/item-center.git', 'http://192.168.1.248:8080/mall/item-center', 'item-center', 'mall / item-center', 'item-center', 'mall/item-center', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (156, '订单中心', 'git@192.168.1.248:mall/order-center.git', 'http://192.168.1.248:8080/mall/order-center.git', 'http://192.168.1.248:8080/mall/order-center', 'order-center', 'mall / order-center', 'order-center', 'mall/order-center', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (152, '通用工具类', 'git@192.168.1.248:mall/common.git', 'http://192.168.1.248:8080/mall/common.git', 'http://192.168.1.248:8080/mall/common', 'common', 'mall / common', 'common', 'mall/common', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (151, '权限管理', 'git@192.168.1.248:mall/authority.git', 'http://192.168.1.248:8080/mall/authority.git', 'http://192.168.1.248:8080/mall/authority', 'authority', 'mall / authority', 'authority', 'mall/authority', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (142, '电子合同项目', 'git@192.168.1.248:mall/e-contract.git', 'http://192.168.1.248:8080/mall/e-contract.git', 'http://192.168.1.248:8080/mall/e-contract', 'e-contract', 'mall / e-contract', 'e-contract', 'mall/e-contract', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (141, '序列化集成', 'git@192.168.1.248:mall/serialization.git', 'http://192.168.1.248:8080/mall/serialization.git', 'http://192.168.1.248:8080/mall/serialization', 'serialization', 'mall / serialization', 'serialization', 'mall/serialization', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (139, 'www官网的cms系统', 'git@192.168.1.248:mall/www-mamaqunaer-cms.git', 'http://192.168.1.248:8080/mall/www-mamaqunaer-cms.git', 'http://192.168.1.248:8080/mall/www-mamaqunaer-cms', 'www-mamaqunaer-cms', 'mall / www-mamaqunaer-cms', 'www-mamaqunaer-cms', 'mall/www-mamaqunaer-cms', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (138, 'www官网', 'git@192.168.1.248:mall/www-mamaqunaer.git', 'http://192.168.1.248:8080/mall/www-mamaqunaer.git', 'http://192.168.1.248:8080/mall/www-mamaqunaer', 'www-mamaqunaer', 'mall / www-mamaqunaer', 'www-mamaqunaer', 'mall/www-mamaqunaer', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (125, '进货商城ERP系统', 'git@192.168.1.248:mall/erp.git', 'http://192.168.1.248:8080/mall/erp.git', 'http://192.168.1.248:8080/mall/erp', 'erp', 'mall / erp', 'erp', 'mall/erp', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (124, 'elasticsearch client', 'git@192.168.1.248:mall/es.git', 'http://192.168.1.248:8080/mall/es.git', 'http://192.168.1.248:8080/mall/es', 'es', 'mall / es', 'es', 'mall/es', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (99, '会话模块', 'git@192.168.1.248:mall/session.git', 'http://192.168.1.248:8080/mall/session.git', 'http://192.168.1.248:8080/mall/session', 'session', 'mall / session', 'session', 'mall/session', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (98, '发送短信的jar', 'git@192.168.1.248:mall/sms.git', 'http://192.168.1.248:8080/mall/sms.git', 'http://192.168.1.248:8080/mall/sms', 'sms', 'mall / sms', 'sms', 'mall/sms', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (97, '缓存模块', 'git@192.168.1.248:mall/cache.git', 'http://192.168.1.248:8080/mall/cache.git', 'http://192.168.1.248:8080/mall/cache', 'cache', 'mall / cache', 'cache', 'mall/cache', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (90, '进货商城供应商应用', 'git@192.168.1.248:mall/supplier.git', 'http://192.168.1.248:8080/mall/supplier.git', 'http://192.168.1.248:8080/mall/supplier', 'supplier', 'mall / supplier', 'supplier', 'mall/supplier', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (89, '进货商城CMS系统', 'git@192.168.1.248:mall/cms.git', 'http://192.168.1.248:8080/mall/cms.git', 'http://192.168.1.248:8080/mall/cms', 'cms', 'mall / cms', 'cms', 'mall/cms', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (81, '进货商城门店应用', 'git@192.168.1.248:mall/xiaodian.git', 'http://192.168.1.248:8080/mall/xiaodian.git', 'http://192.168.1.248:8080/mall/xiaodian', 'xiaodian', 'mall / xiaodian', 'xiaodian', 'mall/xiaodian', NULL, NULL, NULL, NULL);
INSERT INTO public.git_repo VALUES (79, '进货商城相关文档', 'git@192.168.1.248:mall/docs.git', 'http://192.168.1.248:8080/mall/docs.git', 'http://192.168.1.248:8080/mall/docs', 'docs', 'mall / docs', 'docs', 'mall/docs', NULL, NULL, NULL, NULL);


--
-- Data for Name: publishment; Type: TABLE DATA; Schema: public; Owner: wangnan
--

INSERT INTO public.publishment VALUES (8, 309, 'develop,master', 'dev', 'root', '192.168.1.249', '/data/project/mama_schedule_kd', 'schedule-kd', '', '', '', '', 0, 'develop_schedule_kd', '进货商城ERP与金蝶数据互通项目（线下环境）', NULL, NULL, NULL, NULL);
INSERT INTO public.publishment VALUES (4, 310, 'develop', 'dev', 'root', '192.168.1.249', '/data/project/mama_spring_boot_actuator_universal', 'spring-boot-actuator-universal', '-Xms768m -Xmx768m', '', '', '', 0, 'develop_spring_boot_actuator_universal', 'Java平台监控系统（线下环境）', NULL, NULL, NULL, NULL);
INSERT INTO public.publishment VALUES (13, 174, 'develop', 'dev', 'root', '192.168.1.248', '/home/project/mama_config_server', 'config-server', '-Xms768m -Xmx768m', NULL, NULL, NULL, 0, 'develop_config_server', '配置中心（线下环境）', NULL, NULL, NULL, NULL);


--
-- Name: git_repo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wangnan
--

SELECT pg_catalog.setval('public.git_repo_id_seq', 1, false);


--
-- Name: publishment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wangnan
--

SELECT pg_catalog.setval('public.publishment_id_seq', 13, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: wangnan
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: git_repo git_repo_pkey; Type: CONSTRAINT; Schema: public; Owner: wangnan
--

ALTER TABLE ONLY public.git_repo
    ADD CONSTRAINT git_repo_pkey PRIMARY KEY (id);


--
-- Name: publishment idx_name; Type: CONSTRAINT; Schema: public; Owner: wangnan
--

ALTER TABLE ONLY public.publishment
    ADD CONSTRAINT idx_name UNIQUE (name);


--
-- Name: CONSTRAINT idx_name ON publishment; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON CONSTRAINT idx_name ON public.publishment IS '发布名称唯一键';


--
-- Name: publishment publishment_pkey; Type: CONSTRAINT; Schema: public; Owner: wangnan
--

ALTER TABLE ONLY public.publishment
    ADD CONSTRAINT publishment_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

