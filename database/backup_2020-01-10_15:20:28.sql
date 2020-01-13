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
    name character varying(64) NOT NULL,
    description character varying(128) NOT NULL,
    git_repo_id integer NOT NULL,
    git_branches character varying(64) NOT NULL,
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
    is_deleted integer NOT NULL,
    source_file_dir character varying(64),
    git_branch_type character varying(8)
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
-- Name: COLUMN publishment.source_file_dir; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment.source_file_dir IS '发布文件的相对目录（相对于源项目的根目录）';


--
-- Name: publishment_fe_vue; Type: TABLE; Schema: public; Owner: wangnan
--

CREATE TABLE public.publishment_fe_vue (
    id integer NOT NULL,
    name character varying(64) NOT NULL,
    description character varying(128) NOT NULL,
    git_repo_id integer NOT NULL,
    git_branches character varying(32) NOT NULL,
    profile character varying(8) NOT NULL,
    to_ip character varying(64) NOT NULL,
    to_project_home character varying(64) NOT NULL,
    created_at timestamp without time zone NOT NULL,
    created_by character varying(32) NOT NULL,
    last_updated_at timestamp without time zone NOT NULL,
    last_updated_by character varying(32) NOT NULL,
    is_deleted integer NOT NULL,
    source_file_dir character varying(64)
);


ALTER TABLE public.publishment_fe_vue OWNER TO wangnan;

--
-- Name: COLUMN publishment_fe_vue.id; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_fe_vue.id IS '主键id';


--
-- Name: COLUMN publishment_fe_vue.name; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_fe_vue.name IS '发布名称';


--
-- Name: COLUMN publishment_fe_vue.description; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_fe_vue.description IS '发布描述';


--
-- Name: COLUMN publishment_fe_vue.git_repo_id; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_fe_vue.git_repo_id IS 'git仓库id';


--
-- Name: COLUMN publishment_fe_vue.git_branches; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_fe_vue.git_branches IS '发布的git分支';


--
-- Name: COLUMN publishment_fe_vue.profile; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_fe_vue.profile IS '发布环境';


--
-- Name: COLUMN publishment_fe_vue.to_ip; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_fe_vue.to_ip IS '目标服务器ip';


--
-- Name: COLUMN publishment_fe_vue.to_project_home; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_fe_vue.to_project_home IS '目标服务器主目录';


--
-- Name: COLUMN publishment_fe_vue.created_at; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_fe_vue.created_at IS '创建时间';


--
-- Name: COLUMN publishment_fe_vue.created_by; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_fe_vue.created_by IS '创建人';


--
-- Name: COLUMN publishment_fe_vue.last_updated_at; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_fe_vue.last_updated_at IS '最后更新时间';


--
-- Name: COLUMN publishment_fe_vue.last_updated_by; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_fe_vue.last_updated_by IS '最后更新人';


--
-- Name: COLUMN publishment_fe_vue.is_deleted; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_fe_vue.is_deleted IS '是否删除：0表示正常，1表示已删除';


--
-- Name: publishment_fe_vue_id_seq; Type: SEQUENCE; Schema: public; Owner: wangnan
--

CREATE SEQUENCE public.publishment_fe_vue_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.publishment_fe_vue_id_seq OWNER TO wangnan;

--
-- Name: publishment_fe_vue_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wangnan
--

ALTER SEQUENCE public.publishment_fe_vue_id_seq OWNED BY public.publishment_fe_vue.id;


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
-- Name: publishment_nodejs; Type: TABLE; Schema: public; Owner: wangnan
--

CREATE TABLE public.publishment_nodejs (
    id integer DEFAULT nextval('public.publishment_nodejs_id_seq'::regclass) NOT NULL,
    name character varying(64) NOT NULL,
    description character varying(128) NOT NULL,
    git_repo_id integer NOT NULL,
    git_branches character varying(32) NOT NULL,
    profile character varying(8) NOT NULL,
    to_ip character varying(64) NOT NULL,
    to_project_home character varying(64) NOT NULL,
    created_at timestamp without time zone NOT NULL,
    created_by character varying(32) NOT NULL,
    last_updated_at timestamp without time zone NOT NULL,
    last_updated_by character varying(32) NOT NULL,
    is_deleted integer NOT NULL,
    source_file_dir character varying(64)
);


ALTER TABLE public.publishment_nodejs OWNER TO wangnan;

--
-- Name: COLUMN publishment_nodejs.id; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_nodejs.id IS '主键id';


--
-- Name: COLUMN publishment_nodejs.name; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_nodejs.name IS '发布名称';


--
-- Name: COLUMN publishment_nodejs.description; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_nodejs.description IS '发布描述';


--
-- Name: COLUMN publishment_nodejs.git_repo_id; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_nodejs.git_repo_id IS 'git仓库id';


--
-- Name: COLUMN publishment_nodejs.git_branches; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_nodejs.git_branches IS '发布的git分支';


--
-- Name: COLUMN publishment_nodejs.profile; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_nodejs.profile IS '发布环境';


--
-- Name: COLUMN publishment_nodejs.to_ip; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_nodejs.to_ip IS '目标服务器ip';


--
-- Name: COLUMN publishment_nodejs.to_project_home; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_nodejs.to_project_home IS '目标服务器主目录';


--
-- Name: COLUMN publishment_nodejs.created_at; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_nodejs.created_at IS '创建时间';


--
-- Name: COLUMN publishment_nodejs.created_by; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_nodejs.created_by IS '创建人';


--
-- Name: COLUMN publishment_nodejs.last_updated_at; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_nodejs.last_updated_at IS '最后更新时间';


--
-- Name: COLUMN publishment_nodejs.last_updated_by; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_nodejs.last_updated_by IS '最后更新人';


--
-- Name: COLUMN publishment_nodejs.is_deleted; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_nodejs.is_deleted IS '是否删除：0表示正常，1表示已删除';


--
-- Name: publishment_staticfile; Type: TABLE; Schema: public; Owner: wangnan
--

CREATE TABLE public.publishment_staticfile (
    id integer NOT NULL,
    name character varying(64) NOT NULL,
    description character varying(128) NOT NULL,
    git_repo_id integer NOT NULL,
    git_branches character varying(32) NOT NULL,
    to_ip character varying(64) NOT NULL,
    to_project_home character varying(64) NOT NULL,
    created_at timestamp without time zone NOT NULL,
    created_by character varying(32) NOT NULL,
    is_deleted integer NOT NULL,
    last_updated_at timestamp without time zone NOT NULL,
    last_updated_by character varying(32) NOT NULL,
    source_file_dir character varying(64)
);


