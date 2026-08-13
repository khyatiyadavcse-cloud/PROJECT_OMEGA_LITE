--
-- PostgreSQL database dump
--

\restrict O319Yxg6OokWmK44C2Qi0t9i9YotWQOU2Vt9nCHsugFbY0MUwyuxsfV10dnTILk

-- Dumped from database version 17.10
-- Dumped by pg_dump version 17.10

-- Started on 2026-08-13 22:33:45

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 245 (class 1255 OID 16566)
-- Name: update_prediction_date(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.update_prediction_date() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    NEW.prediction_date = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$;


ALTER FUNCTION public.update_prediction_date() OWNER TO postgres;

--
-- TOC entry 244 (class 1255 OID 16565)
-- Name: updaterisklevel(integer, character varying); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public.updaterisklevel(IN p_device_id integer, IN p_risk_level character varying)
    LANGUAGE plpgsql
    AS $$
BEGIN
    UPDATE RiskPredictions
    SET risk_level = p_risk_level
    WHERE device_id = p_device_id;
END;
$$;


ALTER PROCEDURE public.updaterisklevel(IN p_device_id integer, IN p_risk_level character varying) OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 224 (class 1259 OID 16421)
-- Name: devices; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.devices (
    device_id integer NOT NULL,
    user_id integer,
    device_name character varying(100),
    device_type character varying(50),
    ip_address character varying(30),
    os_id integer,
    last_scan timestamp without time zone,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.devices OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16420)
-- Name: devices_device_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.devices_device_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.devices_device_id_seq OWNER TO postgres;

--
-- TOC entry 5046 (class 0 OID 0)
-- Dependencies: 223
-- Name: devices_device_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.devices_device_id_seq OWNED BY public.devices.device_id;


--
-- TOC entry 228 (class 1259 OID 16446)
-- Name: devicesoftware; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.devicesoftware (
    device_software_id integer NOT NULL,
    device_id integer,
    software_id integer,
    installed_version character varying(30),
    status character varying(20)
);


ALTER TABLE public.devicesoftware OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 16445)
-- Name: devicesoftware_device_software_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.devicesoftware_device_software_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.devicesoftware_device_software_id_seq OWNER TO postgres;

--
-- TOC entry 5047 (class 0 OID 0)
-- Dependencies: 227
-- Name: devicesoftware_device_software_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.devicesoftware_device_software_id_seq OWNED BY public.devicesoftware.device_software_id;


--
-- TOC entry 232 (class 1259 OID 16473)
-- Name: devicevulnerabilities; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.devicevulnerabilities (
    device_vulnerability_id integer NOT NULL,
    device_id integer,
    vulnerability_id integer,
    status character varying(20),
    detected_at timestamp without time zone
);


ALTER TABLE public.devicevulnerabilities OWNER TO postgres;

--
-- TOC entry 231 (class 1259 OID 16472)
-- Name: devicevulnerabilities_device_vulnerability_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.devicevulnerabilities_device_vulnerability_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.devicevulnerabilities_device_vulnerability_id_seq OWNER TO postgres;

--
-- TOC entry 5048 (class 0 OID 0)
-- Dependencies: 231
-- Name: devicevulnerabilities_device_vulnerability_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.devicevulnerabilities_device_vulnerability_id_seq OWNED BY public.devicevulnerabilities.device_vulnerability_id;


--
-- TOC entry 236 (class 1259 OID 16502)
-- Name: riskpredictions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.riskpredictions (
    prediction_id integer NOT NULL,
    device_id integer,
    risk_score integer,
    risk_level character varying(20),
    prediction_probability numeric(5,2),
    prediction_date timestamp without time zone
);


ALTER TABLE public.riskpredictions OWNER TO postgres;

--
-- TOC entry 241 (class 1259 OID 16547)
-- Name: highriskdevices; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.highriskdevices AS
 SELECT d.device_name,
    r.risk_score,
    r.risk_level
   FROM (public.riskpredictions r
     JOIN public.devices d ON ((r.device_id = d.device_id)))
  WHERE ((r.risk_level)::text = 'High'::text);


ALTER VIEW public.highriskdevices OWNER TO postgres;

