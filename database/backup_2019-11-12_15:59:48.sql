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
    created_at timestamp without time zone NOT NULL,
    created_by character varying(32) NOT NULL,
    last_updated_at timestamp without time zone NOT NULL,
    last_updated_by character varying(32) NOT NULL,
    is_deleted integer NOT NULL
);


ALTER TABLE public.git_repo OWNER TO wangnan;

--
-- Name: COLUMN git_repo.created_at; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.git_repo.created_at IS '创建时间';


--
-- Name: COLUMN git_repo.created_by; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.git_repo.created_by IS '创建人';


--
-- Name: COLUMN git_repo.last_updated_at; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.git_repo.last_updated_at IS '最后更新时间';


--
-- Name: COLUMN git_repo.last_updated_by; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.git_repo.last_updated_by IS '最后更新人';


--
-- Name: COLUMN git_repo.is_deleted; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.git_repo.is_deleted IS '是否删除：0表示正常，1表示已删除';


--
-- Name: git_repo_id_seq; Type: SEQUENCE; Schema: public; Owner: wangnan
--

CREATE SEQUENCE public.git_repo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.git_repo_id_seq OWNER TO wangnan;

--
-- Name: git_repo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wangnan
--

ALTER SEQUENCE public.git_repo_id_seq OWNED BY public.git_repo.id;


--
-- Name: publishment; Type: TABLE; Schema: public; Owner: wangnan
--

CREATE TABLE public.publishment (
    id integer NOT NULL,
    name character varying NOT NULL,
    description character varying NOT NULL,
    git_repo_id integer NOT NULL,
    git_branches character varying(32) NOT NULL,
    profile character varying(8) NOT NULL,
    to_ip character varying(64) NOT NULL,
    to_project_home character varying(64) NOT NULL,
    to_process_name character varying(32) NOT NULL,
    to_java_opts character varying(128),
    git_merged_branch character varying(16),
    git_tag_version character varying(16),
    git_tag_comment character varying(128),
    git_delete_temp_branch integer,
    created_at timestamp without time zone NOT NULL,
    created_by character varying(32) NOT NULL,
    last_updated_at timestamp without time zone NOT NULL,
    last_updated_by character varying(32) NOT NULL,
    is_deleted integer NOT NULL
);


ALTER TABLE public.publishment OWNER TO wangnan;

--
-- Name: COLUMN publishment.id; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.id IS '主键id';


--
-- Name: COLUMN publishment.name; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.name IS '发布名称';


--
-- Name: COLUMN publishment.description; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.description IS '发布描述';


--
-- Name: COLUMN publishment.git_repo_id; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.git_repo_id IS 'git仓库id';


--
-- Name: COLUMN publishment.git_branches; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.git_branches IS '发布的git分支';


--
-- Name: COLUMN publishment.profile; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.profile IS '发布环境';


--
-- Name: COLUMN publishment.to_ip; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.to_ip IS '目标服务器ip，多个以半角逗号分隔';


--
-- Name: COLUMN publishment.to_project_home; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.to_project_home IS '目标服务器项目主目录';


--
-- Name: COLUMN publishment.to_process_name; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.to_process_name IS '目标服务器项目进程名';


--
-- Name: COLUMN publishment.to_java_opts; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.to_java_opts IS 'JAVA变量';


--
-- Name: COLUMN publishment.git_merged_branch; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.git_merged_branch IS '发布完毕后git合并到的分支';


--
-- Name: COLUMN publishment.git_tag_version; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.git_tag_version IS '发布完毕后git打标签名';


--
-- Name: COLUMN publishment.git_tag_comment; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.git_tag_comment IS '发布完毕后git打标签备注，依赖于git_tag_version';


--
-- Name: COLUMN publishment.git_delete_temp_branch; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.git_delete_temp_branch IS '发布完毕后是否删除临时git分支，多分支发布时有效';