ALTER TABLE public.publishment_staticfile OWNER TO wangnan;

--
-- Name: COLUMN publishment_staticfile.id; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_staticfile.id IS '主键id';


--
-- Name: COLUMN publishment_staticfile.name; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_staticfile.name IS '发布名称';


--
-- Name: COLUMN publishment_staticfile.description; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_staticfile.description IS '发布描述';


--
-- Name: COLUMN publishment_staticfile.git_repo_id; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_staticfile.git_repo_id IS 'git仓库id';


--
-- Name: COLUMN publishment_staticfile.git_branches; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_staticfile.git_branches IS '发布的git分支';


--
-- Name: COLUMN publishment_staticfile.to_ip; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_staticfile.to_ip IS '目标服务器ip';


--
-- Name: COLUMN publishment_staticfile.to_project_home; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_staticfile.to_project_home IS '目标服务器主目录';


--
-- Name: COLUMN publishment_staticfile.created_at; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_staticfile.created_at IS '创建时间';


--
-- Name: COLUMN publishment_staticfile.created_by; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_staticfile.created_by IS '创建人';


--
-- Name: COLUMN publishment_staticfile.is_deleted; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_staticfile.is_deleted IS '是否删除：0表示正常，1表示已删除';


--
-- Name: COLUMN publishment_staticfile.last_updated_at; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_staticfile.last_updated_at IS '最后更新时间';


--
-- Name: COLUMN publishment_staticfile.last_updated_by; Type: COMMENT; Schema: public; Owner: wangnan
--

COMMENT ON COLUMN public.publishment_staticfile.last_updated_by IS '最后更新人';


--
-- Name: publishment_staticfile_id_seq; Type: SEQUENCE; Schema: public; Owner: wangnan
--

CREATE SEQUENCE public.publishment_staticfile_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.publishment_staticfile_id_seq OWNER TO wangnan;

--
-- Name: publishment_staticfile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wangnan
--

ALTER SEQUENCE public.publishment_staticfile_id_seq OWNED BY public.publishment_staticfile.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: wangnan
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    login_code character varying(32) NOT NULL,
    login_pwd character varying(32) NOT NULL,
    nick_name character varying(32) NOT NULL,
    email character varying(64),
    gitlab_email character varying(64),
    created_at timestamp without time zone NOT NULL,
    created_by character varying(32) NOT NULL,
    last_updated_at timestamp without time zone,
    last_updated_by character varying(32),
    is_deleted integer DEFAULT 0 NOT NULL,
    role character varying(16) NOT NULL
);


ALTER TABLE public."user" OWNER TO wangnan;

--
-- Name: git_repo id; Type: DEFAULT; Schema: public; Owner: wangnan
--

ALTER TABLE ONLY public.git_repo ALTER COLUMN id SET DEFAULT nextval('public.git_repo_id_seq'::regclass);


--
-- Name: publishment id; Type: DEFAULT; Schema: public; Owner: wangnan
--

ALTER TABLE ONLY public.publishment ALTER COLUMN id SET DEFAULT nextval('public.publishment_id_seq'::regclass);


--
-- Name: publishment_fe_vue id; Type: DEFAULT; Schema: public; Owner: wangnan
--

ALTER TABLE ONLY public.publishment_fe_vue ALTER COLUMN id SET DEFAULT nextval('public.publishment_fe_vue_id_seq'::regclass);


--
-- Name: publishment_staticfile id; Type: DEFAULT; Schema: public; Owner: wangnan
--