--
-- TOC entry 234 (class 1259 OID 16490)
-- Name: loginhistory; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.loginhistory (
    login_id integer NOT NULL,
    device_id integer,
    login_time timestamp without time zone,
    failed_attempts integer,
    successful_logins integer,
    location character varying(100),
    ip_address character varying(30)
);


ALTER TABLE public.loginhistory OWNER TO postgres;

--
-- TOC entry 233 (class 1259 OID 16489)
-- Name: loginhistory_login_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.loginhistory_login_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.loginhistory_login_id_seq OWNER TO postgres;

--
-- TOC entry 5049 (class 0 OID 0)
-- Dependencies: 233
-- Name: loginhistory_login_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.loginhistory_login_id_seq OWNED BY public.loginhistory.login_id;


--
-- TOC entry 230 (class 1259 OID 16464)
-- Name: vulnerabilities; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vulnerabilities (
    vulnerability_id integer NOT NULL,
    cve_id character varying(30),
    title character varying(255),
    severity character varying(20),
    cvss_score numeric(3,1),
    description text,
    published_date date
);


ALTER TABLE public.vulnerabilities OWNER TO postgres;

--
-- TOC entry 242 (class 1259 OID 16551)
-- Name: openvulnerabilities; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.openvulnerabilities AS
 SELECT d.device_name,
    v.cve_id,
    v.title,
    v.severity
   FROM ((public.devicevulnerabilities dv
     JOIN public.devices d ON ((dv.device_id = d.device_id)))
     JOIN public.vulnerabilities v ON ((dv.vulnerability_id = v.vulnerability_id)))
  WHERE ((dv.status)::text = 'Open'::text);


ALTER VIEW public.openvulnerabilities OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 16414)
-- Name: operatingsystems; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.operatingsystems (
    os_id integer NOT NULL,
    os_name character varying(50),
    version character varying(30),
    vendor character varying(50)
);


ALTER TABLE public.operatingsystems OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16413)
-- Name: operatingsystems_os_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.operatingsystems_os_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.operatingsystems_os_id_seq OWNER TO postgres;

--
-- TOC entry 5050 (class 0 OID 0)
-- Dependencies: 221
-- Name: operatingsystems_os_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.operatingsystems_os_id_seq OWNED BY public.operatingsystems.os_id;


--
-- TOC entry 238 (class 1259 OID 16515)
-- Name: recommendations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.recommendations (
    recommendation_id integer NOT NULL,
    prediction_id integer,
    recommendation_text text,
    priority character varying(20),
    status character varying(20)
);


ALTER TABLE public.recommendations OWNER TO postgres;

--
-- TOC entry 243 (class 1259 OID 16556)
-- Name: pendingrecommendations; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.pendingrecommendations AS
 SELECT recommendation_text,
    priority,
    status
   FROM public.recommendations
  WHERE ((status)::text = 'Pending'::text);


ALTER VIEW public.pendingrecommendations OWNER TO postgres;

--
-- TOC entry 237 (class 1259 OID 16514)
-- Name: recommendations_recommendation_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.recommendations_recommendation_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.recommendations_recommendation_id_seq OWNER TO postgres;

--
-- TOC entry 5051 (class 0 OID 0)
-- Dependencies: 237
-- Name: recommendations_recommendation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.recommendations_recommendation_id_seq OWNED BY public.recommendations.recommendation_id;


--
-- TOC entry 240 (class 1259 OID 16529)
-- Name: reports; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.reports (
    report_id integer NOT NULL,
    prediction_id integer,
    generated_by integer,
    file_path text,
    generated_at timestamp without time zone
);


ALTER TABLE public.reports OWNER TO postgres;

--
-- TOC entry 239 (class 1259 OID 16528)
-- Name: reports_report_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.reports_report_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.reports_report_id_seq OWNER TO postgres;

--
-- TOC entry 5052 (class 0 OID 0)
-- Dependencies: 239
-- Name: reports_report_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.reports_report_id_seq OWNED BY public.reports.report_id;


--
-- TOC entry 235 (class 1259 OID 16501)
-- Name: riskpredictions_prediction_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.riskpredictions_prediction_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.riskpredictions_prediction_id_seq OWNER TO postgres;