--
-- Name: COLUMN publishment.created_at; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.created_at IS '创建时间';


--
-- Name: COLUMN publishment.created_by; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.created_by IS '创建人';


--
-- Name: COLUMN publishment.last_updated_at; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.last_updated_at IS '最后更新时间';


--
-- Name: COLUMN publishment.last_updated_by; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.last_updated_by IS '最后更新人';


--
-- Name: COLUMN publishment.is_deleted; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.is_deleted IS '是否删除：0表示正常，1表示已删除';


--
-- Name: publishment_id_seq; Type: SEQUENCE; Schema: public; Owner: wangnan
--

CREATE SEQUENCE public.publishment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.publishment_id_seq OWNER TO wangnan;

--
-- Name: publishment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wangnan
--

ALTER SEQUENCE public.publishment_id_seq OWNED BY public.publishment.id;


--
-- Name: git_repo id; Type: DEFAULT; Schema: public; Owner: wangnan
--

ALTER TABLE ONLY public.git_repo ALTER COLUMN id SET DEFAULT nextval('public.git_repo_id_seq'::regclass);


--
-- Name: publishment id; Type: DEFAULT; Schema: public; Owner: wangnan
--

ALTER TABLE ONLY public.publishment ALTER COLUMN id SET DEFAULT nextval('public.publishment_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: wangnan
--

INSERT INTO public.alembic_version VALUES ('2579e237c51a');


--
-- Data for Name: git_repo; Type: TABLE DATA; Schema: public; Owner: wangnan
--

INSERT INTO public.git_repo VALUES (195, 'Spring Cloud 监控平台', 'git@192.168.1.248:mall/spring-boot-admin-server.git', 'http://192.168.1.248:8080/mall/spring-boot-admin-server.git', 'http://192.168.1.248:8080/mall/spring-boot-admin-server', 'spring-boot-admin-server', 'mall / spring-boot-admin-server', 'spring-boot-admin-server', 'mall/spring-boot-admin-server', '2019-11-11 15:58:30.79321', 'system-auto', '2019-11-11 15:58:30.79321', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (194, '收银系统商品中心', 'git@192.168.1.248:mall/pos-item-center.git', 'http://192.168.1.248:8080/mall/pos-item-center.git', 'http://192.168.1.248:8080/mall/pos-item-center', 'pos-item-center', 'mall / pos-item-center', 'pos-item-center', 'mall/pos-item-center', '2019-11-11 15:58:30.795229', 'system-auto', '2019-11-11 15:58:30.795229', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (193, '收银系统销售单服务', 'git@192.168.1.248:mall/pos-order-center.git', 'http://192.168.1.248:8080/mall/pos-order-center.git', 'http://192.168.1.248:8080/mall/pos-order-center', 'pos-order-center', 'mall / pos-order-center', 'pos-order-center', 'mall/pos-order-center', '2019-11-11 15:58:30.798058', 'system-auto', '2019-11-11 15:58:30.798058', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (192, '收银系统销售单服务', 'git@192.168.1.248:mall/pos-order-center-del.git', 'http://192.168.1.248:8080/mall/pos-order-center-del.git', 'http://192.168.1.248:8080/mall/pos-order-center-del', 'pos-order-center-del', 'mall / pos-order-center-del', 'pos-order-center-del', 'mall/pos-order-center-del', '2019-11-11 15:58:30.800524', 'system-auto', '2019-11-11 15:58:30.800524', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (174, '配置中心', 'git@192.168.1.248:mall/config-server.git', 'http://192.168.1.248:8080/mall/config-server.git', 'http://192.168.1.248:8080/mall/config-server', 'config-server', 'mall / config-server', 'config-server', 'mall/config-server', '2019-11-11 15:58:30.804911', 'system-auto', '2019-11-11 15:58:30.804911', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (159, '用户中心', 'git@192.168.1.248:mall/user-center.git', 'http://192.168.1.248:8080/mall/user-center.git', 'http://192.168.1.248:8080/mall/user-center', 'user-center', 'mall / user-center', 'user-center', 'mall/user-center', '2019-11-11 15:58:30.806986', 'system-auto', '2019-11-11 15:58:30.806986', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (158, 'spring cloud注册中心', 'git@192.168.1.248:mall/spring-cloud-server.git', 'http://192.168.1.248:8080/mall/spring-cloud-server.git', 'http://192.168.1.248:8080/mall/spring-cloud-server', 'spring-cloud-server', 'mall / spring-cloud-server', 'spring-cloud-server', 'mall/spring-cloud-server', '2019-11-11 15:58:30.809074', 'system-auto', '2019-11-11 15:58:30.809074', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (157, '商品中心', 'git@192.168.1.248:mall/item-center.git', 'http://192.168.1.248:8080/mall/item-center.git', 'http://192.168.1.248:8080/mall/item-center', 'item-center', 'mall / item-center', 'item-center', 'mall/item-center', '2019-11-11 15:58:30.811098', 'system-auto', '2019-11-11 15:58:30.811098', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (156, '订单中心', 'git@192.168.1.248:mall/order-center.git', 'http://192.168.1.248:8080/mall/order-center.git', 'http://192.168.1.248:8080/mall/order-center', 'order-center', 'mall / order-center', 'order-center', 'mall/order-center', '2019-11-11 15:58:30.814227', 'system-auto', '2019-11-11 15:58:30.814227', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (152, '通用工具类', 'git@192.168.1.248:mall/common.git', 'http://192.168.1.248:8080/mall/common.git', 'http://192.168.1.248:8080/mall/common', 'common', 'mall / common', 'common', 'mall/common', '2019-11-11 15:58:30.817099', 'system-auto', '2019-11-11 15:58:30.817099', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (151, '权限管理', 'git@192.168.1.248:mall/authority.git', 'http://192.168.1.248:8080/mall/authority.git', 'http://192.168.1.248:8080/mall/authority', 'authority', 'mall / authority', 'authority', 'mall/authority', '2019-11-11 15:58:30.819471', 'system-auto', '2019-11-11 15:58:30.819471', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (142, '电子合同项目', 'git@192.168.1.248:mall/e-contract.git', 'http://192.168.1.248:8080/mall/e-contract.git', 'http://192.168.1.248:8080/mall/e-contract', 'e-contract', 'mall / e-contract', 'e-contract', 'mall/e-contract', '2019-11-11 15:58:30.821709', 'system-auto', '2019-11-11 15:58:30.821709', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (141, '序列化集成', 'git@192.168.1.248:mall/serialization.git', 'http://192.168.1.248:8080/mall/serialization.git', 'http://192.168.1.248:8080/mall/serialization', 'serialization', 'mall / serialization', 'serialization', 'mall/serialization', '2019-11-11 15:58:30.82394', 'system-auto', '2019-11-11 15:58:30.82394', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (139, 'www官网的cms系统', 'git@192.168.1.248:mall/www-mamaqunaer-cms.git', 'http://192.168.1.248:8080/mall/www-mamaqunaer-cms.git', 'http://192.168.1.248:8080/mall/www-mamaqunaer-cms', 'www-mamaqunaer-cms', 'mall / www-mamaqunaer-cms', 'www-mamaqunaer-cms', 'mall/www-mamaqunaer-cms', '2019-11-11 15:58:30.826399', 'system-auto', '2019-11-11 15:58:30.826399', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (138, 'www官网', 'git@192.168.1.248:mall/www-mamaqunaer.git', 'http://192.168.1.248:8080/mall/www-mamaqunaer.git', 'http://192.168.1.248:8080/mall/www-mamaqunaer', 'www-mamaqunaer', 'mall / www-mamaqunaer', 'www-mamaqunaer', 'mall/www-mamaqunaer', '2019-11-11 15:58:30.829048', 'system-auto', '2019-11-11 15:58:30.829048', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (125, '进货商城ERP系统', 'git@192.168.1.248:mall/erp.git', 'http://192.168.1.248:8080/mall/erp.git', 'http://192.168.1.248:8080/mall/erp', 'erp', 'mall / erp', 'erp', 'mall/erp', '2019-11-11 15:58:30.832151', 'system-auto', '2019-11-11 15:58:30.832151', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (124, 'elasticsearch client', 'git@192.168.1.248:mall/es.git', 'http://192.168.1.248:8080/mall/es.git', 'http://192.168.1.248:8080/mall/es', 'es', 'mall / es', 'es', 'mall/es', '2019-11-11 15:58:30.834431', 'system-auto', '2019-11-11 15:58:30.834431', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (99, '会话模块', 'git@192.168.1.248:mall/session.git', 'http://192.168.1.248:8080/mall/session.git', 'http://192.168.1.248:8080/mall/session', 'session', 'mall / session', 'session', 'mall/session', '2019-11-11 15:58:30.836591', 'system-auto', '2019-11-11 15:58:30.836591', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (98, '发送短信的jar', 'git@192.168.1.248:mall/sms.git', 'http://192.168.1.248:8080/mall/sms.git', 'http://192.168.1.248:8080/mall/sms', 'sms', 'mall / sms', 'sms', 'mall/sms', '2019-11-11 15:58:30.838672', 'system-auto', '2019-11-11 15:58:30.838672', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (97, '缓存模块', 'git@192.168.1.248:mall/cache.git', 'http://192.168.1.248:8080/mall/cache.git', 'http://192.168.1.248:8080/mall/cache', 'cache', 'mall / cache', 'cache', 'mall/cache', '2019-11-11 15:58:30.840668', 'system-auto', '2019-11-11 15:58:30.840668', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (90, '进货商城供应商应用', 'git@192.168.1.248:mall/supplier.git', 'http://192.168.1.248:8080/mall/supplier.git', 'http://192.168.1.248:8080/mall/supplier', 'supplier', 'mall / supplier', 'supplier', 'mall/supplier', '2019-11-11 15:58:30.842722', 'system-auto', '2019-11-11 15:58:30.842722', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (89, '进货商城CMS系统', 'git@192.168.1.248:mall/cms.git', 'http://192.168.1.248:8080/mall/cms.git', 'http://192.168.1.248:8080/mall/cms', 'cms', 'mall / cms', 'cms', 'mall/cms', '2019-11-11 15:58:30.844693', 'system-auto', '2019-11-11 15:58:30.844693', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (79, '进货商城相关文档', 'git@192.168.1.248:mall/docs.git', 'http://192.168.1.248:8080/mall/docs.git', 'http://192.168.1.248:8080/mall/docs', 'docs', 'mall / docs', 'docs', 'mall/docs', '2019-11-11 15:58:30.849842', 'system-auto', '2019-11-11 15:58:30.849842', 'system-auto', 1);
INSERT INTO public.git_repo VALUES (81, '进货商城门店应用', 'git@192.168.1.248:mall/xiaodian.git', 'http://192.168.1.248:8080/mall/xiaodian.git', 'http://192.168.1.248:8080/mall/xiaodian', 'xiaodian', 'mall / xiaodian', 'xiaodian', 'mall/xiaodian', '2019-11-11 15:58:30.847074', 'system-auto', '2019-11-11 15:58:30.847074', 'system-auto', 1);
INSERT INTO public.git_repo VALUES (318, '妈妈优选/妈妈纷享后台CMS系统（含schedule定时调度系统）', 'git@192.168.1.248:mall/youxuan-cms.git', 'http://192.168.1.248:8080/mall/youxuan-cms.git', 'http://192.168.1.248:8080/mall/youxuan-cms', 'youxuan-cms', 'mall / youxuan-cms', 'youxuan-cms', 'mall/youxuan-cms', '2019-11-11 15:58:30.760822', 'system-auto', '2019-11-11 15:58:30.760822', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (317, '妈妈优选/妈妈纷享对外系统（买家端、卖家端）', 'git@192.168.1.248:mall/youxuan.git', 'http://192.168.1.248:8080/mall/youxuan.git', 'http://192.168.1.248:8080/mall/youxuan', 'youxuan', 'mall / youxuan', 'youxuan', 'mall/youxuan', '2019-11-11 15:58:30.762897', 'system-auto', '2019-11-11 15:58:30.762897', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (310, '应用监控平台', 'git@192.168.1.248:mall/spring-boot-actuator-universal.git', 'http://192.168.1.248:8080/mall/spring-boot-actuator-universal.git', 'http://192.168.1.248:8080/mall/spring-boot-actuator-universal', 'spring-boot-actuator-universal', 'mall / spring-boot-actuator-universal', 'spring-boot-actuator-universal', 'mall/spring-boot-actuator-universal', '2019-11-11 15:58:30.765638', 'system-auto', '2019-11-11 15:58:30.765638', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (309, '进货商城、ERP与金蝶数据交换项目', 'git@192.168.1.248:mall/schedule-kd.git', 'http://192.168.1.248:8080/mall/schedule-kd.git', 'http://192.168.1.248:8080/mall/schedule-kd', 'schedule-kd', 'mall / schedule-kd', 'schedule-kd', 'mall/schedule-kd', '2019-11-11 15:58:30.767912', 'system-auto', '2019-11-11 15:58:30.767912', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (302, '星火计划CMS', 'git@192.168.1.248:mall/xinghuo-cms.git', 'http://192.168.1.248:8080/mall/xinghuo-cms.git', 'http://192.168.1.248:8080/mall/xinghuo-cms', 'xinghuo-cms', 'mall / xinghuo-cms', 'xinghuo-cms', 'mall/xinghuo-cms', '2019-11-11 15:58:30.769859', 'system-auto', '2019-11-11 15:58:30.769859', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (301, '星火计划', 'git@192.168.1.248:mall/xinghuo.git', 'http://192.168.1.248:8080/mall/xinghuo.git', 'http://192.168.1.248:8080/mall/xinghuo', 'xinghuo', 'mall / xinghuo', 'xinghuo', 'mall/xinghuo', '2019-11-11 15:58:30.773132', 'system-auto', '2019-11-11 15:58:30.773132', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (300, '星火计划管理后台', 'git@192.168.1.248:2019_lx_group/spark_BMS.git', 'http://192.168.1.248:8080/2019_lx_group/spark_BMS.git', 'http://192.168.1.248:8080/2019_lx_group/spark_BMS', 'spark_BMS', '2019_lx_group / spark_BMS', 'spark_BMS', '2019_lx_group/spark_BMS', '2019-11-11 15:58:30.775578', 'system-auto', '2019-11-11 15:58:30.775578', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (295, '数据大屏', 'git@192.168.1.248:mall/data-platform.git', 'http://192.168.1.248:8080/mall/data-platform.git', 'http://192.168.1.248:8080/mall/data-platform', 'data-platform', 'mall / data-platform', 'data-platform', 'mall/data-platform', '2019-11-11 15:58:30.777646', 'system-auto', '2019-11-11 15:58:30.777646', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (260, '配置文件资源库', 'git@192.168.1.248:mall/config-repository.git', 'http://192.168.1.248:8080/mall/config-repository.git', 'http://192.168.1.248:8080/mall/config-repository', 'config-repository', 'mall / config-repository', 'config-repository', 'mall/config-repository', '2019-11-11 15:58:30.779694', 'system-auto', '2019-11-11 15:58:30.779694', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (255, 'spring cloud网关服务', 'git@192.168.1.248:mall/gateway.git', 'http://192.168.1.248:8080/mall/gateway.git', 'http://192.168.1.248:8080/mall/gateway', 'gateway', 'mall / gateway', 'gateway', 'mall/gateway', '2019-11-11 15:58:30.782243', 'system-auto', '2019-11-11 15:58:30.782243', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (213, '用户中心平台', 'git@192.168.1.248:mall/user-center-platform.git', 'http://192.168.1.248:8080/mall/user-center-platform.git', 'http://192.168.1.248:8080/mall/user-center-platform', 'user-center-platform', 'mall / user-center-platform', 'user-center-platform', 'mall/user-center-platform', '2019-11-11 15:58:30.784432', 'system-auto', '2019-11-11 15:58:30.784432', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (211, '商品中心平台', 'git@192.168.1.248:mall/item-center-platform.git', 'http://192.168.1.248:8080/mall/item-center-platform.git', 'http://192.168.1.248:8080/mall/item-center-platform', 'item-center-platform', 'mall / item-center-platform', 'item-center-platform', 'mall/item-center-platform', '2019-11-11 15:58:30.78656', 'system-auto', '2019-11-11 15:58:30.78656', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (197, '收银系统平台端', 'git@192.168.1.248:mall/pos-platform.git', 'http://192.168.1.248:8080/mall/pos-platform.git', 'http://192.168.1.248:8080/mall/pos-platform', 'pos-platform', 'mall / pos-platform', 'pos-platform', 'mall/pos-platform', '2019-11-11 15:58:30.789059', 'system-auto', '2019-11-11 15:58:30.789059', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (196, '收银系统商户端', 'git@192.168.1.248:mall/pos-shop.git', 'http://192.168.1.248:8080/mall/pos-shop.git', 'http://192.168.1.248:8080/mall/pos-shop', 'pos-shop', 'mall / pos-shop', 'pos-shop', 'mall/pos-shop', '2019-11-11 15:58:30.791178', 'system-auto', '2019-11-11 15:58:30.791178', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (178, '', 'git@192.168.1.248:mall/hystrix-turbine.git', 'http://192.168.1.248:8080/mall/hystrix-turbine.git', 'http://192.168.1.248:8080/mall/hystrix-turbine', 'hystrix-turbine', 'mall / hystrix-turbine', 'hystrix-turbine', 'mall/hystrix-turbine', '2019-11-11 15:58:30.802756', 'system-auto', '2019-11-11 15:58:30.802756', 'system-auto', 0);


--
-- Data for Name: publishment; Type: TABLE DATA; Schema: public; Owner: wangnan
--

INSERT INTO public.publishment VALUES (5, 'develop_spring_boot_actuator_universal', '全局应用监控（线下）', 310, 'develop', 'dev', '192.168.1.249', '/data/project/mama_spring_boot_actuator_universal', 'spring-boot-actuator-universal', NULL, NULL, NULL, NULL, 0, '2019-11-11 17:15:18.058975', 'HTTP post request', '2019-11-11 17:15:18.058975', 'HTTP post request', 0);


--
-- Name: git_repo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wangnan
--

SELECT pg_catalog.setval('public.git_repo_id_seq', 1, false);


--
-- Name: publishment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wangnan
--

SELECT pg_catalog.setval('public.publishment_id_seq', 5, true);


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
-- Name: publishment publishment_pkey; Type: CONSTRAINT; Schema: public; Owner: wangnan
--

ALTER TABLE ONLY public.publishment
    ADD CONSTRAINT publishment_pkey PRIMARY KEY (id);


--
-- Name: publishment publishment_git_repo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wangnan
--

ALTER TABLE ONLY public.publishment
    ADD CONSTRAINT publishment_git_repo_id_fkey FOREIGN KEY (git_repo_id) REFERENCES public.git_repo(id);


--
-- PostgreSQL database dump complete
--