ALTER TABLE ONLY public.publishment_staticfile ALTER COLUMN id SET DEFAULT nextval('public.publishment_staticfile_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: wangnan
--

INSERT INTO public.alembic_version VALUES ('3880a3a819d5');


--
-- Data for Name: git_repo; Type: TABLE DATA; Schema: public; Owner: wangnan
--

INSERT INTO public.git_repo VALUES (351, '集成信鸽涌动推送的客户端', 'git@git.mamaqunaer.cc:mall/xg.git', 'http://git.mamaqunaer.cc/mall/xg.git', 'http://git.mamaqunaer.cc/mall/xg', 'xg', 'mall / xg', 'xg', 'mall/xg', '2020-01-09 18:14:04.563785', 'system-auto', '2020-01-09 18:14:04.563785', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (350, '集成阿里云MNS客户端', 'git@git.mamaqunaer.cc:mall/mns.git', 'http://git.mamaqunaer.cc/mall/mns.git', 'http://git.mamaqunaer.cc/mall/mns', 'mns', 'mall / mns', 'mns', 'mall/mns', '2020-01-09 18:14:04.689833', 'system-auto', '2020-01-09 18:14:04.689833', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (349, '集成物流查询接口的客户端', 'git@git.mamaqunaer.cc:mall/logistics.git', 'http://git.mamaqunaer.cc/mall/logistics.git', 'http://git.mamaqunaer.cc/mall/logistics', 'logistics', 'mall / logistics', 'logistics', 'mall/logistics', '2020-01-09 18:14:04.697297', 'system-auto', '2020-01-09 18:14:04.697297', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (348, '微信小程序识别营业执照工具', 'git@git.mamaqunaer.cc:mall/wxlicense.git', 'http://git.mamaqunaer.cc/mall/wxlicense.git', 'http://git.mamaqunaer.cc/mall/wxlicense', 'wxlicense', 'mall / wxlicense', 'wxlicense', 'mall/wxlicense', '2020-01-09 18:14:04.700772', 'system-auto', '2020-01-09 18:14:04.700772', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (346, '全局的自动配置（主要包括框架类自动配置等）', 'git@git.mamaqunaer.cc:mall/spring-boot-autoconfigure-universal.git', 'http://git.mamaqunaer.cc/mall/spring-boot-autoconfigure-universal.git', 'http://git.mamaqunaer.cc/mall/spring-boot-autoconfigure-universal', 'spring-boot-autoconfigure-universal', 'mall / spring-boot-autoconfigure-universal', 'spring-boot-autoconfigure-universal', 'mall/spring-boot-autoconfigure-universal', '2020-01-09 18:14:04.705741', 'system-auto', '2020-01-09 18:14:04.705741', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (328, '联星贸易官网', 'git@git.mamaqunaer.cc:2019_lx_group/lxtrading.git', 'http://git.mamaqunaer.cc/2019_lx_group/lxtrading.git', 'http://git.mamaqunaer.cc/2019_lx_group/lxtrading', 'lxtrading', '2019_lx_group / lxtrading', 'lxtrading', '2019_lx_group/lxtrading', '2020-01-09 18:14:04.734723', 'system-auto', '2020-01-09 18:14:04.734723', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (324, '妈妈纷享小程序+uni-app', 'git@git.mamaqunaer.cc:2019_lx_group/enjoyWeApp.git', 'http://git.mamaqunaer.cc/2019_lx_group/enjoyWeApp.git', 'http://git.mamaqunaer.cc/2019_lx_group/enjoyWeApp', 'enjoyWeApp', '2019_lx_group / enjoyWeApp', 'enjoyWeApp', '2019_lx_group/enjoyWeApp', '2020-01-09 18:14:04.739653', 'system-auto', '2020-01-09 18:14:04.739653', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (316, '妈妈优选平台端', 'git@git.mamaqunaer.cc:2019_lx_group/platform.git', 'http://git.mamaqunaer.cc/2019_lx_group/platform.git', 'http://git.mamaqunaer.cc/2019_lx_group/platform', 'platform', '2019_lx_group / platform', 'platform', '2019_lx_group/platform', '2020-01-09 18:14:04.758325', 'system-auto', '2020-01-09 18:14:04.758325', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (313, '妈妈优选卖家端后台', 'git@git.mamaqunaer.cc:2019_lx_group/sellerBackstage.git', 'http://git.mamaqunaer.cc/2019_lx_group/sellerBackstage.git', 'http://git.mamaqunaer.cc/2019_lx_group/sellerBackstage', 'sellerBackstage', '2019_lx_group / sellerBackstage', 'sellerBackstage', '2019_lx_group/sellerBackstage', '2020-01-09 18:14:04.764046', 'system-auto', '2020-01-09 18:14:04.764046', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (308, '用户中心后台管理', 'git@git.mamaqunaer.cc:2019_lx_group/userBackstage.git', 'http://git.mamaqunaer.cc/2019_lx_group/userBackstage.git', 'http://git.mamaqunaer.cc/2019_lx_group/userBackstage', 'userBackstage', '2019_lx_group / userBackstage', 'userBackstage', '2019_lx_group/userBackstage', '2020-01-09 18:14:04.772852', 'system-auto', '2020-01-09 18:14:04.772852', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (306, '帕利亚多官网html&css', 'git@git.mamaqunaer.cc:2019_lx_group/pallyMore.git', 'http://git.mamaqunaer.cc/2019_lx_group/pallyMore.git', 'http://git.mamaqunaer.cc/2019_lx_group/pallyMore', 'pallyMore', '2019_lx_group / pallyMore', 'pallyMore', '2019_lx_group/pallyMore', '2020-01-09 18:14:04.776526', 'system-auto', '2020-01-09 18:14:04.776526', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (303, 'mpvue', 'git@git.mamaqunaer.cc:2019_lx_group/sparkWeApp.git', 'http://git.mamaqunaer.cc/2019_lx_group/sparkWeApp.git', 'http://git.mamaqunaer.cc/2019_lx_group/sparkWeApp', 'sparkWeApp', '2019_lx_group / sparkWeApp', 'sparkWeApp', '2019_lx_group/sparkWeApp', '2020-01-09 18:14:04.780519', 'system-auto', '2020-01-09 18:14:04.780519', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (297, '数据大屏1.0', 'git@git.mamaqunaer.cc:2019_lx_group/dataScreen.git', 'http://git.mamaqunaer.cc/2019_lx_group/dataScreen.git', 'http://git.mamaqunaer.cc/2019_lx_group/dataScreen', 'dataScreen', '2019_lx_group / dataScreen', 'dataScreen', '2019_lx_group/dataScreen', '2020-01-09 18:14:04.794572', 'system-auto', '2020-01-09 18:14:04.794572', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (290, 'mutuki.cn', 'git@git.mamaqunaer.cc:2019_lx_group/mutuki.git', 'http://git.mamaqunaer.cc/2019_lx_group/mutuki.git', 'http://git.mamaqunaer.cc/2019_lx_group/mutuki', 'mutuki', '2019_lx_group / mutuki', 'mutuki', '2019_lx_group/mutuki', '2020-01-09 18:14:04.799266', 'system-auto', '2020-01-09 18:14:04.799266', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (121, 'supplier', 'git@git.mamaqunaer.cc:pcGroup/supplier.git', 'http://git.mamaqunaer.cc/pcGroup/supplier.git', 'http://git.mamaqunaer.cc/pcGroup/supplier', 'supplier', 'pcGroup / supplier', 'supplier', 'pcGroup/supplier', '2020-01-09 18:14:04.925421', 'system-auto', '2020-01-09 18:14:04.925421', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (331, '消息队列客户端', 'git@git.mamaqunaer.cc:mall/messagequeue.git', 'http://git.mamaqunaer.cc/mall/messagequeue.git', 'http://git.mamaqunaer.cc/mall/messagequeue', 'messagequeue', 'mall / messagequeue', 'messagequeue', 'mall/messagequeue', '2020-01-09 18:14:04.727689', 'system-auto', '2020-01-09 18:14:04.727689', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (329, 'Maven 依赖及版本管理', 'git@git.mamaqunaer.cc:mall/mamaqunaer-dependencies.git', 'http://git.mamaqunaer.cc/mall/mamaqunaer-dependencies.git', 'http://git.mamaqunaer.cc/mall/mamaqunaer-dependencies', 'mamaqunaer-dependencies', 'mall / mamaqunaer-dependencies', 'mamaqunaer-dependencies', 'mall/mamaqunaer-dependencies', '2020-01-09 18:14:04.730455', 'system-auto', '2020-01-09 18:14:04.730455', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (318, '妈妈优选/妈妈纷享后台CMS系统（含schedule定时调度系统）', 'git@git.mamaqunaer.cc:mall/youxuan-cms.git', 'http://git.mamaqunaer.cc/mall/youxuan-cms.git', 'http://git.mamaqunaer.cc/mall/youxuan-cms', 'youxuan-cms', 'mall / youxuan-cms', 'youxuan-cms', 'mall/youxuan-cms', '2020-01-09 18:14:04.742144', 'system-auto', '2020-01-09 18:14:04.742144', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (317, '妈妈优选/妈妈纷享对外系统（买家端、卖家端）', 'git@git.mamaqunaer.cc:mall/youxuan.git', 'http://git.mamaqunaer.cc/mall/youxuan.git', 'http://git.mamaqunaer.cc/mall/youxuan', 'youxuan', 'mall / youxuan', 'youxuan', 'mall/youxuan', '2020-01-09 18:14:04.753714', 'system-auto', '2020-01-09 18:14:04.753714', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (310, '通用应用监控平台（采集数据包括数据库、中间件等）', 'git@git.mamaqunaer.cc:mall/spring-boot-actuator-universal.git', 'http://git.mamaqunaer.cc/mall/spring-boot-actuator-universal.git', 'http://git.mamaqunaer.cc/mall/spring-boot-actuator-universal', 'spring-boot-actuator-universal', 'mall / spring-boot-actuator-universal', 'spring-boot-actuator-universal', 'mall/spring-boot-actuator-universal', '2020-01-09 18:14:04.767292', 'system-auto', '2020-01-09 18:14:04.767292', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (309, '进货商城、ERP与金蝶数据交换系统（定时任务）', 'git@git.mamaqunaer.cc:mall/schedule-kd.git', 'http://git.mamaqunaer.cc/mall/schedule-kd.git', 'http://git.mamaqunaer.cc/mall/schedule-kd', 'schedule-kd', 'mall / schedule-kd', 'schedule-kd', 'mall/schedule-kd', '2020-01-09 18:14:04.770268', 'system-auto', '2020-01-09 18:14:04.770268', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (302, '星火计划CMS', 'git@git.mamaqunaer.cc:mall/xinghuo-cms.git', 'http://git.mamaqunaer.cc/mall/xinghuo-cms.git', 'http://git.mamaqunaer.cc/mall/xinghuo-cms', 'xinghuo-cms', 'mall / xinghuo-cms', 'xinghuo-cms', 'mall/xinghuo-cms', '2020-01-09 18:14:04.783665', 'system-auto', '2020-01-09 18:14:04.783665', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (301, '星火计划', 'git@git.mamaqunaer.cc:mall/xinghuo.git', 'http://git.mamaqunaer.cc/mall/xinghuo.git', 'http://git.mamaqunaer.cc/mall/xinghuo', 'xinghuo', 'mall / xinghuo', 'xinghuo', 'mall/xinghuo', '2020-01-09 18:14:04.786936', 'system-auto', '2020-01-09 18:14:04.786936', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (300, '星火计划管理后台', 'git@git.mamaqunaer.cc:2019_lx_group/spark_BMS.git', 'http://git.mamaqunaer.cc/2019_lx_group/spark_BMS.git', 'http://git.mamaqunaer.cc/2019_lx_group/spark_BMS', 'spark_BMS', '2019_lx_group / spark_BMS', 'spark_BMS', '2019_lx_group/spark_BMS', '2020-01-09 18:14:04.790894', 'system-auto', '2020-01-09 18:14:04.790894', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (295, '数据大屏', 'git@git.mamaqunaer.cc:mall/data-platform.git', 'http://git.mamaqunaer.cc/mall/data-platform.git', 'http://git.mamaqunaer.cc/mall/data-platform', 'data-platform', 'mall / data-platform', 'data-platform', 'mall/data-platform', '2020-01-09 18:14:04.796971', 'system-auto', '2020-01-09 18:14:04.796971', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (260, '配置文件资源库', 'git@git.mamaqunaer.cc:mall/config-repository.git', 'http://git.mamaqunaer.cc/mall/config-repository.git', 'http://git.mamaqunaer.cc/mall/config-repository', 'config-repository', 'mall / config-repository', 'config-repository', 'mall/config-repository', '2020-01-09 18:14:04.805522', 'system-auto', '2020-01-09 18:14:04.805522', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (110, 'MallBbackstage', 'git@git.mamaqunaer.cc:pcGroup/MallBbackstage.git', 'http://git.mamaqunaer.cc/pcGroup/MallBbackstage.git', 'http://git.mamaqunaer.cc/pcGroup/MallBbackstage', 'MallBbackstage', 'pcGroup / MallBbackstage', 'MallBbackstage', 'pcGroup/MallBbackstage', '2020-01-09 18:14:04.928088', 'system-auto', '2020-01-09 18:14:04.928088', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (109, 'supplierBackstage', 'git@git.mamaqunaer.cc:pcGroup/supplierBackstage.git', 'http://git.mamaqunaer.cc/pcGroup/supplierBackstage.git', 'http://git.mamaqunaer.cc/pcGroup/supplierBackstage', 'supplierBackstage', 'pcGroup / supplierBackstage', 'supplierBackstage', 'pcGroup/supplierBackstage', '2020-01-09 18:14:04.930825', 'system-auto', '2020-01-09 18:14:04.930825', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (211, '商品中心平台', 'git@git.mamaqunaer.cc:mall/item-center-platform.git', 'http://git.mamaqunaer.cc/mall/item-center-platform.git', 'http://git.mamaqunaer.cc/mall/item-center-platform', 'item-center-platform', 'mall / item-center-platform', 'item-center-platform', 'mall/item-center-platform', '2020-01-09 18:14:04.814282', 'system-auto', '2020-01-09 18:14:04.814282', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (197, '收银系统平台端', 'git@git.mamaqunaer.cc:mall/pos-platform.git', 'http://git.mamaqunaer.cc/mall/pos-platform.git', 'http://git.mamaqunaer.cc/mall/pos-platform', 'pos-platform', 'mall / pos-platform', 'pos-platform', 'mall/pos-platform', '2020-01-09 18:14:04.822891', 'system-auto', '2020-01-09 18:14:04.822891', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (192, '收银系统销售单服务', 'git@git.mamaqunaer.cc:mall/pos-order-center-del.git', 'http://git.mamaqunaer.cc/mall/pos-order-center-del.git', 'http://git.mamaqunaer.cc/mall/pos-order-center-del', 'pos-order-center-del', 'mall / pos-order-center-del', 'pos-order-center-del', 'mall/pos-order-center-del', '2020-01-09 18:14:04.838367', 'system-auto', '2020-01-09 18:14:04.838367', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (174, '配置中心', 'git@git.mamaqunaer.cc:mall/config-server.git', 'http://git.mamaqunaer.cc/mall/config-server.git', 'http://git.mamaqunaer.cc/mall/config-server', 'config-server', 'mall / config-server', 'config-server', 'mall/config-server', '2020-01-09 18:14:04.860511', 'system-auto', '2020-01-09 18:14:04.860511', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (171, '', 'git@git.mamaqunaer.cc:pcGroup/supplier3.0.git', 'http://git.mamaqunaer.cc/pcGroup/supplier3.0.git', 'http://git.mamaqunaer.cc/pcGroup/supplier3.0', 'supplier3.0', 'pcGroup / supplier3.0', 'supplier3.0', 'pcGroup/supplier3.0', '2020-01-09 18:14:04.863546', 'system-auto', '2020-01-09 18:14:04.863546', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (164, 'vue+element 商品中心', 'git@git.mamaqunaer.cc:pcGroup/commodityCenter.git', 'http://git.mamaqunaer.cc/pcGroup/commodityCenter.git', 'http://git.mamaqunaer.cc/pcGroup/commodityCenter', 'commodityCenter', 'pcGroup / commodityCenter', 'commodityCenter', 'pcGroup/commodityCenter', '2020-01-09 18:14:04.866385', 'system-auto', '2020-01-09 18:14:04.866385', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (159, '用户中心', 'git@git.mamaqunaer.cc:mall/user-center.git', 'http://git.mamaqunaer.cc/mall/user-center.git', 'http://git.mamaqunaer.cc/mall/user-center', 'user-center', 'mall / user-center', 'user-center', 'mall/user-center', '2020-01-09 18:14:04.869107', 'system-auto', '2020-01-09 18:14:04.869107', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (156, '订单中心', 'git@git.mamaqunaer.cc:mall/order-center.git', 'http://git.mamaqunaer.cc/mall/order-center.git', 'http://git.mamaqunaer.cc/mall/order-center', 'order-center', 'mall / order-center', 'order-center', 'mall/order-center', '2020-01-09 18:14:04.877719', 'system-auto', '2020-01-09 18:14:04.877719', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (152, '通用工具类', 'git@git.mamaqunaer.cc:mall/common.git', 'http://git.mamaqunaer.cc/mall/common.git', 'http://git.mamaqunaer.cc/mall/common', 'common', 'mall / common', 'common', 'mall/common', '2020-01-09 18:14:04.880455', 'system-auto', '2020-01-09 18:14:04.880455', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (151, '权限管理', 'git@git.mamaqunaer.cc:mall/authority.git', 'http://git.mamaqunaer.cc/mall/authority.git', 'http://git.mamaqunaer.cc/mall/authority', 'authority', 'mall / authority', 'authority', 'mall/authority', '2020-01-09 18:14:04.883621', 'system-auto', '2020-01-09 18:14:04.883621', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (150, '', 'git@git.mamaqunaer.cc:pcGroup/MallBackStage3.0.git', 'http://git.mamaqunaer.cc/pcGroup/MallBackStage3.0.git', 'http://git.mamaqunaer.cc/pcGroup/MallBackStage3.0', 'MallBackStage3.0', 'pcGroup / MallBackStage3.0', 'MallBackStage3.0', 'pcGroup/MallBackStage3.0', '2020-01-09 18:14:04.886544', 'system-auto', '2020-01-09 18:14:04.886544', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (99, '会话模块', 'git@git.mamaqunaer.cc:mall/session.git', 'http://git.mamaqunaer.cc/mall/session.git', 'http://git.mamaqunaer.cc/mall/session', 'session', 'mall / session', 'session', 'mall/session', '2020-01-09 18:14:04.934149', 'system-auto', '2020-01-09 18:14:04.934149', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (98, '发送消息的客户端', 'git@git.mamaqunaer.cc:mall/sms.git', 'http://git.mamaqunaer.cc/mall/sms.git', 'http://git.mamaqunaer.cc/mall/sms', 'sms', 'mall / sms', 'sms', 'mall/sms', '2020-01-09 18:14:04.936477', 'system-auto', '2020-01-09 18:14:04.936477', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (97, '缓存模块', 'git@git.mamaqunaer.cc:mall/cache.git', 'http://git.mamaqunaer.cc/mall/cache.git', 'http://git.mamaqunaer.cc/mall/cache', 'cache', 'mall / cache', 'cache', 'mall/cache', '2020-01-09 18:14:04.939036', 'system-auto', '2020-01-09 18:14:04.939036', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (90, '进货商城供应商应用', 'git@git.mamaqunaer.cc:mall/supplier.git', 'http://git.mamaqunaer.cc/mall/supplier.git', 'http://git.mamaqunaer.cc/mall/supplier', 'supplier', 'mall / supplier', 'supplier', 'mall/supplier', '2020-01-09 18:14:04.941939', 'system-auto', '2020-01-09 18:14:04.941939', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (89, '进货商城CMS系统', 'git@git.mamaqunaer.cc:mall/cms.git', 'http://git.mamaqunaer.cc/mall/cms.git', 'http://git.mamaqunaer.cc/mall/cms', 'cms', 'mall / cms', 'cms', 'mall/cms', '2020-01-09 18:14:04.94486', 'system-auto', '2020-01-09 18:14:04.94486', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (255, 'spring cloud网关服务', 'git@git.mamaqunaer.cc:mall/gateway.git', 'http://git.mamaqunaer.cc/mall/gateway.git', 'http://git.mamaqunaer.cc/mall/gateway', 'gateway', 'mall / gateway', 'gateway', 'mall/gateway', '2020-01-09 18:14:04.808113', 'system-auto', '2020-01-09 18:14:04.808113', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (213, '用户中心平台', 'git@git.mamaqunaer.cc:mall/user-center-platform.git', 'http://git.mamaqunaer.cc/mall/user-center-platform.git', 'http://git.mamaqunaer.cc/mall/user-center-platform', 'user-center-platform', 'mall / user-center-platform', 'user-center-platform', 'mall/user-center-platform', '2020-01-09 18:14:04.811217', 'system-auto', '2020-01-09 18:14:04.811217', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (196, '收银系统商户端', 'git@git.mamaqunaer.cc:mall/pos-shop.git', 'http://git.mamaqunaer.cc/mall/pos-shop.git', 'http://git.mamaqunaer.cc/mall/pos-shop', 'pos-shop', 'mall / pos-shop', 'pos-shop', 'mall/pos-shop', '2020-01-09 18:14:04.825445', 'system-auto', '2020-01-09 18:14:04.825445', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (178, '', 'git@git.mamaqunaer.cc:mall/hystrix-turbine.git', 'http://git.mamaqunaer.cc/mall/hystrix-turbine.git', 'http://git.mamaqunaer.cc/mall/hystrix-turbine', 'hystrix-turbine', 'mall / hystrix-turbine', 'hystrix-turbine', 'mall/hystrix-turbine', '2020-01-09 18:14:04.846064', 'system-auto', '2020-01-09 18:14:04.846064', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (158, 'spring cloud注册中心', 'git@git.mamaqunaer.cc:mall/spring-cloud-server.git', 'http://git.mamaqunaer.cc/mall/spring-cloud-server.git', 'http://git.mamaqunaer.cc/mall/spring-cloud-server', 'spring-cloud-server', 'mall / spring-cloud-server', 'spring-cloud-server', 'mall/spring-cloud-server', '2020-01-09 18:14:04.871405', 'system-auto', '2020-01-09 18:14:04.871405', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (157, '商品中心', 'git@git.mamaqunaer.cc:mall/item-center.git', 'http://git.mamaqunaer.cc/mall/item-center.git', 'http://git.mamaqunaer.cc/mall/item-center', 'item-center', 'mall / item-center', 'item-center', 'mall/item-center', '2020-01-09 18:14:04.873874', 'system-auto', '2020-01-09 18:14:04.873874', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (140, 'vue + elementUI', 'git@git.mamaqunaer.cc:pcGroup/mamaBackstage.git', 'http://git.mamaqunaer.cc/pcGroup/mamaBackstage.git', 'http://git.mamaqunaer.cc/pcGroup/mamaBackstage', 'mamaBackstage', 'pcGroup / mamaBackstage', 'mamaBackstage', 'pcGroup/mamaBackstage', '2020-01-09 18:14:04.90089', 'system-auto', '2020-01-09 18:14:04.90089', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (139, 'www官网的cms系统', 'git@git.mamaqunaer.cc:mall/www-mamaqunaer-cms.git', 'http://git.mamaqunaer.cc/mall/www-mamaqunaer-cms.git', 'http://git.mamaqunaer.cc/mall/www-mamaqunaer-cms', 'www-mamaqunaer-cms', 'mall / www-mamaqunaer-cms', 'www-mamaqunaer-cms', 'mall/www-mamaqunaer-cms', '2020-01-09 18:14:04.904089', 'system-auto', '2020-01-09 18:14:04.904089', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (132, '联星erp', 'git@git.mamaqunaer.cc:pcGroup/lxERP.git', 'http://git.mamaqunaer.cc/pcGroup/lxERP.git', 'http://git.mamaqunaer.cc/pcGroup/lxERP', 'lxERP', 'pcGroup / lxERP', 'lxERP', 'pcGroup/lxERP', '2020-01-09 18:14:04.915435', 'system-auto', '2020-01-09 18:14:04.915435', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (125, '进货商城ERP系统', 'git@git.mamaqunaer.cc:mall/erp.git', 'http://git.mamaqunaer.cc/mall/erp.git', 'http://git.mamaqunaer.cc/mall/erp', 'erp', 'mall / erp', 'erp', 'mall/erp', '2020-01-09 18:14:04.919513', 'system-auto', '2020-01-09 18:14:04.919513', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (124, '搜索引擎客户端', 'git@git.mamaqunaer.cc:mall/es.git', 'http://git.mamaqunaer.cc/mall/es.git', 'http://git.mamaqunaer.cc/mall/es', 'es', 'mall / es', 'es', 'mall/es', '2020-01-09 18:14:04.922124', 'system-auto', '2020-01-09 18:14:04.922124', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (84, '供应商商城', 'git@git.mamaqunaer.cc:pcGroup/supplierMall.git', 'http://git.mamaqunaer.cc/pcGroup/supplierMall.git', 'http://git.mamaqunaer.cc/pcGroup/supplierMall', 'supplierMall', 'pcGroup / supplierMall', 'supplierMall', 'pcGroup/supplierMall', '2020-01-09 18:14:04.948093', 'system-auto', '2020-01-09 18:14:04.948093', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (81, '进货商城门店应用', 'git@git.mamaqunaer.cc:mall/xiaodian.git', 'http://git.mamaqunaer.cc/mall/xiaodian.git', 'http://git.mamaqunaer.cc/mall/xiaodian', 'xiaodian', 'mall / xiaodian', 'xiaodian', 'mall/xiaodian', '2020-01-09 18:14:04.950478', 'system-auto', '2020-01-09 18:14:04.950478', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (79, '进货商城相关文档', 'git@git.mamaqunaer.cc:mall/docs.git', 'http://git.mamaqunaer.cc/mall/docs.git', 'http://git.mamaqunaer.cc/mall/docs', 'docs', 'mall / docs', 'docs', 'mall/docs', '2020-01-09 18:14:04.952941', 'system-auto', '2020-01-09 18:14:04.952941', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (334, '集成阿里云OSS的客户端（上传图片等文件）', 'git@git.mamaqunaer.cc:mall/oss.git', 'http://git.mamaqunaer.cc/mall/oss.git', 'http://git.mamaqunaer.cc/mall/oss', 'oss', 'mall / oss', 'oss', 'mall/oss', '2020-01-09 18:14:04.709267', 'system-auto', '2020-01-09 18:14:04.709267', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (332, '玥坤皛官网', 'git@git.mamaqunaer.cc:2019_lx_group/yuekunxiao.git', 'http://git.mamaqunaer.cc/2019_lx_group/yuekunxiao.git', 'http://git.mamaqunaer.cc/2019_lx_group/yuekunxiao', 'yuekunxiao', '2019_lx_group / yuekunxiao', 'yuekunxiao', '2019_lx_group/yuekunxiao', '2020-01-09 18:14:04.72283', 'system-auto', '2020-01-09 18:14:04.72283', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (267, '进货商城-小程序
mpvue+vant', 'git@git.mamaqunaer.cc:2019_lx_group/mallWeapp.git', 'http://git.mamaqunaer.cc/2019_lx_group/mallWeapp.git', 'http://git.mamaqunaer.cc/2019_lx_group/mallWeapp', 'mallWeapp', '2019_lx_group / mallWeapp', 'mallWeapp', '2019_lx_group/mallWeapp', '2020-01-09 18:14:04.80215', 'system-auto', '2020-01-09 18:14:04.80215', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (205, '用户中心', 'git@git.mamaqunaer.cc:2019_lx_group/userCenter.git', 'http://git.mamaqunaer.cc/2019_lx_group/userCenter.git', 'http://git.mamaqunaer.cc/2019_lx_group/userCenter', 'userCenter', '2019_lx_group / userCenter', 'userCenter', '2019_lx_group/userCenter', '2020-01-09 18:14:04.817704', 'system-auto', '2020-01-09 18:14:04.817704', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (198, 'public component resource，review it by everyone', 'git@git.mamaqunaer.cc:2019_lx_group/mamaComponents.git', 'http://git.mamaqunaer.cc/2019_lx_group/mamaComponents.git', 'http://git.mamaqunaer.cc/2019_lx_group/mamaComponents', 'mamaComponents', '2019_lx_group / mamaComponents', 'mamaComponents', '2019_lx_group/mamaComponents', '2020-01-09 18:14:04.82049', 'system-auto', '2020-01-09 18:14:04.82049', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (195, 'Spring Boot 应用监控平台（界面、告警等）', 'git@git.mamaqunaer.cc:mall/spring-boot-admin-server.git', 'http://git.mamaqunaer.cc/mall/spring-boot-admin-server.git', 'http://git.mamaqunaer.cc/mall/spring-boot-admin-server', 'spring-boot-admin-server', 'mall / spring-boot-admin-server', 'spring-boot-admin-server', 'mall/spring-boot-admin-server', '2020-01-09 18:14:04.830184', 'system-auto', '2020-01-09 18:14:04.830184', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (194, '收银系统商品中心', 'git@git.mamaqunaer.cc:mall/pos-item-center.git', 'http://git.mamaqunaer.cc/mall/pos-item-center.git', 'http://git.mamaqunaer.cc/mall/pos-item-center', 'pos-item-center', 'mall / pos-item-center', 'pos-item-center', 'mall/pos-item-center', '2020-01-09 18:14:04.833406', 'system-auto', '2020-01-09 18:14:04.833406', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (193, '收银系统销售单服务', 'git@git.mamaqunaer.cc:mall/pos-order-center.git', 'http://git.mamaqunaer.cc/mall/pos-order-center.git', 'http://git.mamaqunaer.cc/mall/pos-order-center', 'pos-order-center', 'mall / pos-order-center', 'pos-order-center', 'mall/pos-order-center', '2020-01-09 18:14:04.836034', 'system-auto', '2020-01-09 18:14:04.836034', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (191, 'vue-cli3.0', 'git@git.mamaqunaer.cc:2019_lx_group/cashierSystemMall.git', 'http://git.mamaqunaer.cc/2019_lx_group/cashierSystemMall.git', 'http://git.mamaqunaer.cc/2019_lx_group/cashierSystemMall', 'cashierSystemMall', '2019_lx_group / cashierSystemMall', 'cashierSystemMall', '2019_lx_group/cashierSystemMall', '2020-01-09 18:14:04.840652', 'system-auto', '2020-01-09 18:14:04.840652', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (186, 'vue + vue-cli3.0 + elementui', 'git@git.mamaqunaer.cc:2019_lx_group/cashierSystem.git', 'http://git.mamaqunaer.cc/2019_lx_group/cashierSystem.git', 'http://git.mamaqunaer.cc/2019_lx_group/cashierSystem', 'cashierSystem', '2019_lx_group / cashierSystem', 'cashierSystem', '2019_lx_group/cashierSystem', '2020-01-09 18:14:04.843099', 'system-auto', '2020-01-09 18:14:04.843099', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (149, 'vue+elementUi', 'git@git.mamaqunaer.cc:pcGroup/saleSystem.git', 'http://git.mamaqunaer.cc/pcGroup/saleSystem.git', 'http://git.mamaqunaer.cc/pcGroup/saleSystem', 'saleSystem', 'pcGroup / saleSystem', 'saleSystem', 'pcGroup/saleSystem', '2020-01-09 18:14:04.889467', 'system-auto', '2020-01-09 18:14:04.889467', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (144, 'vue+elementUi', 'git@git.mamaqunaer.cc:pcGroup/signContract.git', 'http://git.mamaqunaer.cc/pcGroup/signContract.git', 'http://git.mamaqunaer.cc/pcGroup/signContract', 'signContract', 'pcGroup / signContract', 'signContract', 'pcGroup/signContract', '2020-01-09 18:14:04.892224', 'system-auto', '2020-01-09 18:14:04.892224', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (142, '电子合同项目', 'git@git.mamaqunaer.cc:mall/e-contract.git', 'http://git.mamaqunaer.cc/mall/e-contract.git', 'http://git.mamaqunaer.cc/mall/e-contract', 'e-contract', 'mall / e-contract', 'e-contract', 'mall/e-contract', '2020-01-09 18:14:04.895437', 'system-auto', '2020-01-09 18:14:04.895437', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (141, '序列化集成', 'git@git.mamaqunaer.cc:mall/serialization.git', 'http://git.mamaqunaer.cc/mall/serialization.git', 'http://git.mamaqunaer.cc/mall/serialization', 'serialization', 'mall / serialization', 'serialization', 'mall/serialization', '2020-01-09 18:14:04.898025', 'system-auto', '2020-01-09 18:14:04.898025', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (138, 'www官网（暂时废弃）', 'git@git.mamaqunaer.cc:mall/www-mamaqunaer.git', 'http://git.mamaqunaer.cc/mall/www-mamaqunaer.git', 'http://git.mamaqunaer.cc/mall/www-mamaqunaer', 'www-mamaqunaer', 'mall / www-mamaqunaer', 'www-mamaqunaer', 'mall/www-mamaqunaer', '2020-01-09 18:14:04.906841', 'system-auto', '2020-01-09 18:14:04.906841', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (135, 'jquery+bootstrap', 'git@git.mamaqunaer.cc:pcGroup/mamaqunaerWeb.git', 'http://git.mamaqunaer.cc/pcGroup/mamaqunaerWeb.git', 'http://git.mamaqunaer.cc/pcGroup/mamaqunaerWeb', 'mamaqunaerWeb', 'pcGroup / mamaqunaerWeb', 'mamaqunaerWeb', 'pcGroup/mamaqunaerWeb', '2020-01-09 18:14:04.90947', 'system-auto', '2020-01-09 18:14:04.90947', 'system-auto', 0);
INSERT INTO public.git_repo VALUES (133, '联星erp', 'git@git.mamaqunaer.cc:pcGroup/lxErp.git', 'http://git.mamaqunaer.cc/pcGroup/lxErp.git', 'http://git.mamaqunaer.cc/pcGroup/lxErp', 'lxErp', 'pcGroup / lxErp', 'lxErp', 'pcGroup/lxErp', '2020-01-09 18:14:04.912939', 'system-auto', '2020-01-09 18:14:04.912939', 'system-auto', 0);


--
-- Data for Name: publishment; Type: TABLE DATA; Schema: public; Owner: wangnan
--

INSERT INTO public.publishment VALUES (6, 'develop_config_server', '配置中心服务（线下环境248）', 174, 'test_v1', 'dev', '192.168.1.248', '/home/project/mama_config_server/', 'config-server', '-Xms128m -Xmx512m', NULL, NULL, NULL, 0, '2019-11-12 17:01:06.235046', 'HTTP post request', '2019-11-12 17:01:06.235046', 'HTTP post request', 0, 'target', NULL);
INSERT INTO public.publishment VALUES (5, 'develop_spring_boot_actuator_universal', '全局应用监控（线下）', 310, 'develop,master', 'dev', '192.168.1.249', '/data/project/mama_spring_boot_actuator_universal', 'spring-boot-actuator-universal', '-Xms256m -Xmx768m', 'master', 'v1.0.0-test', '测试发布系统打标签', 1, '2019-11-11 17:15:18.058975', 'HTTP post request', '2019-11-11 17:15:18.058975', 'HTTP post request', 0, 'target', NULL);
INSERT INTO public.publishment VALUES (7, 'develop_www_cms', 'www官网后台（249线下环境）', 139, 'develop', 'dev', '192.168.1.249', '/data/project/mama_www_cms', 'www-cms-web', NULL, NULL, NULL, NULL, 0, '2019-12-11 19:02:07.716065', 'HTTP post request', '2019-12-11 19:02:07.716065', 'HTTP post request', 0, 'www-cms-web/target', 'branches');


--
-- Data for Name: publishment_fe_vue; Type: TABLE DATA; Schema: public; Owner: wangnan
--

INSERT INTO public.publishment_fe_vue VALUES (2, 'cashierSystemMall', '收银系统店铺端测试线', 191, 'master', 'test', '192.168.1.249', '/data/project/mama_cdn/pos', '2019-12-02 10:43:23.220523', 'HTTP post request', '2019-12-02 10:43:23.220523', 'HTTP post request', 0, 'dist/');
INSERT INTO public.publishment_fe_vue VALUES (1, 'develop_xh_cms', '星火计划CMS（线下环境）', 300, 'master', 'test', '192.168.1.249', '/data/project/logs', '2019-11-26 12:27:13.565948', 'HTTP post request', '2019-11-26 12:27:13.565948', 'HTTP post request', 0, 'dist/');


--
-- Data for Name: publishment_nodejs; Type: TABLE DATA; Schema: public; Owner: wangnan
--

INSERT INTO public.publishment_nodejs VALUES (1, 'develop_xiaodian_fe_nodejs', '进货商城门店端前端nodejs', 79, 'master', 'test', '192.168.1.249', '/data/project/mama_xiaodian_front/mall_front222', '2019-12-07 16:21:48.975506', 'HTTP post request', '2019-12-07 16:21:48.975506', 'HTTP post request', 0, '/');


--
-- Data for Name: publishment_staticfile; Type: TABLE DATA; Schema: public; Owner: wangnan
--

INSERT INTO public.publishment_staticfile VALUES (1, 'develop_mama_cdn', 'mama cdn测试（线下环境）', 79, 'master', '192.168.1.249', '/data/project/logs', '2019-11-25 17:19:35.10133', 'HTTP post request', 0, '2019-11-25 17:19:35.10133', 'HTTP post request', 'assets/');


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: wangnan
--

INSERT INTO public."user" VALUES (2, 'admin', '123456', '超级管理员', 'devops@mamaqunaer.com', 'devops@mamaqunaer.com', '2019-12-13 15:57:25.389417', 'admin', '2019-12-13 15:57:25.389417', NULL, 0, 'devops');
INSERT INTO public."user" VALUES (4, 'xiaobei', '123456', '小贝', '153634555@qq.com', '153634555@qq.com', '2019-12-13 17:44:40.261821', 'admin', '2019-12-13 17:44:40.261821', NULL, 0, 'frontend');


--
-- Name: git_repo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wangnan
--

SELECT pg_catalog.setval('public.git_repo_id_seq', 1, false);


--
-- Name: publishment_fe_vue_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wangnan
--

SELECT pg_catalog.setval('public.publishment_fe_vue_id_seq', 2, true);


--
-- Name: publishment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wangnan
--

SELECT pg_catalog.setval('public.publishment_id_seq', 10, true);


--
-- Name: publishment_staticfile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wangnan
--

SELECT pg_catalog.setval('public.publishment_staticfile_id_seq', 4, true);


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
-- Name: user idx_login_code; Type: CONSTRAINT; Schema: public; Owner: wangnan
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT idx_login_code UNIQUE (login_code);


--
-- Name: publishment_fe_vue publishment_fe_vue_pkey; Type: CONSTRAINT; Schema: public; Owner: wangnan
--

ALTER TABLE ONLY public.publishment_fe_vue
    ADD CONSTRAINT publishment_fe_vue_pkey PRIMARY KEY (id);


--
-- Name: publishment_nodejs publishment_nodejs_pkey; Type: CONSTRAINT; Schema: public; Owner: wangnan
--

ALTER TABLE ONLY public.publishment_nodejs
    ADD CONSTRAINT publishment_nodejs_pkey PRIMARY KEY (id);


--
-- Name: publishment publishment_pkey; Type: CONSTRAINT; Schema: public; Owner: wangnan
--

ALTER TABLE ONLY public.publishment
    ADD CONSTRAINT publishment_pkey PRIMARY KEY (id);


--
-- Name: publishment_staticfile publishment_staticfile_pkey; Type: CONSTRAINT; Schema: public; Owner: wangnan
--

ALTER TABLE ONLY public.publishment_staticfile
    ADD CONSTRAINT publishment_staticfile_pkey PRIMARY KEY (id);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: wangnan
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: publishment_fe_vue publishment_fe_vue_git_repo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wangnan
--

ALTER TABLE ONLY public.publishment_fe_vue
    ADD CONSTRAINT publishment_fe_vue_git_repo_id_fkey FOREIGN KEY (git_repo_id) REFERENCES public.git_repo(id);


--
-- Name: publishment publishment_git_repo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wangnan
--

ALTER TABLE ONLY public.publishment
    ADD CONSTRAINT publishment_git_repo_id_fkey FOREIGN KEY (git_repo_id) REFERENCES public.git_repo(id);


--
-- Name: publishment_nodejs publishment_nodejs_git_repo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wangnan
--

ALTER TABLE ONLY public.publishment_nodejs
    ADD CONSTRAINT publishment_nodejs_git_repo_id_fkey FOREIGN KEY (git_repo_id) REFERENCES public.git_repo(id);


--
-- Name: publishment_staticfile publishment_staticfile_git_repo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wangnan
--

ALTER TABLE ONLY public.publishment_staticfile
    ADD CONSTRAINT publishment_staticfile_git_repo_id_fkey FOREIGN KEY (git_repo_id) REFERENCES public.git_repo(id);


--
-- PostgreSQL database dump complete
--