--
-- TOC entry 5053 (class 0 OID 0)
-- Dependencies: 235
-- Name: riskpredictions_prediction_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.riskpredictions_prediction_id_seq OWNED BY public.riskpredictions.prediction_id;


--
-- TOC entry 218 (class 1259 OID 16389)
-- Name: roles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.roles (
    role_id integer NOT NULL,
    role_name character varying(50) NOT NULL
);


ALTER TABLE public.roles OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16388)
-- Name: roles_role_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.roles_role_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.roles_role_id_seq OWNER TO postgres;

--
-- TOC entry 5054 (class 0 OID 0)
-- Dependencies: 217
-- Name: roles_role_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.roles_role_id_seq OWNED BY public.roles.role_id;


--
-- TOC entry 226 (class 1259 OID 16439)
-- Name: software; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.software (
    software_id integer NOT NULL,
    software_name character varying(100),
    version character varying(30),
    vendor character varying(100),
    latest_version character varying(30)
);


ALTER TABLE public.software OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 16438)
-- Name: software_software_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.software_software_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.software_software_id_seq OWNER TO postgres;

--
-- TOC entry 5055 (class 0 OID 0)
-- Dependencies: 225
-- Name: software_software_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.software_software_id_seq OWNED BY public.software.software_id;


--
-- TOC entry 220 (class 1259 OID 16397)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    name character varying(100),
    email character varying(100),
    password_hash text,
    role_id integer,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16396)
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_user_id_seq OWNER TO postgres;

--
-- TOC entry 5056 (class 0 OID 0)
-- Dependencies: 219
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- TOC entry 229 (class 1259 OID 16463)
-- Name: vulnerabilities_vulnerability_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.vulnerabilities_vulnerability_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.vulnerabilities_vulnerability_id_seq OWNER TO postgres;

--
-- TOC entry 5057 (class 0 OID 0)
-- Dependencies: 229
-- Name: vulnerabilities_vulnerability_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.vulnerabilities_vulnerability_id_seq OWNED BY public.vulnerabilities.vulnerability_id;


--
-- TOC entry 4815 (class 2604 OID 16424)
-- Name: devices device_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.devices ALTER COLUMN device_id SET DEFAULT nextval('public.devices_device_id_seq'::regclass);


--
-- TOC entry 4818 (class 2604 OID 16449)
-- Name: devicesoftware device_software_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.devicesoftware ALTER COLUMN device_software_id SET DEFAULT nextval('public.devicesoftware_device_software_id_seq'::regclass);


--
-- TOC entry 4820 (class 2604 OID 16476)
-- Name: devicevulnerabilities device_vulnerability_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.devicevulnerabilities ALTER COLUMN device_vulnerability_id SET DEFAULT nextval('public.devicevulnerabilities_device_vulnerability_id_seq'::regclass);


--
-- TOC entry 4821 (class 2604 OID 16493)
-- Name: loginhistory login_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.loginhistory ALTER COLUMN login_id SET DEFAULT nextval('public.loginhistory_login_id_seq'::regclass);


--
-- TOC entry 4814 (class 2604 OID 16417)
-- Name: operatingsystems os_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.operatingsystems ALTER COLUMN os_id SET DEFAULT nextval('public.operatingsystems_os_id_seq'::regclass);


--
-- TOC entry 4823 (class 2604 OID 16518)
-- Name: recommendations recommendation_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recommendations ALTER COLUMN recommendation_id SET DEFAULT nextval('public.recommendations_recommendation_id_seq'::regclass);


--
-- TOC entry 4824 (class 2604 OID 16532)
-- Name: reports report_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reports ALTER COLUMN report_id SET DEFAULT nextval('public.reports_report_id_seq'::regclass);


--
-- TOC entry 4822 (class 2604 OID 16505)
-- Name: riskpredictions prediction_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.riskpredictions ALTER COLUMN prediction_id SET DEFAULT nextval('public.riskpredictions_prediction_id_seq'::regclass);


--
-- TOC entry 4811 (class 2604 OID 16392)
-- Name: roles role_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roles ALTER COLUMN role_id SET DEFAULT nextval('public.roles_role_id_seq'::regclass);


