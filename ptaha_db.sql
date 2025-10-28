--
-- PostgreSQL database dump
--

\restrict nWTB89QhItU1XTlOqTzNRwrPMquCFXsLsW3hoSIIX7xt0lMTepUQGJ01d2eaIlL

-- Dumped from database version 17.6
-- Dumped by pg_dump version 17.6

-- Started on 2025-10-26 21:43:11

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 220 (class 1259 OID 16703)
-- Name: active_substances; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.active_substances (
    substance_id integer NOT NULL,
    substance_name character varying(100) NOT NULL,
    description text NOT NULL
);


ALTER TABLE public.active_substances OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16702)
-- Name: active_substances_substance_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.active_substances_substance_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.active_substances_substance_id_seq OWNER TO postgres;

--
-- TOC entry 4927 (class 0 OID 0)
-- Dependencies: 219
-- Name: active_substances_substance_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.active_substances_substance_id_seq OWNED BY public.active_substances.substance_id;


--
-- TOC entry 218 (class 1259 OID 16696)
-- Name: manufacturers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.manufacturers (
    manufacturer_id integer NOT NULL,
    company_name character varying(100) NOT NULL,
    country character varying(50) NOT NULL
);


ALTER TABLE public.manufacturers OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16695)
-- Name: manufacturers_manufacturer_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.manufacturers_manufacturer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.manufacturers_manufacturer_id_seq OWNER TO postgres;

--
-- TOC entry 4928 (class 0 OID 0)
-- Dependencies: 217
-- Name: manufacturers_manufacturer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.manufacturers_manufacturer_id_seq OWNED BY public.manufacturers.manufacturer_id;


--
-- TOC entry 223 (class 1259 OID 16720)
-- Name: preparation_composition; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.preparation_composition (
    preparation_id integer NOT NULL,
    substance_id integer NOT NULL,
    dosage character varying(50) NOT NULL
);


ALTER TABLE public.preparation_composition OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 16712)
-- Name: preparations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.preparations (
    preparation_id integer NOT NULL,
    trade_name character varying(100) NOT NULL,
    form character varying(50) NOT NULL,
    storage_conditions text NOT NULL,
    manufacturer_id integer NOT NULL
);


ALTER TABLE public.preparations OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16711)
-- Name: preparations_preparation_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.preparations_preparation_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.preparations_preparation_id_seq OWNER TO postgres;

--
-- TOC entry 4929 (class 0 OID 0)
-- Dependencies: 221
-- Name: preparations_preparation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.preparations_preparation_id_seq OWNED BY public.preparations.preparation_id;


--
-- TOC entry 4757 (class 2604 OID 16706)
-- Name: active_substances substance_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.active_substances ALTER COLUMN substance_id SET DEFAULT nextval('public.active_substances_substance_id_seq'::regclass);


--
-- TOC entry 4756 (class 2604 OID 16699)
-- Name: manufacturers manufacturer_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.manufacturers ALTER COLUMN manufacturer_id SET DEFAULT nextval('public.manufacturers_manufacturer_id_seq'::regclass);


--
-- TOC entry 4758 (class 2604 OID 16715)
-- Name: preparations preparation_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.preparations ALTER COLUMN preparation_id SET DEFAULT nextval('public.preparations_preparation_id_seq'::regclass);


--
-- TOC entry 4918 (class 0 OID 16703)
-- Dependencies: 220
-- Data for Name: active_substances; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.active_substances (substance_id, substance_name, description) FROM stdin;
3	Drotaverine	Спазмолітик.
2	Paracetamol	Анальгетик та антипіретик (знеболююче та жарознижуюче).
1	Ibuprofen	Нестероїдний протизапальний препарат (НПЗП).
\.


--
-- TOC entry 4916 (class 0 OID 16696)
-- Dependencies: 218
-- Data for Name: manufacturers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.manufacturers (manufacturer_id, company_name, country) FROM stdin;
1	Bayer AG	Німеччина
2	АТ "Фармак"	Україна
3	KRKA, d. d.	Словенія
\.


--
-- TOC entry 4921 (class 0 OID 16720)
-- Dependencies: 223
-- Data for Name: preparation_composition; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.preparation_composition (preparation_id, substance_id, dosage) FROM stdin;
4	1	200 мг
3	3	40 мг
2	2	500 мг
1	1	200 мг
\.


--
-- TOC entry 4920 (class 0 OID 16712)
-- Dependencies: 222
-- Data for Name: preparations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.preparations (preparation_id, trade_name, form, storage_conditions, manufacturer_id) FROM stdin;
4	Ібупрофен-Дарниця	Таблетки	Зберігати при t° до 25°C.	2
3	Но-Шпа	Таблетки	Зберігати при t° 15-25°C.	3
2	Парацетамол-Фармак	Таблетки	Зберігати в оригінальній упаковці при t° до 25°C.	2
1	Нурофєн	Таблетки вкриті оболонкою	Зберігати при t° до 25°C у сухому місці.	1
\.


--
-- TOC entry 4930 (class 0 OID 0)
-- Dependencies: 219
-- Name: active_substances_substance_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.active_substances_substance_id_seq', 1, false);


--
-- TOC entry 4931 (class 0 OID 0)
-- Dependencies: 217
-- Name: manufacturers_manufacturer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.manufacturers_manufacturer_id_seq', 1, false);


--
-- TOC entry 4932 (class 0 OID 0)
-- Dependencies: 221
-- Name: preparations_preparation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.preparations_preparation_id_seq', 1, false);


--
-- TOC entry 4762 (class 2606 OID 16710)
-- Name: active_substances active_substances_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.active_substances
    ADD CONSTRAINT active_substances_pkey PRIMARY KEY (substance_id);


--
-- TOC entry 4760 (class 2606 OID 16701)
-- Name: manufacturers manufacturers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.manufacturers
    ADD CONSTRAINT manufacturers_pkey PRIMARY KEY (manufacturer_id);


--
-- TOC entry 4766 (class 2606 OID 16724)
-- Name: preparation_composition preparation_composition_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.preparation_composition
    ADD CONSTRAINT preparation_composition_pkey PRIMARY KEY (preparation_id, substance_id);


--
-- TOC entry 4764 (class 2606 OID 16719)
-- Name: preparations preparations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.preparations
    ADD CONSTRAINT preparations_pkey PRIMARY KEY (preparation_id);


--
-- TOC entry 4768 (class 2606 OID 16730)
-- Name: preparation_composition preparation_composition_preparation_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.preparation_composition
    ADD CONSTRAINT preparation_composition_preparation_id_fkey FOREIGN KEY (preparation_id) REFERENCES public.preparations(preparation_id) NOT VALID;


--
-- TOC entry 4769 (class 2606 OID 16735)
-- Name: preparation_composition preparation_composition_substance_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.preparation_composition
    ADD CONSTRAINT preparation_composition_substance_id_fkey FOREIGN KEY (substance_id) REFERENCES public.active_substances(substance_id) NOT VALID;


--
-- TOC entry 4767 (class 2606 OID 16725)
-- Name: preparations preparations_manufacturer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.preparations
    ADD CONSTRAINT preparations_manufacturer_id_fkey FOREIGN KEY (manufacturer_id) REFERENCES public.manufacturers(manufacturer_id) NOT VALID;


-- Completed on 2025-10-26 21:43:11

--
-- PostgreSQL database dump complete
--

\unrestrict nWTB89QhItU1XTlOqTzNRwrPMquCFXsLsW3hoSIIX7xt0lMTepUQGJ01d2eaIlL