--
-- TOC entry 4817 (class 2604 OID 16442)
-- Name: software software_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.software ALTER COLUMN software_id SET DEFAULT nextval('public.software_software_id_seq'::regclass);


--
-- TOC entry 4812 (class 2604 OID 16400)
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- TOC entry 4819 (class 2604 OID 16467)
-- Name: vulnerabilities vulnerability_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vulnerabilities ALTER COLUMN vulnerability_id SET DEFAULT nextval('public.vulnerabilities_vulnerability_id_seq'::regclass);


--
-- TOC entry 5024 (class 0 OID 16421)
-- Dependencies: 224
-- Data for Name: devices; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.devices (device_id, user_id, device_name, device_type, ip_address, os_id, last_scan, created_at) FROM stdin;
1	1	Office-PC-01	Desktop	192.168.1.10	1	2026-07-18 18:03:26.967632	2026-07-18 18:03:26.967632
2	2	HR-Laptop	Laptop	192.168.1.20	2	2026-07-18 18:03:26.967632	2026-07-18 18:03:26.967632
3	3	Finance-PC	Desktop	192.168.1.30	1	2026-07-18 18:03:26.967632	2026-07-18 18:03:26.967632
4	4	Security-Server	Server	192.168.1.40	3	2026-07-18 18:03:26.967632	2026-07-18 18:03:26.967632
5	5	CEO-MacBook	Laptop	192.168.1.50	5	2026-07-18 18:03:26.967632	2026-07-18 18:03:26.967632
\.


--
-- TOC entry 5028 (class 0 OID 16446)
-- Dependencies: 228
-- Data for Name: devicesoftware; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.devicesoftware (device_software_id, device_id, software_id, installed_version, status) FROM stdin;
1	1	1	136.0	Outdated
2	1	2	2024	Updated
3	2	1	138.0	Updated
4	2	3	1.102	Updated
5	3	4	3.11	Outdated
6	4	5	17	Updated
7	5	1	138.0	Updated
8	1	1	136.0	Outdated
9	1	2	2024	Updated
10	2	1	138.0	Updated
11	2	3	1.102	Updated
12	3	4	3.11	Outdated
13	4	5	17	Updated
14	5	1	138.0	Updated
\.


--
-- TOC entry 5032 (class 0 OID 16473)
-- Dependencies: 232
-- Data for Name: devicevulnerabilities; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.devicevulnerabilities (device_vulnerability_id, device_id, vulnerability_id, status, detected_at) FROM stdin;
1	1	1	Open	2026-07-10 00:00:00
2	2	2	Open	2026-07-11 00:00:00
3	3	3	Patched	2026-07-12 00:00:00
4	4	4	Open	2026-07-13 00:00:00
5	5	5	Open	2026-07-14 00:00:00
\.


--
-- TOC entry 5034 (class 0 OID 16490)
-- Dependencies: 234
-- Data for Name: loginhistory; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.loginhistory (login_id, device_id, login_time, failed_attempts, successful_logins, location, ip_address) FROM stdin;
1	1	2026-07-15 09:30:00	0	5	Delhi	\N
2	2	2026-07-15 10:00:00	2	1	Mumbai	\N
3	3	2026-07-15 10:30:00	5	0	Bangalore	\N
4	4	2026-07-15 11:00:00	1	4	Pune	\N
5	5	2026-07-15 12:00:00	3	2	Jaipur	\N
\.


--
-- TOC entry 5022 (class 0 OID 16414)
-- Dependencies: 222
-- Data for Name: operatingsystems; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.operatingsystems (os_id, os_name, version, vendor) FROM stdin;
1	Windows	11	Microsoft
2	Windows	10	Microsoft
3	Ubuntu	22.04	Canonical
4	Kali Linux	2025.1	Offensive Security
5	macOS	Sonoma	Apple
\.


--
-- TOC entry 5038 (class 0 OID 16515)
-- Dependencies: 238
-- Data for Name: recommendations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.recommendations (recommendation_id, prediction_id, recommendation_text, priority, status) FROM stdin;
1	1	Update Windows and Antivirus	\N	Pending
2	2	Enable Firewall	\N	Pending
3	3	Patch SQL Vulnerability Immediately	\N	Completed
4	4	Reset Administrator Passwords	\N	Pending
5	5	Install Latest Security Updates	\N	Pending
\.


--
-- TOC entry 5040 (class 0 OID 16529)
-- Dependencies: 240
-- Data for Name: reports; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.reports (report_id, prediction_id, generated_by, file_path, generated_at) FROM stdin;
1	1	1	reports/report1.pdf	2026-07-29 09:40:27.074814
2	2	2	reports/report2.pdf	2026-07-29 09:40:27.074814
3	3	3	reports/report3.pdf	2026-07-29 09:40:27.074814
4	4	4	reports/report4.pdf	2026-07-29 09:40:27.074814
5	5	5	reports/report5.pdf	2026-07-29 09:40:27.074814
\.


--
-- TOC entry 5036 (class 0 OID 16502)
-- Dependencies: 236
-- Data for Name: riskpredictions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.riskpredictions (prediction_id, device_id, risk_score, risk_level, prediction_probability, prediction_date) FROM stdin;
2	2	45	Medium	\N	2026-07-16 00:00:00
3	3	88	Critical	\N	2026-07-16 00:00:00
4	4	70	High	\N	2026-07-16 00:00:00
5	5	55	Medium	\N	2026-07-16 00:00:00
1	1	95	Critical	\N	2026-07-22 10:28:42.932425
\.


--
-- TOC entry 5018 (class 0 OID 16389)
-- Dependencies: 218
-- Data for Name: roles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.roles (role_id, role_name) FROM stdin;
1	Admin
2	Analyst
3	Viewer
\.


--
-- TOC entry 5026 (class 0 OID 16439)
-- Dependencies: 226
-- Data for Name: software; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.software (software_id, software_name, version, vendor, latest_version) FROM stdin;
1	Google Chrome	\N	Google	138.0
2	Microsoft Office	\N	Microsoft	2024
3	Visual Studio Code	\N	Microsoft	1.102
4	Python	\N	Python Software Foundation	3.13
5	PostgreSQL	\N	PostgreSQL Global Development Group	17
\.


--
-- TOC entry 5020 (class 0 OID 16397)
-- Dependencies: 220
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (user_id, name, email, password_hash, role_id, created_at) FROM stdin;
1	Rahul Sharma	rahul@gmail.com	pass123	1	2026-07-18 18:02:00.041966
2	Priya Singh	priya@gmail.com	pass456	2	2026-07-18 18:02:00.041966
3	Amit Verma	amit@gmail.com	pass789	3	2026-07-18 18:02:00.041966
4	Sneha Patel	sneha@gmail.com	pass111	2	2026-07-18 18:02:00.041966
5	Rohan Gupta	rohan@gmail.com	pass222	1	2026-07-18 18:02:00.041966
\.


--
-- TOC entry 5030 (class 0 OID 16464)
-- Dependencies: 230
-- Data for Name: vulnerabilities; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.vulnerabilities (vulnerability_id, cve_id, title, severity, cvss_score, description, published_date) FROM stdin;
1	CVE-2026-1001	Remote Code Execution	Critical	9.8	Allows attacker to execute remote code	\N
2	CVE-2026-1002	Privilege Escalation	High	8.7	Allows gaining administrator access	\N
3	CVE-2026-1003	SQL Injection	Medium	6.9	Database can be manipulated	\N
4	CVE-2026-1004	Weak Authentication	High	7.5	Weak password authentication	\N
5	CVE-2026-1005	Cross Site Scripting	Low	3.4	Browser-side script execution	\N
\.


--
-- TOC entry 5058 (class 0 OID 0)
-- Dependencies: 223
-- Name: devices_device_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.devices_device_id_seq', 5, true);


--
-- TOC entry 5059 (class 0 OID 0)
-- Dependencies: 227
-- Name: devicesoftware_device_software_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.devicesoftware_device_software_id_seq', 14, true);


--
-- TOC entry 5060 (class 0 OID 0)
-- Dependencies: 231
-- Name: devicevulnerabilities_device_vulnerability_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.devicevulnerabilities_device_vulnerability_id_seq', 5, true);


--
-- TOC entry 5061 (class 0 OID 0)
-- Dependencies: 233
-- Name: loginhistory_login_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.loginhistory_login_id_seq', 5, true);


--
-- TOC entry 5062 (class 0 OID 0)
-- Dependencies: 221
-- Name: operatingsystems_os_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.operatingsystems_os_id_seq', 5, true);


--
-- TOC entry 5063 (class 0 OID 0)
-- Dependencies: 237
-- Name: recommendations_recommendation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.recommendations_recommendation_id_seq', 5, true);


--
-- TOC entry 5064 (class 0 OID 0)
-- Dependencies: 239
-- Name: reports_report_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.reports_report_id_seq', 5, true);


--
-- TOC entry 5065 (class 0 OID 0)
-- Dependencies: 235
-- Name: riskpredictions_prediction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.riskpredictions_prediction_id_seq', 5, true);


--
-- TOC entry 5066 (class 0 OID 0)
-- Dependencies: 217
-- Name: roles_role_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.roles_role_id_seq', 3, true);


--
-- TOC entry 5067 (class 0 OID 0)
-- Dependencies: 225
-- Name: software_software_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.software_software_id_seq', 5, true);


--
-- TOC entry 5068 (class 0 OID 0)
-- Dependencies: 219
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_user_id_seq', 5, true);


--
-- TOC entry 5069 (class 0 OID 0)
-- Dependencies: 229
-- Name: vulnerabilities_vulnerability_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.vulnerabilities_vulnerability_id_seq', 5, true);


--
-- TOC entry 4835 (class 2606 OID 16427)
-- Name: devices devices_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.devices
    ADD CONSTRAINT devices_pkey PRIMARY KEY (device_id);


--
-- TOC entry 4841 (class 2606 OID 16451)
-- Name: devicesoftware devicesoftware_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.devicesoftware
    ADD CONSTRAINT devicesoftware_pkey PRIMARY KEY (device_software_id);


--
-- TOC entry 4846 (class 2606 OID 16478)
-- Name: devicevulnerabilities devicevulnerabilities_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.devicevulnerabilities
    ADD CONSTRAINT devicevulnerabilities_pkey PRIMARY KEY (device_vulnerability_id);


--
-- TOC entry 4848 (class 2606 OID 16495)
-- Name: loginhistory loginhistory_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.loginhistory
    ADD CONSTRAINT loginhistory_pkey PRIMARY KEY (login_id);


--
-- TOC entry 4833 (class 2606 OID 16419)
-- Name: operatingsystems operatingsystems_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.operatingsystems
    ADD CONSTRAINT operatingsystems_pkey PRIMARY KEY (os_id);


--
-- TOC entry 4853 (class 2606 OID 16522)
-- Name: recommendations recommendations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recommendations
    ADD CONSTRAINT recommendations_pkey PRIMARY KEY (recommendation_id);


--
-- TOC entry 4855 (class 2606 OID 16536)
-- Name: reports reports_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reports
    ADD CONSTRAINT reports_pkey PRIMARY KEY (report_id);


--
-- TOC entry 4851 (class 2606 OID 16507)
-- Name: riskpredictions riskpredictions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.riskpredictions
    ADD CONSTRAINT riskpredictions_pkey PRIMARY KEY (prediction_id);


--
-- TOC entry 4826 (class 2606 OID 16394)
-- Name: roles roles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_pkey PRIMARY KEY (role_id);


--
-- TOC entry 4839 (class 2606 OID 16444)
-- Name: software software_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.software
    ADD CONSTRAINT software_pkey PRIMARY KEY (software_id);


--
-- TOC entry 4829 (class 2606 OID 16407)
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- TOC entry 4831 (class 2606 OID 16405)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- TOC entry 4844 (class 2606 OID 16471)
-- Name: vulnerabilities vulnerabilities_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vulnerabilities
    ADD CONSTRAINT vulnerabilities_pkey PRIMARY KEY (vulnerability_id);


--
-- TOC entry 4842 (class 1259 OID 16562)
-- Name: idx_cve_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_cve_id ON public.vulnerabilities USING btree (cve_id);


--
-- TOC entry 4836 (class 1259 OID 16564)
-- Name: idx_device_ip; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_device_ip ON public.devices USING btree (ip_address);


--
-- TOC entry 4837 (class 1259 OID 16560)
-- Name: idx_device_name; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_device_name ON public.devices USING btree (device_name);


--
-- TOC entry 4849 (class 1259 OID 16561)
-- Name: idx_risk_level; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_risk_level ON public.riskpredictions USING btree (risk_level);


--
-- TOC entry 4827 (class 1259 OID 16563)
-- Name: idx_user_email; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_user_email ON public.users USING btree (email);


--
-- TOC entry 4868 (class 2620 OID 16567)
-- Name: riskpredictions trg_update_prediction_date; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER trg_update_prediction_date BEFORE UPDATE ON public.riskpredictions FOR EACH ROW EXECUTE FUNCTION public.update_prediction_date();


--
-- TOC entry 4857 (class 2606 OID 16433)
-- Name: devices devices_os_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.devices
    ADD CONSTRAINT devices_os_id_fkey FOREIGN KEY (os_id) REFERENCES public.operatingsystems(os_id);


--
-- TOC entry 4858 (class 2606 OID 16428)
-- Name: devices devices_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.devices
    ADD CONSTRAINT devices_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- TOC entry 4859 (class 2606 OID 16452)
-- Name: devicesoftware devicesoftware_device_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.devicesoftware
    ADD CONSTRAINT devicesoftware_device_id_fkey FOREIGN KEY (device_id) REFERENCES public.devices(device_id);


--
-- TOC entry 4860 (class 2606 OID 16457)
-- Name: devicesoftware devicesoftware_software_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.devicesoftware
    ADD CONSTRAINT devicesoftware_software_id_fkey FOREIGN KEY (software_id) REFERENCES public.software(software_id);


--
-- TOC entry 4861 (class 2606 OID 16479)
-- Name: devicevulnerabilities devicevulnerabilities_device_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.devicevulnerabilities
    ADD CONSTRAINT devicevulnerabilities_device_id_fkey FOREIGN KEY (device_id) REFERENCES public.devices(device_id);


--
-- TOC entry 4862 (class 2606 OID 16484)
-- Name: devicevulnerabilities devicevulnerabilities_vulnerability_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.devicevulnerabilities
    ADD CONSTRAINT devicevulnerabilities_vulnerability_id_fkey FOREIGN KEY (vulnerability_id) REFERENCES public.vulnerabilities(vulnerability_id);


--
-- TOC entry 4863 (class 2606 OID 16496)
-- Name: loginhistory loginhistory_device_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.loginhistory
    ADD CONSTRAINT loginhistory_device_id_fkey FOREIGN KEY (device_id) REFERENCES public.devices(device_id);


--
-- TOC entry 4865 (class 2606 OID 16523)
-- Name: recommendations recommendations_prediction_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recommendations
    ADD CONSTRAINT recommendations_prediction_id_fkey FOREIGN KEY (prediction_id) REFERENCES public.riskpredictions(prediction_id);


--
-- TOC entry 4866 (class 2606 OID 16542)
-- Name: reports reports_generated_by_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reports
    ADD CONSTRAINT reports_generated_by_fkey FOREIGN KEY (generated_by) REFERENCES public.users(user_id);


--
-- TOC entry 4867 (class 2606 OID 16537)
-- Name: reports reports_prediction_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reports
    ADD CONSTRAINT reports_prediction_id_fkey FOREIGN KEY (prediction_id) REFERENCES public.riskpredictions(prediction_id);


--
-- TOC entry 4864 (class 2606 OID 16508)
-- Name: riskpredictions riskpredictions_device_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.riskpredictions
    ADD CONSTRAINT riskpredictions_device_id_fkey FOREIGN KEY (device_id) REFERENCES public.devices(device_id);


--
-- TOC entry 4856 (class 2606 OID 16408)
-- Name: users users_role_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_role_id_fkey FOREIGN KEY (role_id) REFERENCES public.roles(role_id);


-- Completed on 2026-08-13 22:33:46

--
-- PostgreSQL database dump complete
--

\unrestrict O319Yxg6OokWmK44C2Qi0t9i9YotWQOU2Vt9nCHsugFbY0MUwyuxsfV10dnTILk

